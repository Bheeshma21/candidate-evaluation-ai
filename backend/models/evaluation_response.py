from typing import Any, Dict, List
from pydantic import BaseModel


class EvaluationResponse(BaseModel):

    match_score: float

    confidence_score: float

    recommendation: str

    candidate_profile: Dict[str, Any]

    job_profile: Dict[str, Any]

    match_result: Dict[str, Any]

    explanation: Dict[str, Any]

    followup_questions: List[Dict[str, Any]]