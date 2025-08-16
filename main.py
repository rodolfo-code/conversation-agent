# CONFIGURA LANGCHAIN TRACING V2 ANTES DE QUALQUER IMPORTAÇÃO
import os
os.environ["LANGCHAIN_TRACING_V2"] = "false"

# Carrega configurações ANTES de qualquer importação do LangChain
from app.infrastructure.config.config import settings

from fastapi import FastAPI
from app.presentation.conversation_agent_router import router as conversation_agent_router


app = FastAPI(title="conversation-agent")

app.include_router(conversation_agent_router, prefix="/api")


@app.get("/health")
async def health():
    """Health check."""
    return {
        "status": "ok",
        "title": "conversation-agent",
        "langsmith_disabled": not settings.LANGCHAIN_TRACING_V2,
        "version": "1.2.0"
        }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 