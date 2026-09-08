# 🤖 AgentHub AI — Multi-Agent RAG Assistant

AgentHub AI is a multi-agent AI assistant built using **LangGraph, LangChain, Groq, FastAPI, Streamlit, and Retrieval-Augmented Generation (RAG)**.

The system uses a supervisor-based architecture to automatically route user queries to specialized AI agents.

## 🚀 Live Demo

👉 [Launch AgentHub AI](https://snliyana-multi-agent-rag-assistant-frontendapp-ukyhqa.streamlit.app/)

> Note: The backend is hosted on Render's free tier, so the first request may take a short time after inactivity.

## ✨ Features

- 🧠 Supervisor-based agent routing
- 🔎 Research Agent
- 🌤️ Weather Agent
- 📈 Finance Agent
- 🐍 Python Agent
- 📄 RAG Agent
- 💬 General Agent
- 🧠 Session-based conversation memory
- 📤 PDF upload and indexing
- ⚡ FastAPI backend
- 🖥️ Streamlit frontend
- 🌐 Cloud deployment

## 🏗️ Architecture

User  
→ Streamlit Frontend  
→ FastAPI Backend  
→ LangGraph Supervisor  
→ Specialized Agent  
→ Tool / RAG / External Data  
→ Groq LLM  
→ Final Answer

## 🤖 Agents

- **Research Agent** — DuckDuckGo and Wikipedia research
- **Weather Agent** — current weather information
- **Finance Agent** — stock and market information
- **Python Agent** — calculations and Python execution
- **RAG Agent** — answers questions from uploaded PDF documents
- **General Agent** — general conversation and follow-up questions

## 📄 RAG Workflow

PDF Upload  
→ Document Loader  
→ Text Splitting  
→ FastEmbed Embeddings  
→ Chroma Vector Database  
→ Similarity Search  
→ RAG Agent  
→ Groq LLM  
→ Answer

## 🛠️ Tech Stack

- Python
- LangChain
- LangGraph
- Groq
- FastAPI
- Streamlit
- ChromaDB
- FastEmbed
- PyPDF
- DuckDuckGo
- Wikipedia
- yfinance
- Python REPL
- Render
- Streamlit Community Cloud
- GitHub

## 🚀 Local Setup

```bash
git clone https://github.com/snliyana/Multi-Agent-RAG-Assistant.git
cd Multi-Agent-RAG-Assistant
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt