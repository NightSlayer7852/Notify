from langgraph.graph import StateGraph
from state import GraphState

from agents.planner import planner_node
from agents.researcher import researcher_node
from agents.writer import writer_node
from agents.summarizer import summarizer_node
from agents.critic import critic_node
from agents.refine import refine_node

def build_graph():
    builder = StateGraph(GraphState)

    # Add nodes
    builder.add_node("planner", planner_node)
    builder.add_node("researcher", researcher_node)
    builder.add_node("writer", writer_node)
    builder.add_node("critic", critic_node)
    builder.add_node("refine", refine_node)
    builder.add_node("summarizer", summarizer_node)

    # Define flow
    builder.set_entry_point("planner")

    builder.add_edge("planner", "researcher")
    builder.add_edge("researcher", "writer")
    builder.add_edge("writer", "critic")
    builder.add_edge("critic", "refine")
    builder.add_edge("refine", "summarizer")

    return builder.compile()