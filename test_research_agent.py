from dotenv import load_dotenv

load_dotenv()

from backend.app.agents.research_agent import research_agent


result = research_agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Latest developments in artificial intelligence"
            }
        ]
    }
)


print("\n--- RESEARCH AGENT RESULT ---")

print(result["messages"][-1].content)