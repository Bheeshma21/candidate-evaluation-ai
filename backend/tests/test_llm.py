from services.llm_service import LLMService

llm = LLMService()

response = llm.chat(
    "Say Hello in one sentence."
)

print(response)