import json

from rag.retriever import Retriever
from agents.base_agent import BaseAgent
from prompts.job_prompt import JOB_EXTRACTION_PROMPT


class JobAgent(BaseAgent):

    def __init__(self):
        super().__init__("Job Agent")
        self.retriever = Retriever()

    async def execute(self, job_description: str):

        context = "\n".join(
            self.retriever.retrieve(job_description)
        )

        prompt = f"""
Relevant Knowledge:
{context}

{JOB_EXTRACTION_PROMPT.format(
    job_description=job_description
)}
"""

        response = self.llm.chat(prompt)

        return json.loads(response)