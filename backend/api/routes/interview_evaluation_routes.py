from fastapi import APIRouter
from fastapi import HTTPException

from database.database import SessionLocal

from repositories.interview_repository import InterviewRepository
from repositories.interview_evaluation_repository import (
    InterviewEvaluationRepository,
)

from schemas.interview_transcript import InterviewTranscript

from services.interview_evaluator_service import (
    InterviewEvaluatorService,
)

router = APIRouter(
    prefix="/interview-evaluation",
    tags=["Interview Evaluation AI"]
)


@router.post("/{interview_id}")
def evaluate_interview(
    interview_id: int,
    request: InterviewTranscript
):

    db = SessionLocal()

    try:

        interview = InterviewRepository.get_by_id(
            db,
            interview_id
        )

        if interview is None:

            raise HTTPException(
                status_code=404,
                detail="Interview not found"
            )

        result = InterviewEvaluatorService.evaluate(
            request.transcript
        )

        interview_evaluation = (
            InterviewEvaluationRepository.create(
                db=db,
                interview_id=interview.id,
                evaluation=result
            )
        )

        return interview_evaluation

    finally:

        db.close()