from dotenv import load_dotenv

load_dotenv()

from backend.app.agents.python_agent import python_agent


result = python_agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Calculate 125 * 48 and explain the result."
            }
        ]
    }
)


print("\n--- PYTHON AGENT RESULT ---")

print(result["messages"][-1].content)