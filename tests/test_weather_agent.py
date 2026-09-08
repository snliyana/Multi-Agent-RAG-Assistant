from dotenv import load_dotenv

load_dotenv()

from backend.app.agents.weather_agent import weather_agent


result = weather_agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is the current weather in Kuala Lumpur?"
            }
        ]
    }
)


print("\n--- WEATHER AGENT RESULT ---")

print(result["messages"][-1].content)