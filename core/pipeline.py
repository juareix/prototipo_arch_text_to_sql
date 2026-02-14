from stages.retrieval import RetrievalStage
from stages.sql_agent import SQLStage
from stages.answer_generator import AnswerStage

class Pipeline:

    def __init__(self):
        self.retrieval = RetrievalStage(...)
        self.sql = SQLStage(...)
        self.answer = AnswerStage()

    async def run(self, question: str):

        retrieval_context = await self.retrieval.run(question)

        sql_query = await self.sql.run(question)

        sql_result = "mock_result"

        async for token in self.answer.stream(
            question,
            sql_result,
            retrieval_context
        ):
            yield token
