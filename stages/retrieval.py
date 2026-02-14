from llama_index.core import VectorStoreIndex

class RetrievalStage:

    def __init__(self, index: VectorStoreIndex):
        self.index = index

    async def run(self, question: str):
        query_engine = self.index.as_query_engine()
        response = await query_engine.aquery(question)
        return str(response)
