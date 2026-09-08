import os
import uuid
import requests
import streamlit as st


API_URL = st.secrets.get(
    "API_URL",
    os.getenv(
        "API_URL",
        "http://127.0.0.1:8000"
    )
)

# --------------------------------
# Page Config
# --------------------------------

st.set_page_config(
    page_title="AgentHub AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --------------------------------
# Custom CSS
# --------------------------------

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1200px;
        }

        .main-header {
            padding: 1.4rem 1.6rem;
            border-radius: 18px;
            border: 1px solid rgba(120, 120, 120, 0.25);
            margin-bottom: 1.5rem;
        }

        .main-header h1 {
            margin: 0;
            font-size: 2.1rem;
        }

        .main-header p {
            margin-top: 0.35rem;
            opacity: 0.75;
            font-size: 0.95rem;
        }

        .agent-card {
            padding: 0.75rem 0.9rem;
            border-radius: 12px;
            border: 1px solid rgba(120, 120, 120, 0.22);
            margin-bottom: 0.5rem;
        }

        .status-box {
            padding: 0.75rem 0.9rem;
            border-radius: 12px;
            border: 1px solid rgba(120, 120, 120, 0.22);
            margin-bottom: 0.8rem;
        }

        .small-label {
            font-size: 0.82rem;
            opacity: 0.7;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------
# Session State
# --------------------------------

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded_document" not in st.session_state:
    st.session_state.uploaded_document = None


# --------------------------------
# Header
# --------------------------------

st.markdown(
    """
    <div class="main-header">
        <h1>🤖 AgentHub AI</h1>
        <p>
            Multi-Agent AI Assistant powered by LangGraph, Groq,
            FastAPI and Streamlit
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# --------------------------------
# Sidebar
# --------------------------------

with st.sidebar:

    st.title("⚙️ AgentHub")

    st.caption(
        "Multi-agent orchestration with RAG, tools and memory."
    )

    st.divider()

    # --------------------------------
    # Document Upload
    # --------------------------------

    st.subheader("📄 Document RAG")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"],
        key="rag_pdf_uploader",
    )

    if uploaded_file is not None:

        if st.button(
            "📤 Upload & Index",
            key="upload_pdf_button",
            use_container_width=True,
        ):

            with st.spinner(
                "Uploading and indexing document..."
            ):

                try:

                    files = {
                        "file": (
                            uploaded_file.name,
                            uploaded_file.getvalue(),
                            "application/pdf",
                        )
                    }

                    response = requests.post(
                        f"{API_URL}/upload",
                        files=files,
                        timeout=180,
                    )

                    response.raise_for_status()

                    data = response.json()

                    if data.get("status") == "success":

                        st.session_state.uploaded_document = (
                            uploaded_file.name
                        )

                        st.success(
                            "Document indexed successfully."
                        )

                    else:

                        st.error(
                            data.get(
                                "message",
                                "Document upload failed."
                            )
                        )

                except requests.exceptions.RequestException:

                    st.error(
                        "Unable to connect to backend upload API."
                    )

    if st.session_state.uploaded_document:

        st.markdown(
            f"""
            <div class="status-box">
                <div class="small-label">Active document</div>
                📄 <b>{st.session_state.uploaded_document}</b>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    # --------------------------------
    # Available Agents
    # --------------------------------

    st.subheader("🧠 Available Agents")

    agents = [
        ("🔎", "Research Agent"),
        ("🌤️", "Weather Agent"),
        ("📈", "Finance Agent"),
        ("🐍", "Python Agent"),
        ("📄", "RAG Agent"),
        ("💬", "General Agent"),
    ]

    for icon, name in agents:

        st.markdown(
            f"""
            <div class="agent-card">
                {icon} <b>{name}</b>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    # --------------------------------
    # Clear Chat
    # --------------------------------

    if st.button(
        "🗑️ Clear Chat",
        key="clear_chat_button",
        use_container_width=True,
    ):

        st.session_state.messages = []
        st.session_state.session_id = str(uuid.uuid4())

        st.rerun()


# --------------------------------
# Main Status Row
# --------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Agents",
        "6"
    )

with col2:
    st.metric(
        "Backend",
        "FastAPI"
    )

with col3:
    st.metric(
        "LLM",
        "GPT-OSS-120B"
    )


st.divider()


# --------------------------------
# Chat History
# --------------------------------

if not st.session_state.messages:

    st.info(
        "Ask a question, upload a PDF, check the weather, "
        "search finance data, or run a calculation."
    )


for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

        if message.get("agent"):

            agent_name = (
                message["agent"]
                .replace("_", " ")
                .title()
            )

            st.caption(
                f"🧠 Agent: {agent_name}"
            )


# --------------------------------
# Chat Input
# --------------------------------

prompt = st.chat_input(
    "Ask AgentHub AI anything..."
)


if prompt:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    # Display user message
    with st.chat_message("user"):

        st.markdown(prompt)


    # --------------------------------
    # Call Backend
    # --------------------------------

    with st.chat_message("assistant"):

        with st.spinner(
            "AgentHub is thinking..."
        ):

            try:

                response = requests.post(
                    f"{API_URL}/chat",
                    json={
                        "message": prompt,
                        "session_id": (
                            st.session_state.session_id
                        ),
                    },
                    timeout=120,
                )

                response.raise_for_status()

                data = response.json()

                answer = data["answer"]
                agent = data["agent"]

                # Display answer
                st.markdown(answer)

                agent_name = (
                    agent
                    .replace("_", " ")
                    .title()
                )

                st.caption(
                    f"🧠 Agent: {agent_name}"
                )

                # Save response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "agent": agent,
                    }
                )

            except requests.exceptions.RequestException as e:

                error_message = (
                    f"Unable to connect to the backend API.\n\n"
                    f"API URL: {API_URL}\n\n"
                    f"Error: {str(e)}"
                )

                st.error(error_message)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message,
                        "agent": "system",
                    }
                )