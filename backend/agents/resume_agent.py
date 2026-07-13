import json

from rag.retriever import Retriever
from agents.base_agent import BaseAgent
from prompts.resume_prompt import RESUME_EXTRACTION_PROMPT


class ResumeAgent(BaseAgent):

    def __init__(self):
        super().__init__("Resume Agent")
        self.retriever = Retriever()

    async def execute(self, resume_text: str):

        context = "\n".join(
            self.retriever.retrieve(resume_text)
        )

        prompt = f"""
Relevant Knowledge:
{context}

{RESUME_EXTRACTION_PROMPT.format(
    resume=resume_text
)}
"""

        response = self.llm.chat(prompt)

        return json.loads(response)