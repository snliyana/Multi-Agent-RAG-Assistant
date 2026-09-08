import wikipedia

from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import (
    WikipediaQueryRun,
    DuckDuckGoSearchRun,
)

from langchain_core.tools import tool


# Wikimedia requires a descriptive User-Agent
wikipedia.set_user_agent(
    "MultiAIAgentProject/1.0 (educational project)"
)


# -----------------------------
# Wikipedia Tool
# -----------------------------

wikipedia_wrapper = WikipediaAPIWrapper(
    top_k_results=2,
    doc_content_chars_max=2000
)

wikipedia_tool = WikipediaQueryRun(
    api_wrapper=wikipedia_wrapper
)


# -----------------------------
# DuckDuckGo Search Tool
# -----------------------------

_ddg_search = DuckDuckGoSearchRun()


@tool
def duckduckgo_tool(query: str) -> str:
    """
    Search the web using DuckDuckGo.

    If the search provider is temporarily unavailable,
    return an error message instead of crashing the agent.
    """

    try:
        result = _ddg_search.run(query)

        if not result:
            return "Web search returned no results."

        return result

    except Exception as e:
        return (
            "Web search is temporarily unavailable. "
            "Please use another available research source such as Wikipedia. "
            f"Search error: {str(e)}"
        )