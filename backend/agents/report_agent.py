import json

from services.llm_service import LLMService


class ReportAgent:

    def __init__(self):
        self.llm = LLMService()

    async def generate(self, history):

        prompt = f"""
You are an Expert Technical Hiring Manager.

Below is the complete interview history.

{history}

Generate a final interview report.

Return ONLY valid JSON.

{{
    "overall_score": 0,
    "technical_rating": "",
    "communication_rating": "",
    "strengths": [],
    "weaknesses": [],
    "recommendation": "",
    "learning_roadmap": [],
    "final_feedback": ""
}}
"""

        response = self.llm.chat(prompt)

        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        return json.loads(response)