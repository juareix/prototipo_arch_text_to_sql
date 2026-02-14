import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from core.pipeline import Pipeline
from fastapi import status
from fastapi.responses import JSONResponse
import json


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # em produção você restringe
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "API online!"}

pipeline = Pipeline()

@app.post("/chat")
async def chat(request: Request):
    try:
        data = await request.json()
        question = data.get("question")
        if not question:
            return JSONResponse({"error": "Campo 'question' é obrigatório."}, status_code=status.HTTP_400_BAD_REQUEST)
    except Exception:
        return JSONResponse({"error": "JSON inválido."}, status_code=status.HTTP_400_BAD_REQUEST)

    async def generator():
        async for token in pipeline.run(question):
            yield token

    return StreamingResponse(generator(), media_type="text/plain")
