from fastapi import APIRouter
from pydantic import BaseModel

from services.email_service import EmailService

router = APIRouter()


class InterviewRequest(BaseModel):
    email: str
    candidate_name: str
    interview_date: str
    interview_time: str
    interviewer: str
    meeting_link: str


@router.post("/interview/send")
async def interview_send(request: InterviewRequest):

    EmailService.send_interview_email(
        request.email,
        request.candidate_name,
        request.interview_date,
        request.interview_time,
        request.interviewer,
        request.meeting_link
    )

    return {
        "message": "Interview invitation sent successfully."
    }