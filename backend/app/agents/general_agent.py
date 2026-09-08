from langchain_groq import ChatGroq


llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.3
)


def run_general_agent(
    query: str,
    chat_history: list
) -> str:

    messages = [
        {
            "role": "system",
            "content": """
You are a helpful general AI assistant.

Use the conversation history when it is relevant to the
user's current question.

Do not invent information that is not present in the
conversation history.
"""
        }
    ]

    messages.extend(chat_history)

    messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    response = llm.invoke(messages)

    return response.content

    response = llm.invoke(
        f"""
You are a helpful general AI assistant.

Answer the user's question clearly and concisely.

User query:
{query}
"""
    )

    return response.content