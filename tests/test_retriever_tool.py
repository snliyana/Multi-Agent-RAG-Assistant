from backend.app.rag.retriever_tool import search_document


result = search_document.invoke(
    {
        "query": "What position is mentioned in the agreement?"
    }
)


print("\n--- RETRIEVER TOOL RESULT ---")

print(result)