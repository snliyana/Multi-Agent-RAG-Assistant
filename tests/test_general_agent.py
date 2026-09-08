from dotenv import load_dotenv

load_dotenv()

from backend.app.agents.general_agent import run_general_agent


result = run_general_agent(
    "Hello, what can you help me with?"
)


print("\n--- GENERAL AGENT RESULT ---")

print(result)