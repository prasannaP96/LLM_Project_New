from backend.state import AgentState

def safety_agent(state: AgentState) -> dict:

    blocked = ["hack", "attack", "delete database"]

    if any(w in state["query"].lower() for w in blocked):
        return {
            "response": "Unsafe request blocked",
            "status": "STOP"
        }

    return {"status": "SAFE"}