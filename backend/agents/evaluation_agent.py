import json

from services.llm_service import LLMService
from rag.retriever import Retriever


class EvaluationAgent:

    def __init__(self):
        self.llm = LLMService()
        self.retriever = Retriever()

    async def evaluate(
        self,
        question: str,
        answer: str
    ):

        context = "\n".join(
            self.retriever.retrieve(question)
        )

        prompt = f"""
You are a Senior Technical Interviewer.

Use ONLY the retrieved knowledge to evaluate the candidate.

Retrieved Knowledge:
{context}

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer.

Return ONLY valid JSON.

{{
    "score": 0,
    "verdict": "",
    "strengths": [],
    "weaknesses": [],
    "correct_answer": "",
    "feedback": ""
}}
"""

        response = self.llm.chat(prompt)

        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        return json.loads(response)