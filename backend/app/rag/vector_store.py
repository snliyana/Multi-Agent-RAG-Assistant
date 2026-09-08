from pathlib import Path

from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_chroma import Chroma

from backend.app.rag.document_loader import load_and_split_pdf


CHROMA_DIR = "data/chroma_db"
COLLECTION_NAME = "rag_documents"


def get_embedding_model():

    return FastEmbedEmbeddings(
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

    embedding_model = get_embedding_model()

    old_store = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embedding_model,
        collection_name=COLLECTION_NAME,
    )

    try:
        old_store.delete_collection()
    except Exception:
        pass

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CHROMA_DIR,
        collection_name=COLLECTION_NAME,
    )

    return vector_store