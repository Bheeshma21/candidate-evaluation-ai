from fastapi import APIRouter
from pydantic import BaseModel

from services.email_service import EmailService

router = APIRouter()


class EmailRequest(BaseModel):
    email: str
    candidate_name: str
    score: float


@router.post("/email/send")

async def send_email(request: EmailRequest):

    EmailService.send_shortlisted_email(
        request.email,
        request.candidate_name,
        request.score
    )

    return {
        "message": "Email sent successfully"
    }