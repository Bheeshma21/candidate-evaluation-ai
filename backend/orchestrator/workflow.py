from agents.resume_agent import ResumeAgent
from agents.job_agent import JobAgent
from services.matching_service import MatchingService


class RecruitmentWorkflow:

    def __init__(self):

        self.resume_agent = ResumeAgent()

        self.job_agent = JobAgent()

        self.matching_service = MatchingService()