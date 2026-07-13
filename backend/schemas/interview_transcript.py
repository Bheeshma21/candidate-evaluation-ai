from pydantic import BaseModel


class InterviewTranscript(BaseModel):

    transcript: str