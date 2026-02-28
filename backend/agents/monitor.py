import json
from datetime import datetime
from backend.state import AgentState

def monitor_agent(state: AgentState) -> dict:

    log = {
        "time": str(datetime.now()),
        "query": state["query"],
        "status": state["status"]
    }

    with open("monitor.json", "a") as f:
        f.write(json.dumps(log) + "\n")

    return state