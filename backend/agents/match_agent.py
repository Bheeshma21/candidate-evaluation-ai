import json

from rag.retriever import Retriever
from agents.base_agent import BaseAgent
from prompts.match_prompt import MATCH_PROMPT


class MatchAgent(BaseAgent):

    def __init__(self):
        super().__init__("Match Agent")
        self.retriever = Retriever()

    async def execute(self, candidate, job):

        query = f"{candidate}\n{job}"

        context = "\n".join(
            self.retriever.retrieve(query)
        )

        prompt = f"""
Relevant Knowledge:
{context}

{MATCH_PROMPT.format(
    candidate=candidate,
    job=job
)}
"""

        response = self.llm.chat(prompt)

        print("\n========== LLM RESPONSE ==========\n")
        print(response)
        print("\n==================================\n")

        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        return json.loads(response)