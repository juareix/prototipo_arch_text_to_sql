from langchain_core.prompts import ChatPromptTemplate
from infrastructure.llm.llm_factory import get_llm
from .router_prompt import ROUTER_SYSTEM_PROMPT
from .schemas import RouterDecision


class RouterChain:

    def __init__(self):
        self.llm = get_llm("router")

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", ROUTER_SYSTEM_PROMPT),
            ("human", "{question}")
        ])

        self.chain = self.prompt | self.llm

    def run(self, question: str) -> RouterDecision:
        import json
        from .schemas import RouterDecision
        response = self.chain.invoke({"question": question})
        # Extrai o JSON da resposta
        try:
            if isinstance(response, dict):
                return RouterDecision(**response)
            # Tenta encontrar o JSON na resposta textual
            json_str = response
            # Remove texto extra antes/depois do JSON
            json_start = json_str.find('{')
            json_end = json_str.rfind('}') + 1
            json_str = json_str[json_start:json_end]
            data = json.loads(json_str)
            return RouterDecision(**data)
        except Exception as e:
            raise ValueError(f"Falha ao parsear resposta do LLM: {response}\nErro: {e}")