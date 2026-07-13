from agents.resume_agent import ResumeAgent
from agents.job_agent import JobAgent
from agents.match_agent import MatchAgent
from agents.explainability_agent import ExplainabilityAgent
from agents.followup_agent import FollowUpAgent


class RecruitmentWorkflow:

    def __init__(self):

        self.resume_agent = ResumeAgent()
        self.job_agent = JobAgent()
        self.match_agent = MatchAgent()
        self.explainability_agent = ExplainabilityAgent()
        self.followup_agent = FollowUpAgent()

    async def run(
        self,
        resume_text: str,
        job_text: str
    ):

        candidate = await self.resume_agent.execute(resume_text)

        job = await self.job_agent.execute(job_text)

        match = await self.match_agent.execute(
            candidate,
            job
        )

        explanation = await self.explainability_agent.execute(
            match
        )

        questions = await self.followup_agent.execute(
            explanation
        )

        return {
            "candidate": candidate,
            "job": job,
            "match": match,
            "explanation": explanation,
            "followup_questions": questions
        }