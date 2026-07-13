from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from database.database import Base


class Candidate(Base):

    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)

    email = Column(String)

    phone = Column(String)

    skills = Column(Text)

    # NEW
    resume_text = Column(Text)

    profile_json = Column(Text)


class Job(Base):

    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)

    required_skills = Column(Text)

    # NEW
    description = Column(Text)

    job_json = Column(Text)