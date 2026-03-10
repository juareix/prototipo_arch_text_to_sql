import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama

def get_ollama_llm():
    load_dotenv()
    model = os.getenv("OLLAMA_MODEL", "llama2")
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    return Ollama(model=model, base_url=base_url)
