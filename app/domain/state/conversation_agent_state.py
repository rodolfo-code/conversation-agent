from typing_extensions import Literal, TypedDict
from langchain_core.messages import BaseMessage


class ConversationAgentState(TypedDict):
    """State do agente."""
    current_message: str
    messages: list[BaseMessage]
    response: str
    used_nodes: list[Literal["GATEWAY_NODE", "SERVICES_NODE", "HOW_IT_WORKS_NODE", "UNDEFINED"]]
    next_step: Literal["SERVICES_NODE", "HOW_IT_WORKS_NODE", "UNDEFINED"]
