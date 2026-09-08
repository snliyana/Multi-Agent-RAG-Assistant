from typing import TypedDict, List


class AgentState(TypedDict):

    query: str
    next_agent: str
    results: List[str]
    final_answer: str
    chat_history: List[dict]