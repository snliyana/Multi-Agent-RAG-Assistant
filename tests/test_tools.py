from backend.app.tools.research_tools import duckduckgo_tool


result = duckduckgo_tool.invoke(
    "latest developments in artificial intelligence"
)

print(result)