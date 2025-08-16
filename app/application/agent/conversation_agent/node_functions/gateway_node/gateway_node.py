from typing import Dict, Any
from app.domain.state.conversation_agent_state import ConversationAgentState
from app.infrastructure.llm.llm_factory import LLMFactory
from langchain_core.messages import AIMessage

def gateway_node(state: ConversationAgentState) -> Dict[str, Any]:
    """Gateway node that processes the input message."""

    llm_service = LLMFactory.create_llm_service("openai")
    next_step = llm_service.decide_next_node(state['current_message'])

    updated_messages = state['messages'] + [AIMessage(content=next_step)]

    print(f"Next step: {next_step}")
    
    return {
        **state,
        "messages": updated_messages,
        "used_nodes": ["GATEWAY_NODE"],
        "next_step": next_step,
    } 