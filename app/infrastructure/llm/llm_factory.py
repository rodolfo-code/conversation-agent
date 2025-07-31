
from app.infrastructure.llm.openai_service import OpenAIService
from app.application.interfaces.illm_service import ILLMService


class LLMFactory:
    @staticmethod
    def create_llm_service(llm_provider: str = "openai") -> ILLMService:

        if llm_provider == "openai":
            return OpenAIService()
        else:
            raise ValueError(f"LLM não suportado: {llm_provider}")