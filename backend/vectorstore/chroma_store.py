from langchain.vectorstores import Chroma
from backend.ingestion.embedder import get_embedding_model

def create_vector_store(chunks):

    embeddings = get_embedding_model()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )

    vectorstore.persist()

    return vectorstore