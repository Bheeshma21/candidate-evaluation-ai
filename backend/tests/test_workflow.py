import asyncio
import json

from workflow.recruitment_workflow import RecruitmentWorkflow
from parsers.resume_parser import ResumeParser


async def main():

    workflow = RecruitmentWorkflow()

    resume_text = ResumeParser.extract_text(
        r"C:\Users\Bheeshma\Downloads\Bheeshma_Data_Scientist_2025.pdf"
    )

    with open(
        "uploads/jobs/Job Title AI Engineer.txt",
        "r",
        encoding="utf-8"
    ) as f:
        job_text = f.read()

    result = await workflow.run(
        resume_text,
        job_text
    )

    print(json.dumps(result, indent=4))


asyncio.run(main())