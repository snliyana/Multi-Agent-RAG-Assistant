# 🤖 AgentHub AI — Multi-Agent RAG Assistant

AgentHub AI is a multi-agent AI assistant built using **LangGraph, LangChain, Groq, FastAPI, Streamlit, and Retrieval-Augmented Generation (RAG)**.

The system uses a supervisor-based architecture to automatically route user queries to specialized AI agents.

---

## 🚀 Live Demo

👉 [Launch AgentHub AI](https://snliyana-multi-agent-rag-assistant-frontendapp-ukyhqa.streamlit.app/)

> **Note:** The backend is hosted on Render's free tier, so the first request may take a short time after inactivity.

---

## ✨ Features

- 🧠 **Supervisor-based routing** — routes queries to specialized agents
- 🔎 **Research Agent** — DuckDuckGo and Wikipedia research
- 🌤️ **Weather Agent** — current weather information
- 📈 **Finance Agent** — stock and market information
- 🐍 **Python Agent** — calculations and Python execution
- 📄 **RAG Agent** — question answering from uploaded PDF documents
- 💬 **General Agent** — general conversations and questions
- 🧠 **Session-based conversation memory**
- 📤 **PDF upload and indexing**
- ⚡ **FastAPI backend**
- 🖥️ **Streamlit frontend**
- ☁️ **Cloud deployment**

---

## 🏗️ Architecture

```text
User
  ↓
Streamlit Frontend
  ↓
FastAPI Backend
  ↓
LangGraph Supervisor
  ↓
Specialized Agent
  ↓
Tool / RAG / External Data
  ↓
Groq LLM
  ↓
Final Answer
```

The LangGraph supervisor analyzes each request and routes it to the most appropriate specialized agent.

---

## 🤖 Agents

| Agent | Purpose |
|---|---|
| 🔎 Research Agent | DuckDuckGo and Wikipedia research |
| 🌤️ Weather Agent | Current weather information |
| 📈 Finance Agent | Stock and market information |
| 🐍 Python Agent | Calculations and Python execution |
| 📄 RAG Agent | Question answering from uploaded PDF documents |
| 💬 General Agent | General conversation and questions |

---

## 📄 RAG Workflow

```text
PDF Upload
  ↓
Document Loader
  ↓
Text Splitting
  ↓
FastEmbed Embeddings
  ↓
Chroma Vector Database
  ↓
Similarity Search
  ↓
RAG Agent
  ↓
Groq LLM
  ↓
Answer
```

When a PDF is uploaded and indexed, the RAG agent retrieves relevant document chunks and uses them as context to generate an answer.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | LLM and tool integration |
| LangGraph | Multi-agent workflow orchestration |
| Groq | LLM inference |
| FastAPI | Backend REST API |
| Streamlit | Web application frontend |
| ChromaDB | Vector database for RAG |
| FastEmbed | Document embeddings |
| PyPDF | PDF document processing |
| DuckDuckGo | Web research |
| Wikipedia | Knowledge retrieval |
| yfinance | Financial market data |
| Python REPL | Calculations and Python execution |
| Render | Backend deployment |
| Streamlit Community Cloud | Frontend deployment |
| GitHub | Source code and version control |

---

## 🚀 Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/snliyana/Multi-Agent-RAG-Assistant.git
cd Multi-Agent-RAG-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
OPENWEATHER_API_KEY=your_openweather_api_key_here
```

Never commit real API keys to GitHub.

### 5. Start the FastAPI backend

```bash
uvicorn backend.app.main:app --reload
```

The backend will run locally at:

```text
http://127.0.0.1:8000
```

### 6. Start the Streamlit frontend

Open another terminal and run:

```bash
streamlit run frontend/app.py
```

---

## 💡 Example Queries

```text
What is the current weather in Kuala Lumpur?

What is the current stock information for NVIDIA?

Calculate 125 * 48 and explain the result.

Who is Alan Turing?

What is this uploaded document about?
```

---

## ☁️ Deployment

The application uses separate cloud services for the frontend and backend:

- **Frontend:** Streamlit Community Cloud
- **Backend:** Render
- **Source Code:** GitHub

The Streamlit frontend communicates with the deployed FastAPI backend through REST API requests.

---

## 🔐 Security

Sensitive information is excluded from version control using `.gitignore`.

Examples include:

```text
.env
venv/
data/chroma_db/
data/uploads/
```

API keys are configured using environment variables or deployment platform secrets rather than being committed to the repository.

---

## ⚠️ Limitations

This project is designed as a portfolio prototype rather than a production-ready system.

Current limitations include:

- Session-based memory is not persistent across restarts
- Uploaded documents are not stored permanently
- RAG currently focuses on the active uploaded PDF
- No user authentication or persistent multi-user storage
- The application depends on external APIs and cloud services
- Free-tier cloud resources may cause slower response times
- Multi-turn follow-up context may not be handled consistently across all specialized agents
- Agent routing may be less reliable for ambiguous queries

---

## 🔮 Future Improvements

Potential improvements include:

- Persistent conversation memory
- Persistent cloud document storage
- Multi-document RAG
- User authentication
- Source citations for RAG answers
- More robust multi-turn agent routing
- Improved error handling, logging, and monitoring
- Automated testing and CI/CD

---

## 🎯 Project Purpose

This project was developed as a hands-on implementation of **Agentic AI and multi-agent systems**.

It demonstrates practical experience with:

- LLM tool calling
- Agent specialization
- Supervisor-based routing
- LangGraph workflows
- Retrieval-Augmented Generation (RAG)
- Vector databases and embeddings
- Conversation memory
- REST API development
- Frontend/backend integration
- Cloud deployment
- Git and GitHub version control

---

## 👩‍💻 Author

**Liyana Ishak**

AI/ML & Agentic AI Portfolio Project