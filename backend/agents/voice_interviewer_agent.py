from services.llm_service import LLMService
from rag.retriever import Retriever


class VoiceInterviewerAgent:

    def __init__(self):
        self.llm = LLMService()
        self.retriever = Retriever()

    async def ask_question(
        self,
        job_description: str,
        history: list
    ):

        history_text = ""

        for item in history:
            history_text += f"""
Question: {item['question']}
Answer: {item['answer']}
Score: {item['evaluation']['score']}
Feedback: {item['evaluation']['feedback']}

"""

        retrieval_query = f"""
Job Description:
{job_description}

Interview History:
{history_text}
"""

        context = "\n".join(
            self.retriever.retrieve(retrieval_query)
        )

        prompt = f"""
You are a Senior Technical Interviewer.

Retrieved Knowledge:
{context}

Job Description:
{job_description}

Previous Interview:
{history_text}

Rules:
- Ask exactly ONE new interview question.
- Do NOT repeat previous questions.
- If the previous answer scored low, ask an easier follow-up.
- If the previous answer scored high, increase the difficulty.
- Base the question on the retrieved knowledge.
- Return ONLY the interview question.
"""

        return self.llm.chat(prompt).strip()