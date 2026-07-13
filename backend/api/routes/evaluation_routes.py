from fastapi import APIRouter, HTTPException

from database.database import SessionLocal

from repositories.evaluation_repository import EvaluationRepository

from schemas.recruiter_decision import RecruiterDecision


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/evaluations")
def get_evaluations():

    db = SessionLocal()

    try:

        return EvaluationRepository.get_all(db)

    finally:

        db.close()


@router.get("/evaluations/{evaluation_id}")
def get_evaluation(evaluation_id: int):

    db = SessionLocal()

    try:

        evaluation = EvaluationRepository.get_by_id(
            db,
            evaluation_id
        )

        if evaluation is None:

            raise HTTPException(
                status_code=404,
                detail="Evaluation not found"
            )

        return evaluation

    finally:

        db.close()


@router.post("/evaluations/{evaluation_id}/decision")
def recruiter_decision(
    evaluation_id: int,
    request: RecruiterDecision
):

    db = SessionLocal()

    try:

        evaluation = EvaluationRepository.update_decision(
            db,
            evaluation_id,
            request.decision,
            request.notes
        )

        if evaluation is None:

            raise HTTPException(
                status_code=404,
                detail="Evaluation not found"
            )

        return {
            "message": "Recruiter decision saved successfully",
            "evaluation": evaluation
        }

    finally:

        db.close()


@router.delete("/evaluations/{evaluation_id}")
def delete_evaluation(evaluation_id: int):

    db = SessionLocal()

    try:

        evaluation = EvaluationRepository.delete(
            db,
            evaluation_id
        )

        if evaluation is None:

            raise HTTPException(
                status_code=404,
                detail="Evaluation not found"
            )

        return {
            "message": "Evaluation deleted successfully"
        }

    finally:

        db.close()