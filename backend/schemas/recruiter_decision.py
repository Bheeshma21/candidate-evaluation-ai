from pydantic import BaseModel


class RecruiterDecision(BaseModel):

    decision: str

    notes: str = ""