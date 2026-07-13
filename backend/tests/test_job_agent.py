import asyncio

from parsers.job_parser import JobParser
from agents.job_agent import JobAgent


async def main():

    job_text = JobParser.extract_text(
        "uploads/jobs/ai_engineer.txt"
    )

    agent = JobAgent()

    result = await agent.execute(job_text)

    print(result)


asyncio.run(main())