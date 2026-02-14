from core.llm_factory import LLMFactory
from langchain_core.callbacks import AsyncCallbackHandler

class StreamingHandler(AsyncCallbackHandler):

    def __init__(self, queue):
        self.queue = queue

    async def on_llm_new_token(self, token, **kwargs):
        await self.queue.put(token)


class AnswerStage:

    async def stream(self, question, sql_result, retrieval_context):

        from asyncio import Queue
        queue = Queue()

        handler = StreamingHandler(queue)

        llm = LLMFactory.get_answer_llm(
            streaming=True,
            callbacks=[handler]
        )

        async def generate():
            await llm.ainvoke(
                f"""
                Pergunta: {question}

                Contexto: {retrieval_context}

                Resultado SQL:
                {sql_result}
                """
            )

        import asyncio
        asyncio.create_task(generate())

        while True:
            token = await queue.get()
            yield token
