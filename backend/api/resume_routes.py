import os
import shutil
from fastapi import Depends
from sqlalchemy.orm import Session

from database.database import get_db
from repositories.candidate_repository import CandidateRepository

from fastapi import APIRouter, UploadFile, File

from parsers.resume_parser import ResumeParser
from agents.resume_agent import ResumeAgent
from models.candidate_profile import CandidateProfile

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    os.makedirs("uploads/resumes", exist_ok=True)

    file_path = f"uploads/resumes/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = ResumeParser.extract_text(file_path)

    agent = ResumeAgent()

    result = await agent.execute(resume_text)

    profile = CandidateProfile(**result)
    candidate = CandidateRepository.save(
        db,
        profile
    )
    return {
        "candidate_id": candidate.id,
        "name": candidate.name,
        "status": "saved"
    }