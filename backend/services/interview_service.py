import json

from database.database import SessionLocal

from models.interview_model import Interview


class InterviewService:

    def save(
        self,
        job_description,
        history,
        report
    ):

        db = SessionLocal()

        interview = Interview(
            job_description=job_description,
            interview_history=json.dumps(history),
            final_report=json.dumps(report)
        )

        db.add(interview)

        db.commit()

        db.refresh(interview)

        db.close()

        return interview.id