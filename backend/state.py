from typing import TypedDict, Optional

class AgentState(TypedDict):
    query: str
    response: Optional[str]
    status: Optional[str]