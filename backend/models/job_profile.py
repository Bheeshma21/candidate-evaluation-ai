from typing import List, Optional
from pydantic import BaseModel


class JobProfile(BaseModel):
    title: str

    required_skills: List[str] = []
    preferred_skills: List[str] = []

    experience: Optional[str] = None

    education: Optional[str] = None

    responsibilities: List[str] = []

    technologies: List[str] = []

    certifications: List[str] = []

    summary: Optional[str] = None