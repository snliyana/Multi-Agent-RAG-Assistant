from pathlib import Path

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from backend.app.rag.document_loader import load_and_split_pdf


CHROMA_DIR = "data/chroma_db"
COLLECTION_NAME = "rag_documents"


embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)


def create_vector_store(pdf_path: str):

    chunks = load_and_split_pdf(pdf_path)

    if not chunks:
        raise ValueError(
            "No text chunks were generated from the PDF."
        )

    Path(CHROMA_DIR).mkdir(
        parents=True,
        exist_ok=True
    )

    # Open existing collection
    old_store = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embedding_model,
        collection_name=COLLECTION_NAME,
    )

    # Remove the old collection safely
    try:
        old_store.delete_collection()
    except Exception:
        pass

    # Create a fresh collection using only the newly uploaded PDF
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CHROMA_DIR,
        collection_name=COLLECTION_NAME,
    )

    return vector_store