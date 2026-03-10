import json
import os
from langchain_community.embeddings import OllamaEmbeddings
from chromadb import Client

# Caminho para o arquivo de schema
SCHEMA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'docs', 'schemas', 'olist_schema.json'))

# Inicializa o modelo de embeddings Ollama
ollama_model = os.getenv("OLLAMA_EMBEDDINGS_MODEL", "llama2")
ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
embeddings = OllamaEmbeddings(model=ollama_model, base_url=ollama_url)

# Inicializa o ChromaDB
chroma_client = Client()
collection = chroma_client.get_or_create_collection(name="olist_schema")

def load_schema():
    with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def schema_to_text(table_name, columns):
    col_str = ", ".join([f"{col['name']} ({col['type']})" for col in columns])
    return f"Tabela: {table_name} | Colunas: {col_str}"

def ingest_schema():
    schema = load_schema()
    docs = []
    metadatas = []
    ids = []
    for table, columns in schema.items():
        text = schema_to_text(table, columns)
        docs.append(text)
        metadatas.append({"table": table})
        ids.append(table)
    # Gera embeddings
    vectors = embeddings.embed_documents(docs)
    # Armazena no Chroma
    collection.add(documents=docs, embeddings=vectors, metadatas=metadatas, ids=ids)
    print(f"Ingestão concluída: {len(docs)} tabelas no Chroma.")

if __name__ == "__main__":
    ingest_schema()
