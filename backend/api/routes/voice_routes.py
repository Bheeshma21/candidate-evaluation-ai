from fastapi import APIRouter
from pydantic import BaseModel
import asyncio

from voice.interview_manager import InterviewManager
from shared.live_state import live_data

router = APIRouter(
    prefix="/voice",
    tags=["Voice"]
)


class VoiceInterviewRequest(BaseModel):
    job_description: str


@router.get("/live")
async def live():

    print("LIVE API:", live_data)

    return live_data


@router.post("/start")
async def start(request: VoiceInterviewRequest):

    live_data["question"] = ""
    live_data["answer"] = ""
    live_data["status"] = "Interview Started"

    manager = InterviewManager()

    asyncio.create_task(
        manager.start(request.job_description)
    )

    return {
        "status": "started"
    }