from sqlalchemy import Column, Integer, Float, String, JSON, DateTime
from sqlalchemy.sql import func

from database.database import Base


class Evaluation(Base):

    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True, index=True)

    candidate_name = Column(String, nullable=False)
    job_title = Column(String, nullable=False)

    match_score = Column(Float)
    confidence_score = Column(Float)

    recommendation = Column(String)

    # NEW
    recruiter_decision = Column(String)

    # NEW
    recruiter_notes = Column(String)

    candidate_profile = Column(JSON)
    job_profile = Column(JSON)

    match_result = Column(JSON)
    explanation = Column(JSON)

    followup_questions = Column(JSON)

    audit_log = Column(JSON)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )