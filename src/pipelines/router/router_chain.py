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

        self.chain = (
            self.prompt
            | self.llm.with_structured_output(RouterDecision)
        )

    def run(self, question: str) -> RouterDecision:
        return self.chain.invoke({"question": question})