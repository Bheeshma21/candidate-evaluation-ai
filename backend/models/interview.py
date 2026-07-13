from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from database.database import Base


class Interview(Base):

    __tablename__ = "interviews"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    evaluation_id = Column(Integer)

    candidate_name = Column(String)

    email = Column(String)

    interview_date = Column(String)

    interview_time = Column(String)

    interviewer = Column(String)

    meeting_link = Column(String)

    status = Column(
        String,
        default="Scheduled"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )