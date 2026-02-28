from langgraph.graph import StateGraph, END
from backend.state import AgentState

from backend.agents.validator import validator_agent
from backend.agents.safety import safety_agent
from backend.agents.compliance import compliance_agent
from backend.agents.llm import llm_agent
from backend.agents.monitor import monitor_agent


def route(state):
    return state["status"]


workflow = StateGraph(AgentState)

workflow.add_node("validator", validator_agent)
workflow.add_node("safety", safety_agent)
workflow.add_node("compliance", compliance_agent)
workflow.add_node("llm", llm_agent)
workflow.add_node("monitor", monitor_agent)

workflow.set_entry_point("validator")

workflow.add_conditional_edges(
    "validator",
    route,
    {"STOP": END, "VALID": "safety"}
)

workflow.add_conditional_edges(
    "safety",
    route,
    {"STOP": END, "SAFE": "compliance"}
)

workflow.add_conditional_edges(
    "compliance",
    route,
    {"STOP": END, "COMPLIANT": "llm"}
)

workflow.add_edge("llm", "monitor")
workflow.add_edge("monitor", END)

app = workflow.compile()