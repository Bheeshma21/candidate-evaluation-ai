from database.database import SessionLocal

from repositories.candidate_repository import CandidateRepository
from repositories.job_repository import JobRepository

from agents.match_agent import MatchAgent


class RecruitmentOrchestrator:

    def __init__(self):

        self.db = SessionLocal()

        self.match_agent = MatchAgent()

    async def run(
        self,
        candidate_id: int,
        job_id: int
    ):

        candidate = CandidateRepository.get_by_id(
            self.db,
            candidate_id
        )

        if not candidate:
            raise Exception("Candidate not found")

        job = JobRepository.get_by_id(
            self.db,
            job_id
        )

        if not job:
            raise Exception("Job not found")

        match_result = await self.match_agent.execute(
            candidate.profile_json,
            job.job_json
        )

        return {
            "candidate": candidate.name,
            "job": job.title,
            "match_result": match_result
        }