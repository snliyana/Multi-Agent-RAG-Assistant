from backend.app.rag.vector_store import create_vector_store


vector_store = create_vector_store(
    "data/sample.pdf"
)


print("\n--- VECTOR STORE TEST ---")

print("Vector database created successfully.")


results = vector_store.similarity_search(
    "What position is mentioned in the agreement?",
    k=3
)


print("\n--- SEARCH RESULTS ---")

for i, document in enumerate(results, start=1):

    print(f"\nResult {i}:")

    print(document.page_content[:500])

    print("\nMetadata:")
    print(document.metadata)