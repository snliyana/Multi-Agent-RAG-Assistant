# 🤖 Multi-Agent RAG Assistant

A multi-agent AI assistant built using **LangGraph, LangChain, Groq, FastAPI, Streamlit, and Retrieval-Augmented Generation (RAG)**.

The system uses a supervisor-based architecture to automatically route user queries to specialized AI agents for research, weather information, financial data, Python calculations, document question answering, and general conversation.

## ✨ Features

- 🧠 **Supervisor Agent** – Routes user queries to the appropriate specialized agent
- 🔎 **Research Agent** – Performs web and Wikipedia research
- 🌤️ **Weather Agent** – Retrieves current weather information
- 📈 **Finance Agent** – Retrieves stock and company market information
- 🐍 **Python Agent** – Executes Python-based calculations
- 📄 **RAG Agent** – Answers questions from uploaded PDF documents
- 💬 **General Agent** – Handles general conversations and questions
- 🧠 **Conversation Memory** – Maintains chat context using session-based memory
- 📤 **PDF Upload & Indexing** – Upload and process documents directly from the UI
- ⚡ **FastAPI Backend** – Provides REST API endpoints for chat and document upload
- 🖥️ **Streamlit Frontend** – Interactive web interface for users

## 🏗️ Architecture

```text
                         User
                           │
                           ▼
                    Streamlit Frontend
                           │
                           ▼
                     FastAPI Backend
                           │
                           ▼
                  LangGraph Supervisor
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
  Research Agent      Weather Agent      Finance Agent
        │                  │                  │
        ▼                  ▼                  ▼
 DuckDuckGo /          Weather API          yfinance
 Wikipedia
        │
        ├──────────────┬──────────────┐
        ▼              ▼              ▼
  Python Agent      RAG Agent     General Agent
        │              │
        ▼              ▼
   Python REPL     Chroma Vector DB
                       │
                       ▼
              HuggingFace Embeddings
                       │
                       ▼
                 Uploaded PDF

                           │
                           ▼
                       Groq LLM
```

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | LLM and tool integration |
| LangGraph | Multi-agent workflow orchestration |
| Groq | LLM inference |
| FastAPI | Backend REST API |
| Streamlit | Web application frontend |
| ChromaDB | Vector database |
| HuggingFace | Document embeddings |
| PyPDF | PDF document processing |
| DuckDuckGo | Web research |
| Wikipedia | Knowledge retrieval |
| yfinance | Financial market data |
| Python REPL | Mathematical and Python execution |

## 📂 Project Structure

```text
Multi-Agent-RAG-Assistant/
│
├── backend/
│   └── app/
│       ├── agents/
│       │   ├── finance_agent.py
│       │   ├── general_agent.py
│       │   ├── python_agent.py
│       │   ├── rag_agent.py
│       │   ├── research_agent.py
│       │   └── weather_agent.py
│       │
│       ├── graph/
│       │   ├── state.py
│       │   ├── supervisor.py
│       │   └── workflow.py
│       │
│       ├── memory/
│       │   └── session_memory.py
│       │
│       ├── rag/
│       │   ├── document_loader.py
│       │   ├── retriever_tool.py
│       │   └── vector_store.py
│       │
│       ├── tools/
│       │   ├── finance_tools.py
│       │   ├── python_tools.py
│       │   ├── research_tools.py
│       │   └── weather_tools.py
│       │
│       └── main.py
│
├── frontend/
│   └── app.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/snliyana/Multi-Agent-RAG-Assistant.git
cd Multi-Agent-RAG-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

Never commit your real API keys to GitHub.

### 5. Start the FastAPI backend

```bash
uvicorn backend.app.main:app --reload
```

FastAPI documentation will be available locally at:

```text
http://127.0.0.1:8000/docs
```

### 6. Start the Streamlit frontend

Open another terminal and run:

```bash
streamlit run frontend/app.py
```

The application will then be available in your browser.

## 💡 Example Queries

```text
What is the current weather in Kuala Lumpur?

What is the current stock information for NVIDIA?

Calculate 125 * 48 and explain the result.

Who is Alan Turing?

What is this uploaded document about?
```

The supervisor analyzes each query and routes it to the appropriate agent.

## 📄 RAG Workflow

The document question-answering pipeline works as follows:

```text
PDF Upload
   ↓
Document Loader
   ↓
Text Splitting
   ↓
HuggingFace Embeddings
   ↓
Chroma Vector Database
   ↓
Similarity Search
   ↓
RAG Agent
   ↓
LLM-generated Answer
```

When a new PDF is uploaded, it becomes the active document used by the RAG agent.

## 🔐 Security

Sensitive information is excluded from version control using `.gitignore`.

The following files/directories are not committed:

```text
.env
venv/
data/chroma_db/
data/uploads/
```

An `.env.example` file is provided to show the required environment variables without exposing API credentials.

## 🎯 Project Purpose

This project was developed as a hands-on implementation of **Agentic AI and multi-agent systems**.

It demonstrates:

- LLM tool calling
- Agent specialization
- Supervisor-based routing
- LangGraph workflows
- Retrieval-Augmented Generation (RAG)
- Vector databases and embeddings
- Conversation memory
- REST API development
- Frontend/backend integration

## 🔮 Future Improvements

Potential improvements include:

- Support for multiple active documents
- Persistent conversation memory
- User authentication
- Streaming LLM responses
- Additional specialized agents
- Document management
- Cloud deployment and monitoring

## 👩‍💻 Author

**Liyana Ishak**

AI/ML & Agentic AI Portfolio Project