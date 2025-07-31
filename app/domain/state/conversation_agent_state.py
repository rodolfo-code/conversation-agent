from typing_extensions import TypedDict
from langchain_core.messages import BaseMessage


class ConversationAgentState(TypedDict):
    """State do agente."""
    current_message: str
    messages: list[BaseMessage]
    response: str

