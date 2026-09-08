from dotenv import load_dotenv

load_dotenv()

from backend.app.agents.finance_agent import finance_agent


result = finance_agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is the current stock information for NVIDIA?"
            }
        ]
    }
)


print("\n--- FINANCE AGENT RESULT ---")

print(result["messages"][-1].content)