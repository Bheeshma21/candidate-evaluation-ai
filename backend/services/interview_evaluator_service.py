import json

from services.llm_service import LLMService

from prompts.interview_evaluator_prompt import (
    INTERVIEW_EVALUATOR_PROMPT
)


class InterviewEvaluatorService:

    @staticmethod
    def evaluate(transcript: str):

        llm = LLMService()

        prompt = INTERVIEW_EVALUATOR_PROMPT.format(
            transcript=transcript
        )

        response = llm.chat(prompt)

        print("\n========== INTERVIEW AI ==========\n")
        print(response)
        print("\n=================================\n")

        response = response.strip()
        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()
        print("\n========== CLEAN JSON ==========\n")
        print(response)
        print("\n===============================\n")
        return json.loads(response)