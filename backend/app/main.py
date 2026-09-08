from pathlib import Path
import shutil

from dotenv import load_dotenv

# Load environment variables FIRST
load_dotenv()

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

from backend.app.graph.workflow import graph
from backend.app.memory.session_memory import (
    get_chat_history,
    save_message,
)
from backend.app.rag.vector_store import create_vector_store


app = FastAPI(
    title="Multi-Agent RAG Assistant API",
    description="FastAPI backend for a LangGraph multi-agent AI assistant",
    version="1.0.0",
)


# --------------------------------
# Request / Response Models
# --------------------------------

class ChatRequest(BaseModel):
    message: str
    session_id: str


class ChatResponse(BaseModel):
    answer: str
    agent: str


# --------------------------------
# Upload Directory
# --------------------------------

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# --------------------------------
# Basic Endpoints
# --------------------------------

@app.get("/")
def root():
    return {
        "message": "Multi-Agent RAG Assistant API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# --------------------------------
# Chat Endpoint
# --------------------------------

@app.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    chat_history = get_chat_history(
        request.session_id
    )

    initial_state = {
        "query": request.message,
        "next_agent": "",
        "results": [],
        "final_answer": "",
        "chat_history": chat_history,
    }

    result = graph.invoke(
        initial_state
    )

    save_message(
        session_id=request.session_id,
        role="user",
        content=request.message,
    )

    save_message(
        session_id=request.session_id,
        role="assistant",
        content=result["final_answer"],
    )

    return ChatResponse(
        answer=result["final_answer"],
        agent=result["next_agent"],
    )


# --------------------------------
# PDF Upload Endpoint
# --------------------------------

@app.post("/upload")
def upload_document(
    file: UploadFile = File(...)
):

    if not file.filename:
        return {
            "status": "error",
            "message": "No file was provided."
        }

    if not file.filename.lower().endswith(".pdf"):
        return {
            "status": "error",
            "message": "Only PDF files are supported."
        }

    file_path = (
        UPLOAD_DIR /
        Path(file.filename).name
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    create_vector_store(
        str(file_path)
    )

    return {
        "status": "success",
        "filename": file.filename,
        "message": (
            "Document uploaded and "
            "indexed successfully."
        )
    }