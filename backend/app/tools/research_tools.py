import wikipedia

from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import (
    WikipediaQueryRun,
    DuckDuckGoSearchRun,
)


# Wikimedia requires a descriptive User-Agent
wikipedia.set_user_agent(
    "MultiAIAgentProject/1.0 (educational project)"
)


wikipedia_wrapper = WikipediaAPIWrapper(
    top_k_results=2,
    doc_content_chars_max=2000
)


wikipedia_tool = WikipediaQueryRun(
    api_wrapper=wikipedia_wrapper
)


duckduckgo_tool = DuckDuckGoSearchRun()