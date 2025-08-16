import logging
from langgraph.graph import StateGraph, START, END
from app.application.agent.conversation_agent.node_functions.services_node.services_node import services_node
from app.application.agent.conversation_agent.node_functions.how_it_works_node.how_it_works_node import how_it_works_node
from app.domain.state.conversation_agent_state import ConversationAgentState
from app.application.agent.conversation_agent.node_functions.gateway_node.gateway_node import gateway_node

logger = logging.getLogger(__name__)

def decision_router(state: ConversationAgentState) -> str:
    """Decision router function."""
    next_step = state.get("next_step")

    if not next_step:
        return "UNDEFINED"

    return next_step

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
        self.workflow.add_node("SERVICES_NODE", services_node)
        self.workflow.add_node("HOW_IT_WORKS_NODE", how_it_works_node)

        self.workflow.set_entry_point("GATEWAY_NODE")

        self.workflow.add_edge(START, "GATEWAY_NODE")
        self.workflow.add_conditional_edges(
            "GATEWAY_NODE", 
            decision_router, 
            {
                "SERVICES_NODE": "SERVICES_NODE",
                "HOW_IT_WORKS_NODE": "HOW_IT_WORKS_NODE",
                "UNDEFINED": END
            }
        )

        self.workflow.add_edge("SERVICES_NODE", END)
        self.workflow.add_edge("HOW_IT_WORKS_NODE", END)

    
    def _compile_agent(self):
        return self.workflow.compile()

    def build_agent(self):
        print(self._build_agent.get_graph().draw_mermaid())
        return self._build_agent
    
def get_conversation_agent():
    builder = ConversationAgentBuilder()
    agent = builder.build_agent()
    return agent