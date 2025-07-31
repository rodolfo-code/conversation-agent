from typing import Dict, Any
from app.domain.state.conversation_agent_state import ConversationAgentState
from app.infrastructure.llm.llm_factory import LLMFactory
from langchain_core.messages import AIMessage

def gateway_node(state: ConversationAgentState) -> Dict[str, Any]:
    """Gateway node that processes the input message."""

    llm_service = LLMFactory.create_llm_service("openai")
    llm_response = llm_service.conversation(state['messages'])

    updated_messages = state['messages'] + [AIMessage(content=llm_response)]

    
    return {
        **state,
        "messages": updated_messages,
        "response": llm_response,
    } 