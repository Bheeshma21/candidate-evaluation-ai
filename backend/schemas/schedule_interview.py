from pydantic import BaseModel


class ScheduleInterview(BaseModel):

    interview_date: str

    interview_time: str

    interviewer: str

    meeting_link: str