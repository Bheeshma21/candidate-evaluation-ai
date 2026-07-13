from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import DateTime

from datetime import datetime

from database.database import Base


class Interview(Base):

    __tablename__ = "ai_interviews"

    id = Column(Integer, primary_key=True, index=True)

    job_description = Column(Text)

    interview_history = Column(Text)

    final_report = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )