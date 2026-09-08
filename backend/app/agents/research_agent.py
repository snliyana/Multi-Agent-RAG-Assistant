from langchain_groq import ChatGroq
from langchain.agents import create_agent

from backend.app.tools.research_tools import (
    wikipedia_tool,
    duckduckgo_tool,
)


llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)


research_agent = create_agent(
    model=llm,
    tools=[
        wikipedia_tool,
        duckduckgo_tool,
    ],
    system_prompt="""
You are a research specialist.

Use Wikipedia for stable encyclopedic or background knowledge.

Use DuckDuckGo Search for recent information, current developments,
news, or information that may have changed over time.

Use the most appropriate tool based on the user's question.

After using the tool, provide a clear and concise answer based on
the retrieved information.
"""
)