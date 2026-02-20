import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

_llm_cache = {}

def get_llm(llm_type: str = "router"):
	"""
	Retorna uma instância do LLM configurada para o tipo solicitado.
	Atualmente suporta apenas Gemini via langchain-google-genai.
	"""
	if llm_type in _llm_cache:
		return _llm_cache[llm_type]

	load_dotenv()
	api_key = os.getenv("GEMINY_KEY")
	if not api_key:
		raise ValueError("Chave da API Gemini não encontrada no .env (GEMINY-KEY)")

	llm = ChatGoogleGenerativeAI(
		model="gemini-3-flash-preview",
		google_api_key=api_key,
		temperature=0.0,
		convert_system_message_to_human=True,
	)
	_llm_cache[llm_type] = llm
	return llm
