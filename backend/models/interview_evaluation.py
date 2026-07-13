from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import JSON
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from database.database import Base


class InterviewEvaluation(Base):

    __tablename__ = "interview_evaluations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    interview_id = Column(
        Integer,
        nullable=False
    )

    technical_score = Column(Float)

    communication_score = Column(Float)

    problem_solving_score = Column(Float)

    confidence_score = Column(Float)

    final_score = Column(Float)

    recommendation = Column(String)

    strengths = Column(JSON)

    weaknesses = Column(JSON)

    summary = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )