from fastapi import APIRouter, HTTPException, Request, Depends
import logging
from fastapi.responses import JSONResponse
from app.domain.input.input_message import InputMessage
from app.application.services.conversation_agent_service import ConversationAgentService

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/gateway")
async def process(request: InputMessage, conversation_agent_service: ConversationAgentService = Depends(ConversationAgentService)):
    """Process content."""
    logger.info("Processing content", extra={"request": request})

    try:
        response = await conversation_agent_service.process(request)

        

        return JSONResponse(content=response)
    except Exception as e:
        logger.error(f"Error processing content: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

    