import json

from rag.retriever import Retriever
from agents.base_agent import BaseAgent


class ExplainabilityAgent(BaseAgent):

    def __init__(self):
        super().__init__("Explainability Agent")
        self.retriever = Retriever()

    async def execute(self, match_result):

        context = "\n".join(
            self.retriever.retrieve(str(match_result))
        )

        prompt = f"""
You are an expert AI Hiring Manager.

Relevant Knowledge:
{context}

Analyze the following candidate match result.

Match Result:
{match_result}

Return ONLY valid JSON.

{{
    "decision": "",
    "confidence": 0,
    "strengths": [],
    "weaknesses": [],
    "risks": [],
    "final_summary": "",
    "next_round": ""
}}
"""

        response = self.llm.chat(prompt)

        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        return json.loads(response)