from abc import ABC, abstractmethod
from typing import List

class ILLMService(ABC):
    @abstractmethod
    def services_info(self, messages: List[str]) -> str:
        pass

    @abstractmethod
    def decide_next_node(self, messages: List[str]) -> str:
        pass
    
    @abstractmethod
    def clean_works(self) -> str:
        pass