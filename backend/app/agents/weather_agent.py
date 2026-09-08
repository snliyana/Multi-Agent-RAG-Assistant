from langchain_groq import ChatGroq
from langchain.agents import create_agent

from backend.app.tools.weather_tools import get_weather


llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)


weather_agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="""
You are a weather specialist.

When the user asks about current weather or temperature
for a location, use the get_weather tool.

Always use the tool instead of guessing weather information.

After receiving the weather data, provide a clear and
concise answer to the user.
"""
)