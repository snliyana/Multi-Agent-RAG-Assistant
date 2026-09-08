# 🤖 AgentHub AI — Multi-Agent RAG Assistant

AgentHub AI is a multi-agent AI assistant built using **LangGraph, LangChain, Groq, FastAPI, Streamlit, and Retrieval-Augmented Generation (RAG)**.

The system uses a supervisor-based architecture to automatically route user queries to specialized AI agents for research, weather information, financial data, Python calculations, document question answering, and general conversation.

---

## 🚀 Live Demo

Try the deployed application here:

👉 [Launch AgentHub AI](https://snliyana-multi-agent-rag-assistant-frontendapp-ukyhqa.streamlit.app/)

> **Note:** The backend is hosted on Render's free tier. The first request may take a short time while the server wakes up after a period of inactivity.

---

## ✨ Features

- 🧠 **Supervisor Agent** – Routes user queries to the appropriate specialized agent
- 🔎 **Research Agent** – Performs web and Wikipedia research
- 🌤️ **Weather Agent** – Retrieves current weather information
- 📈 **Finance Agent** – Retrieves stock and company market information
- 🐍 **Python Agent** – Executes Python-based calculations
- 📄 **RAG Agent** – Answers questions from uploaded PDF documents
- 💬 **General Agent** – Handles general conversations and questions
- 🧠 **Conversation Memory** – Maintains chat context using session-based memory
- 📤 **PDF Upload & Indexing** – Uploads and processes documents directly from the UI
- ⚡ **FastAPI Backend** – Provides REST API endpoints for chat and document upload
- 🖥️ **Streamlit Frontend** – Provides an interactive web interface
- 🌐 **Cloud Deployment** – Frontend deployed on Streamlit Community Cloud and backend deployed on Render

---

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
       ┌───────────────────┼───────────────────┐
       │                   │                   │
       ▼                   ▼                   ▼
 Research Agent       Weather Agent       Finance Agent
       │                   │                   │
       ▼                   ▼                   ▼
DuckDuckGo /          Weather API           yfinance
 Wikipedia
       │
       ├───────────────────┬───────────────────┐
       │                   │                   │
       ▼                   ▼                   ▼
 Python Agent          RAG Agent         General Agent
       │                   │
       ▼                   ▼
 Python REPL        Chroma Vector DB
                           │
                           ▼
                 FastEmbed Embeddings
                           │
                           ▼
                     Uploaded PDF

                           │
                           ▼
                       Groq LLM