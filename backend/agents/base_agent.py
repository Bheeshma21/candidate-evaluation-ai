from abc import ABC, abstractmethod
from typing import Any

from services.llm_service import LLMService


class BaseAgent(ABC):

    def __init__(self, name: str):
        self.name = name
        self.llm = LLMService()

    @abstractmethod
    async def execute(self, data: Any):
        pass