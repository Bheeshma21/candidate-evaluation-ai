from typing import List, Optional
from pydantic import BaseModel


class Education(BaseModel):
    institution: str
    location: Optional[str] = None
    degree: str
    duration: Optional[str] = None
    percentage: Optional[str] = None
    cgpa: Optional[str] = None


class Experience(BaseModel):
    company: str
    position: str
    duration: Optional[str] = None
    description: Optional[str] = None


class Project(BaseModel):
    name: str
    url: Optional[str] = None
    duration: Optional[str] = None
    description: Optional[str] = None


class Certification(BaseModel):
    name: str
    issuer: Optional[str] = None
    duration: Optional[str] = None


class CandidateProfile(BaseModel):
    name: str
    email: str
    phone: str
    linkedin: Optional[str] = None
    github: Optional[str] = None

    skills: List[str] = []
    technologies: List[str] = []

    education: List[Education] = []
    experience: List[Experience] = []
    projects: List[Project] = []
    certifications: List[Certification] = []

    summary: Optional[str] = None