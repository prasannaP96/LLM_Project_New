from backend.state import AgentState

def compliance_agent(state: AgentState) -> dict:

    sensitive = ["password", "credit card"]

    if any(w in state["query"].lower() for w in sensitive):
        return {
            "response": "Compliance violation",
            "status": "STOP"
        }

    return {"status": "COMPLIANT"}