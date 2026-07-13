from pydantic import BaseModel


class InterviewFeedback(BaseModel):

    interview_notes: str