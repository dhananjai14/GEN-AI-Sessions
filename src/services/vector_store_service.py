from services.llm_service import embeddings_model as embedding
from langchain_chroma import Chroma
from typing import List
import chromadb
from langchain_chroma import Chroma
from services.llm_service import embeddings_model as embedding


def create_vector_store(collection_name:str) -> Chroma:
    vector_store = Chroma(
    collection_name=collection_name,
    embedding_function=embedding,
    persist_directory="./chroma_langchain_db",
        )
    return vector_store
    

def add_documents_vectorDB(collection_name: str, documents:List ):
    client = chromadb.PersistentClient(path="./chroma_langchain_db")
    vector_store_from_client = Chroma(
    client=client,
    collection_name=collection_name,
    embedding_function=embedding,)

    vector_store_from_client.add_documents(documents)


def get_retriever(vectro_store_clinet):
    retriever = vectro_store_clinet.as_retriever(
    search_type="mmr", search_kwargs={"k": 2, "fetch_k": 5})

    return retriever

def wrapper_vector_store_service(collection_name, documents, **kwargs):
    vector_store_client = create_vector_store(collection_name)
    add_documents_vectorDB(documents)
    retriever = get_retriever(vector_store_client)
    query = kwargs.get("query", "")
    results = retriever.invoke(query)
    return results



