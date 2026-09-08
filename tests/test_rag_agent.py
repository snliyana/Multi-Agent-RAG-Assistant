from dotenv import load_dotenv

load_dotenv()

from backend.app.agents.rag_agent import rag_agent


result = rag_agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What position is mentioned in the document?"
            }
        ]
    }
)


print("\n--- RAG AGENT RESULT ---")

print(result["messages"][-1].content)