from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv

_llm_cache = {}

def get_llm(llm_type: str = "router"):
	"""
	Seleciona dinamicamente o provedor de LLM via .env e retorna a instância correspondente.
	"""
	load_dotenv()
	provider = os.getenv("LLM_PROVIDER", "gemini").lower()
	if provider == "gemini":
		from .gemini import get_gemini_llm
		return get_gemini_llm()
	elif provider == "ollama":
		from .ollama import get_ollama_llm
		return get_ollama_llm()
	else:
		raise ValueError(f"LLM_PROVIDER '{provider}' não suportado. Use 'gemini' ou 'ollama'.")

	llm = ChatGoogleGenerativeAI(
		model="gemini-3-flash-preview",
		google_api_key=api_key,
		temperature=0.0,
		convert_system_message_to_human=True,
	)
	_llm_cache[llm_type] = llm
	return llm
