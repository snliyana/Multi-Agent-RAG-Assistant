from langchain_core.tools import tool
from langchain_chroma import Chroma

from backend.app.rag.vector_store import (
    CHROMA_DIR,
    COLLECTION_NAME,
    get_embedding_model,
)


@tool
def search_document(query: str) -> str:
    """
    Search the currently indexed PDF document
    and return relevant text chunks.
    """

    embedding_model = get_embedding_model()

    vector_store = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embedding_model,
        collection_name=COLLECTION_NAME,
    )

    results = vector_store.similarity_search(
        query,
        k=3
    )

    if not results:
        return (
            "No relevant information was found "
            "in the uploaded document."
        )

    formatted_results = []

    for i, doc in enumerate(
        results,
        start=1
    ):

        page = doc.metadata.get(
            "page_label",
            "unknown"
        )

        formatted_results.append(
            f"Result {i} - Page {page}:\n"
            f"{doc.page_content}"
        )

    return "\n\n".join(
        formatted_results
    )