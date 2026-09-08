from langgraph.graph import StateGraph, START, END
from backend.app.agents.research_agent import research_agent
from backend.app.graph.state import AgentState
from backend.app.graph.supervisor import supervisor_node
from backend.app.agents.weather_agent import weather_agent
from backend.app.agents.finance_agent import finance_agent
from backend.app.agents.python_agent import python_agent
from backend.app.agents.rag_agent import rag_agent
from backend.app.agents.general_agent import run_general_agent

# --------------------------------
# Temporary Agent Nodes
# --------------------------------

def research_agent_node(state: AgentState) -> AgentState:

    response = research_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": state["query"]
                }
            ]
        }
    )

    final_response = response["messages"][-1].content

    state["results"].append(final_response)
    state["final_answer"] = final_response

    return state


def rag_agent_node(state: AgentState) -> AgentState:

    response = rag_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": state["query"]
                }
            ]
        }
    )

    final_response = response["messages"][-1].content

    state["results"].append(final_response)
    state["final_answer"] = final_response

    return state


def finance_agent_node(state: AgentState) -> AgentState:

    response = finance_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": state["query"]
                }
            ]
        }
    )

    final_response = response["messages"][-1].content

    state["results"].append(final_response)
    state["final_answer"] = final_response

    return state


def weather_agent_node(state: AgentState) -> AgentState:

    response = weather_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": state["query"]
                }
            ]
        }
    )

    final_response = response["messages"][-1].content

    state["results"].append(final_response)
    state["final_answer"] = final_response

    return state


def python_agent_node(state: AgentState) -> AgentState:

    response = python_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": state["query"]
                }
            ]
        }
    )

    final_response = response["messages"][-1].content

    state["results"].append(final_response)
    state["final_answer"] = final_response

    return state


def general_agent_node(state: AgentState) -> AgentState:

    final_response = run_general_agent(
        query=state["query"],
        chat_history=state["chat_history"],
    )

    state["results"].append(final_response)
    state["final_answer"] = final_response

    return state


# --------------------------------
# Router
# --------------------------------

def route_to_agent(state: AgentState):
    return state["next_agent"]


# --------------------------------
# Build LangGraph
# --------------------------------

workflow = StateGraph(AgentState)

workflow.add_node(
    "supervisor",
    supervisor_node
)

workflow.add_node(
    "research_agent",
    research_agent_node
)

workflow.add_node(
    "rag_agent",
    rag_agent_node
)

workflow.add_node(
    "finance_agent",
    finance_agent_node
)

workflow.add_node(
    "weather_agent",
    weather_agent_node
)

workflow.add_node(
    "python_agent",
    python_agent_node
)

workflow.add_node(
    "general_agent",
    general_agent_node
)


# START → Supervisor
workflow.add_edge(
    START,
    "supervisor"
)


# Supervisor → Selected Agent
workflow.add_conditional_edges(
    "supervisor",
    route_to_agent,
    {
        "research_agent": "research_agent",
        "rag_agent": "rag_agent",
        "finance_agent": "finance_agent",
        "weather_agent": "weather_agent",
        "python_agent": "python_agent",
        "general_agent": "general_agent",
    }
)


# Agents → END
workflow.add_edge("research_agent", END)
workflow.add_edge("rag_agent", END)
workflow.add_edge("finance_agent", END)
workflow.add_edge("weather_agent", END)
workflow.add_edge("python_agent", END)
workflow.add_edge("general_agent", END)


# Compile graph
graph = workflow.compile()