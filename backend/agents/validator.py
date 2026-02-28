from backend.state import AgentState

def validator_agent(state: AgentState) -> dict:
    query = state["query"].strip().lower()

    if len(query) < 3:
        return {"response": "Invalid query", "status": "STOP"}

    smalltalk = ["hi", "hello", "ok", "thanks"]

    if query in smalltalk:
        return {
            "response": "Please ask a valid business question.",
            "status": "STOP"
        }

    return {"status": "VALID"}