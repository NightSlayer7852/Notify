# utils/llm.py
import os
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0.7
)

def call_llm(prompt):
    messages = [
        SystemMessage(content="You are a helpful AI assistant."),
        HumanMessage(content=prompt)
    ]

    response = llm.invoke(messages)
    return response.content