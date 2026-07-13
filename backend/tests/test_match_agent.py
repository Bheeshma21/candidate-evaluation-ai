import asyncio

from database.database import SessionLocal
from repositories.candidate_repository import CandidateRepository
from repositories.job_repository import JobRepository
from agents.match_agent import MatchAgent


async def main():

    db = SessionLocal()

    candidate = CandidateRepository.get_by_id(db, 1)

    job = JobRepository.get_by_id(db, 1)

    agent = MatchAgent()

    result = await agent.execute(
        candidate.profile_json,
        job.job_json
    )

    print(result)

    db.close()


asyncio.run(main())