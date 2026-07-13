import json

from rag.retriever import Retriever
from agents.base_agent import BaseAgent


class FollowUpAgent(BaseAgent):

    def __init__(self):
        super().__init__("Follow-Up Agent")
        self.retriever = Retriever()

    async def execute(self, explainability_result):

        context = "\n".join(
            self.retriever.retrieve(str(explainability_result))
        )

        prompt = f"""
You are a Senior Technical Interviewer.

Relevant Knowledge:
{context}

Based on the candidate weaknesses below, generate interview questions.

Weaknesses:
{explainability_result}

Return ONLY valid JSON.

{{
    "questions":[
        {{
            "skill":"",
            "difficulty":"",
            "question":"",
            "expected_answer":""
        }}
    ]
}}
"""

        response = self.llm.chat(prompt)

        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        return json.loads(response)