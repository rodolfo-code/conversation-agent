import logging
from langgraph.graph import StateGraph, START, END
from app.domain.state.conversation_agent_state import ConversationAgentState
from app.application.agent.conversation_agent.node_functions.gateway_node.gateway_node import gateway_node

logger = logging.getLogger(__name__)


class ConversationAgentBuilder:
    """Builder for conversation_agent using LangGraph."""
    
    def __init__(self):
        """Initialize the agent builder."""
        self.workflow = StateGraph(ConversationAgentState)
        self._build_graph()
        self._build_agent = self._compile_agent()

    
    def _build_graph(self):
        """Build the workflow graph."""

        self.workflow.add_node("GATEWAY_NODE", gateway_node)

        self.workflow.set_entry_point("GATEWAY_NODE")

        self.workflow.add_edge(START, "GATEWAY_NODE")
        self.workflow.add_edge("GATEWAY_NODE", END)


    
    def _compile_agent(self):
        return self.workflow.compile()

    def build_agent(self):
        print(self._build_agent.get_graph().draw_mermaid())
        return self._build_agent
    
def get_conversation_agent():
    builder = ConversationAgentBuilder()
    agent = builder.build_agent()
    return agent