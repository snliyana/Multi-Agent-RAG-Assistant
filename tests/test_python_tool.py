from backend.app.tools.python_tools import python_repl_tool


result = python_repl_tool.invoke(
    "print(125 * 48)"
)


print("\n--- PYTHON TOOL RESULT ---")
print(result)