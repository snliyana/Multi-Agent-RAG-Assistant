from typing import Dict, List


conversation_memory: Dict[str, List[dict]] = {}


def get_chat_history(session_id: str) -> List[dict]:
    return conversation_memory.get(session_id, [])


def save_message(
    session_id: str,
    role: str,
    content: str
) -> None:

    if session_id not in conversation_memory:
        conversation_memory[session_id] = []

    conversation_memory[session_id].append(
        {
            "role": role,
            "content": content
        }
    )


def clear_chat_history(session_id: str) -> None:
    conversation_memory[session_id] = []