from typing import Dict, Any
from app.domain.state.conversation_agent_state import ConversationAgentState
from app.infrastructure.llm.llm_factory import LLMFactory
from langchain_core.messages import AIMessage

def services_node(state: ConversationAgentState) -> Dict[str, Any]:
    """Services node that processes the input message."""

    llm_service = LLMFactory.create_llm_service("openai")
    llm_response = llm_service.services_info(state['messages'])

    updated_messages = state['messages'] + [AIMessage(content=llm_response)]

    
    return {
        **state,
        "messages": updated_messages,
        "used_nodes": state["used_nodes"] + ["SERVICES_NODE"],
        "response": llm_response,
    } 