from dotenv import load_dotenv

load_dotenv()

from backend.app.graph.workflow import graph


initial_state = {
    "query": "Hello, what can you help me with?",
    "next_agent": "",
    "results": [],
    "final_answer": ""
}


result = graph.invoke(initial_state)


print("\n--- RESULT ---")

print("Query:")
print(result["query"])

print("\nSelected Agent:")
print(result["next_agent"])

print("\nFinal Answer:")
print(result["final_answer"])