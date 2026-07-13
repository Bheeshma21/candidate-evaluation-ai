from pydantic import BaseModel


class MatchRequest(BaseModel):
    candidate_id: int
    job_id: int