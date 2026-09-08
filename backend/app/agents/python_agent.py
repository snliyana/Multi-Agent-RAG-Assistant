from langchain_groq import ChatGroq
from langchain.agents import create_agent

from backend.app.tools.python_tools import python_repl_tool


llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)


python_agent = create_agent(
    model=llm,
    tools=[python_repl_tool],
    system_prompt="""
You are a Python and numerical analysis specialist.

Use the Python REPL tool for calculations, mathematical problems,
data analysis, numerical reasoning, and Python execution.

Prefer using the Python tool when a calculation is required instead
of calculating mentally.

Return a clear and concise explanation of the result.

Do not execute destructive system commands, file deletion commands,
or unsafe operating-system actions.
"""
)