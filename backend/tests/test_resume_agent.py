import asyncio
import json

from parsers.resume_parser import ResumeParser
from agents.resume_agent import ResumeAgent


resume_text = ResumeParser.extract_text(
    r"C:\Users\Bheeshma\Downloads\Bheeshma_Data_Scientist_2025.pdf"
)


async def main():

    agent = ResumeAgent()

    result = await agent.execute(resume_text)

    print(json.dumps(result, indent=4))


asyncio.run(main())