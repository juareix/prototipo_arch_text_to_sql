import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

def get_gemini_llm():
    load_dotenv()
    api_key = os.getenv("GEMINY_KEY")
    if not api_key:
        raise ValueError("Chave da API Gemini não encontrada no .env (GEMINY_KEY)")
    return ChatGoogleGenerativeAI(
        model="gemini-3-flash-preview",
        google_api_key=api_key,
        temperature=0.0,
        convert_system_message_to_human=True,
    )
