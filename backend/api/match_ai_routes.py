from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from database.database import SessionLocal
from services.email_service import EmailService

from repositories.candidate_repository import CandidateRepository
from repositories.job_repository import JobRepository
from repositories.evaluation_repository import EvaluationRepository

from graph.workflow import workflow
from schemas.workflow_state import WorkflowState


router = APIRouter(
    prefix="/ai",
    tags=["AI Matching"],
)


class MatchRequest(BaseModel):
    candidate_id: int
    job_id: int


@router.post("/match")
async def match_candidate(request: MatchRequest):
    db = SessionLocal()

    try:
        candidate = CandidateRepository.get_by_id(
            db,
            request.candidate_id,
        )
        if not candidate:
            raise HTTPException(status_code=404, detail="Candidate not found")

        job = JobRepository.get_by_id(
            db,
            request.job_id,
        )
        if not job:
            raise HTTPException(status_code=404, detail="Job not found")

        state = WorkflowState(
            resume_text=candidate.resume_text,
            job_description=job.description,
        )

        result = await workflow.ainvoke(state)

        # Normalize possible return shapes from LangGraph/LangChain nodes.
        # Expected: dict containing match_result, followup_questions, explanation.
        match_result = None
        overall_score = 0

        if isinstance(result, dict):
            match_result = result.get("match_result")
            if isinstance(match_result, dict):
                overall_score = match_result.get("overall_score", result.get("overall_score", 0))
            else:
                overall_score = result.get("overall_score", 0)
        else:
            match_result = getattr(result, "match_result", None)
            if isinstance(match_result, dict):
                overall_score = match_result.get("overall_score", getattr(result, "overall_score", 0))
            else:
                overall_score = getattr(result, "overall_score", 0) or 0

        if match_result is None or not isinstance(match_result, dict):
            raise HTTPException(status_code=500, detail="AI matching returned unexpected result shape")

        score = overall_score or 0

        # Email shortlist
        if score >= 70 and getattr(candidate, "email", None):
            EmailService.send_shortlisted_email(
                to_email=candidate.email,
                candidate_name=candidate.name,
                score=score,
            )

        # Persist evaluation (signature may vary; try both)
        try:
            EvaluationRepository.create(db, result)
        except TypeError:
            EvaluationRepository.create(
                db,
                {
                    "candidate_id": request.candidate_id,
                    "job_id": request.job_id,
                    "match_result": match_result,
                    "followup_questions": result.get("followup_questions")
                    if isinstance(result, dict)
                    else getattr(result, "followup_questions", None),
                    "explanation": result.get("explanation")
                    if isinstance(result, dict)
                    else getattr(result, "explanation", None),
                },
            )

        followup_questions = result.get("followup_questions", []) if isinstance(result, dict) else getattr(result, "followup_questions", [])
        explanation = result.get("explanation", "") if isinstance(result, dict) else getattr(result, "explanation", "")

        # Frontend expects:
        # {
        #   match_score: number,
        #   recommendation: string,
        #   match_result: { matched_skills: [], missing_skills: [] }
        # }
        return {
            "match_score": match_result.get("overall_score", score),
            "recommendation": match_result.get("recommendation"),
            "match_result": {
                "matched_skills": match_result.get("matched_skills", []),
                "missing_skills": match_result.get("missing_skills", []),
            },
            # keep existing fields for any other UI pieces
            "overall_score": match_result.get("overall_score", score),
            "interview_ready": match_result.get("interview_ready", False),
            "confidence": match_result.get("confidence", 0),
            "skill_score": match_result.get("skill_score", 0),
            "experience_score": match_result.get("experience_score", 0),
            "education_score": match_result.get("education_score", 0),
            "technology_score": match_result.get("technology_score", 0),
            "evidence": match_result.get("evidence", []),
            "followup_questions": followup_questions,
            "explanation": explanation,
        }


    finally:
        db.close()

