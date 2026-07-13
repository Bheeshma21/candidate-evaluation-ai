from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database.database import get_db

from agents.job_agent import JobAgent
from models.job_profile import JobProfile
from repositories.job_repository import JobRepository


router = APIRouter(
    prefix="/job",
    tags=["Job"]
)


class JobRequest(BaseModel):
    job_description: str


@router.post("/create")
async def create_job(
    request: JobRequest,
    db: Session = Depends(get_db)
):

    agent = JobAgent()

    result = await agent.execute(
        request.job_description
    )

    profile = JobProfile(**result)

    job = JobRepository.save(
        db,
        profile
    )

    return {
        "job_id": job.id,
        "title": job.title,
        "status": "saved"
    }