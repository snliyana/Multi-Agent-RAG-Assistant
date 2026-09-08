from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not set in .env file")

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=api_key,
    temperature=0.2
)

response = llm.invoke("Say hello and introduce yourself in one short sentence.")

print(response.content)