from typing import Dict, Any
from app.domain.state.conversation_agent_state import ConversationAgentState
from app.infrastructure.llm.llm_factory import LLMFactory
from langchain_core.messages import AIMessage


def how_it_works_node(state: ConversationAgentState) -> Dict[str, Any]:
    """
        Recebe input do supervisor e retorna informaçoes de como funciona o serviço.
    """

    llm_service = LLMFactory.create_llm_service("openai")
    how_the_clean_works_content = llm_service.clean_works()

    updated_messages = state['messages'] + [AIMessage(content=how_the_clean_works_content)]

    return {
        **state,
        "messages": updated_messages,
        "used_nodes": state["used_nodes"] + ["HOW_IT_WORKS_NODE"],
        "response": how_the_clean_works_content,
    }