from typing import Any, Dict, Optional

import logging

from langchain_core.messages import HumanMessage, AIMessage

from app.application.agent.conversation_agent.agent_builder.conversation_agent_builder import ConversationAgentBuilder
from app.domain.input.input_message import InputMessage
from app.domain.state.conversation_agent_state import ConversationAgentState

logger = logging.getLogger(__name__)


class ConversationAgentService:
    """Service for conversation_agent processing."""
    
    def __init__(self):
        """Initialize the agent service."""
        self.agent_builder = ConversationAgentBuilder()
        self.config = self.agent_builder.build_agent()
        
        logger.info(
            "conversation_agent service initialized",
            extra={"config": self.config}
        )

    async def process(self, input_message: InputMessage):
        """Process the request."""

        initial_state = ConversationAgentState(
            current_message=input_message.message,
            messages=[HumanMessage(content=input_message.message)]
        )

        final_state = self.config.invoke(initial_state)

        response = {
            "response": final_state.get("response", "No response generated"),
            "message": final_state.get("current_message", input_message.message)
        }

        logger.info("Conversation agent response", extra={"response": response})

        return response