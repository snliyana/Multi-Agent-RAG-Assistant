from dotenv import load_dotenv

load_dotenv()

from backend.app.graph.supervisor import supervisor_node


test_state = {
    "query": "Calculate 125 * 48",
    "next_agent": "",
    "results": [],
    "final_answer": ""
}


result = supervisor_node(test_state)

print(result)