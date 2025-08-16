"""
Configuration settings for conversation-agent.
"""

import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

# CONFIGURA LANGCHAIN TRACING V2 CORRETAMENTE
# Para desabilitar LangSmith, configuramos V2 como false
os.environ["LANGCHAIN_TRACING_V2"] = "false"


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    OPENAI_MODEL_NAME: str = "gpt-4o-mini"  
    OPENAI_TEMPERATURE: float = 0.2
    
    # LangSmith configurações - CONFIGURADO CORRETAMENTE
    LANGCHAIN_TRACING_V2: bool = False  # Desabilita LangSmith por padrão
    LANGCHAIN_ENDPOINT: str = "https://api.smith.langchain.com"
    LANGCHAIN_API_KEY: str = ""  # Opcional, só necessário se LANGCHAIN_TRACING_V2=True
    
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Configura corretamente o LangChain Tracing V2
        self._configure_langchain_tracing()
    
    def _configure_langchain_tracing(self):
        """Configura corretamente o LangChain Tracing V2"""
        # Sempre configura V2 como false para desabilitar LangSmith
        os.environ["LANGCHAIN_TRACING_V2"] = "false"


settings = Settings()


if __name__ == "__main__":
    print("Configurações carregadas:")
    print(f"OPENAI_MODEL: {settings.OPENAI_MODEL_NAME}")
    print(f"LANGCHAIN_TRACING_V2: {settings.LANGCHAIN_TRACING_V2}")
    if settings.LANGCHAIN_TRACING_V2:
        print("LangSmith HABILITADO com tracing V2")
    else:
        print("LangSmith DESABILITADO - tracing V2 configurado corretamente") 