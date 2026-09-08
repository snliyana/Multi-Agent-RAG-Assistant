from typing import Literal

from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from backend.app.graph.state import AgentState


class RouteDecision(BaseModel):
    next_agent: Literal[
        "research_agent",
        "rag_agent",
        "finance_agent",
        "weather_agent",
        "python_agent",
        "general_agent",
    ] = Field(
        ...,
        description="The agent that should handle the user's query."
    )


llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

router_llm = llm.with_structured_output(RouteDecision)


def supervisor_node(state: AgentState) -> AgentState:

    user_query = state["query"]
    chat_history = state["chat_history"]

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
You are the supervisor of a multi-agent AI system.

Your job is to route the user's query to the most suitable agent.

Available agents:

research_agent:
Use for general knowledge, web research, Wikipedia,
news, people, companies, technology, and general information.

rag_agent:
Use when the user asks questions about uploaded documents,
PDF files, reports, or knowledge stored in the vector database.

finance_agent:
Use for stocks, financial data, company financial analysis,
market information, financial statements, and investment-related data.

weather_agent:
Use for weather, temperature, forecasts, and climate conditions.

python_agent:
Use for calculations, Python execution, mathematical analysis,
data analysis, and numerical tasks.

general_agent:
Use for casual conversation or queries that do not need
a specialised tool.

Return only the appropriate next agent.
"""
            ),
            (
    "user",
    """
Conversation history:
{chat_history}

Current user query:
{query}

Choose the most suitable agent for the current query.
"""
),
        ]
    )

    chain = prompt | router_llm

    response = chain.invoke(
    {
        "query": user_query,
        "chat_history": chat_history,
    }
)

    state["next_agent"] = response.next_agent

    return state