arquitetura pensada:

app/
│
├── main.py
│
├── core/                          # Configuração central
│   ├── config.py                  # leitura de ENV
│   ├── settings.py
│   └── logging.py
│
├── api/                           # Camada HTTP
│   └── routes/
│       └── chat.py
│
├── services/                      # Orquestração principal
│   └── chat_service.py            # chama router → pipeline
│
├── pipelines/
│   │
│   ├── router/                    # 🔥 NOVA CAMADA
│   │   ├── router_prompt.py
│   │   ├── router_chain.py
│   │   └── schemas.py
│   │
│   ├── sql/
│   │   ├── sql_prompt.py
│   │   ├── sql_generation_chain.py
│   │   ├── sql_execution.py
│   │   ├── sql_answer_chain.py
│   │   └── schema_retriever.py
│   │
│   ├── policy/
│   │   ├── policy_prompt.py
│   │   ├── policy_rag_pipeline.py
│   │   └── retriever.py
│   │
│   └── smalltalk/
│       └── smalltalk_chain.py
│
├── infrastructure/
│   │
│   ├── llm/
│   │   ├── base_llm.py
│   │   ├── llm_factory.py          # decide via ENV qual usar
│   │   ├── openai_client.py
│   │   ├── ollama_client.py
│   │   └── internal_api_client.py
|   |
│   |───docs                        #Schemas das tabelas, docs de policys
│   ├── vectorstores/
│   │   ├── base_vectorstore.py
│   │   ├── vectorstore_factory.py  # decide FAISS ou Chroma
│   │   ├── chroma_manager.py
│   │   └── faiss_manager.py
│   │
│   ├── database/
│   │   ├── db_connection.py
│   │   └── query_executor.py
│   │
│   └── embeddings/
│       ├── embedding_factory.py
│       └── embedding_client.py
│
├── domain/                        # Schemas Pydantic
│   ├── chat_models.py
│   ├── router_models.py
│   └── sql_models.py
│
└── utils/
    └── helpers.py
