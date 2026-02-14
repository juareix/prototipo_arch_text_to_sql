
from core.llm_factory import LLMFactory
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.utilities.sql_database import SQLDatabase

class SQLStage:
    def __init__(self, db_uri: str):
        self.llm = LLMFactory.get_sql_llm()
        self.db = SQLDatabase.from_uri(db_uri)
        self.agent = create_sql_agent(
            llm=self.llm,
            db=self.db,
            agent_type="tool-calling",
            verbose=True
        )

    async def run(self, question: str):
        # O agente espera um dicionário com a chave 'input'
        result = await self.agent.ainvoke({"input": question})
        return result["output"]
