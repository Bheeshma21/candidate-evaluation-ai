from pydantic import BaseModel


class MatchResult(BaseModel):

    overall_score: float

    recommendation: str

    interview_ready: bool

    confidence: float

    skill_score: float

    experience_score: float

    education_score: float

    technology_score: float

    matched_skills: list[str]

    missing_skills: list[str]

    evidence: list[str]