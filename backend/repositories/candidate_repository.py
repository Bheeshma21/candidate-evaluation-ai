import json

from sqlalchemy.orm import Session

from database.models import Candidate
from models.candidate_profile import CandidateProfile


class CandidateRepository:

    @staticmethod
    def save(
        db: Session,
        profile: CandidateProfile
    ):

        candidate = Candidate(
            name=profile.name,
            email=profile.email,
            phone=profile.phone,
            skills=json.dumps(profile.skills),
        # temporary until upload endpoint provides full resume
            resume_text=profile.model_dump_json(),

            profile_json=profile.model_dump_json()
    )

        db.add(candidate)
        db.commit()
        db.refresh(candidate)

        return candidate

    @staticmethod
    def get_by_id(
        db: Session,
        candidate_id: int
    ):

        return (
            db.query(Candidate)
            .filter(Candidate.id == candidate_id)
            .first()
        )