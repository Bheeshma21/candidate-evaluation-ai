import json

from sqlalchemy.orm import Session

from database.models import Job
from models.job_profile import JobProfile


class JobRepository:

    @staticmethod
    def save(
        db: Session,
        profile: JobProfile
    ):

        job = Job(
            title=profile.title,
            required_skills=json.dumps(profile.required_skills),
            description=profile.model_dump_json(),
            job_json=profile.model_dump_json()
        )

        db.add(job)
        db.commit()
        db.refresh(job)

        return job

    @staticmethod
    def get_by_id(
        db: Session,
        job_id: int
    ):

        return (
            db.query(Job)
            .filter(Job.id == job_id)
            .first()
        )