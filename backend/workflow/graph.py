from langgraph.graph import StateGraph
from backend.workflow.nodes import retrieve_node, generate_node
from backend.workflow.router import route_decision
from backend.hitl.escalation import human_escalation
from backend.workflow.state import GraphState


def build_graph():

    workflow = StateGraph(GraphState)

    workflow.add_node("retrieve", retrieve_node)
    workflow.add_node("generate", generate_node)
    workflow.add_node("human", human_escalation)

    workflow.set_entry_point("retrieve")

    workflow.add_edge("retrieve", "generate")

    workflow.add_conditional_edges(
        "generate",
        route_decision,
        {
            "human": "human",
            "output": "__end__"
        }
    )

    workflow.add_edge("human", "__end__")

    return workflow.compile()