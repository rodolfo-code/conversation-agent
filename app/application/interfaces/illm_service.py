from abc import ABC, abstractmethod
from typing import List

class ILLMService(ABC):
    @abstractmethod
    def conversation(self, messages: List[str]) -> str:
        pass