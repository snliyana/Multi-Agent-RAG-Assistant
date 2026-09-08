from backend.app.rag.document_loader import load_and_split_pdf


chunks = load_and_split_pdf(
    "data/sample.pdf"
)


print("\n--- DOCUMENT LOADER TEST ---")

print("Total chunks:", len(chunks))

print("\nFirst chunk:")

print(chunks[0].page_content[:1000])

print("\nMetadata:")

print(chunks[0].metadata)