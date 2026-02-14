from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama

class LLMFactory:

    @staticmethod
    def get_sql_llm():
        return ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0
        )

    @staticmethod
    def get_answer_llm(streaming=False, callbacks=None):
        return ChatOpenAI(
            model="gpt-4o",
            temperature=0.2,
            streaming=streaming,
            callbacks=callbacks
        )

    @staticmethod
    def get_local_llm():
        return Ollama(model="llama3")
