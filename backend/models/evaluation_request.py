from pydantic import BaseModel


class EvaluationRequest(BaseModel):
    resume_text: str
    job_description: str