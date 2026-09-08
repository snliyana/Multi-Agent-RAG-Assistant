from langchain_core.tools import tool
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


CHROMA_DIR = "data/chroma_db"
COLLECTION_NAME = "rag_documents"


embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)


@tool
def search_document(query: str) -> str:
    """
    Search the currently indexed PDF document
    and return relevant text chunks.
    """

    # Open the latest vector database each time
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