from parsers.resume_parser import ResumeParser
from agents.resume_agent import ResumeAgent
from models.candidate_profile import CandidateProfile

import asyncio


async def main():

    resume_text = ResumeParser.extract_text(
        r"C:\Users\Bheeshma\Downloads\Bheeshma_Data_Scientist_2025.pdf"
    )

    agent = ResumeAgent()

    result = await agent.execute(resume_text)

    profile = CandidateProfile(**result)

    print(profile)

    print("\nCandidate Name:", profile.name)
    print("Email:", profile.email)
    print("Total Skills:", len(profile.skills))


asyncio.run(main())