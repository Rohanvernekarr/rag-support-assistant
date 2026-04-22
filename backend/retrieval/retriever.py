from langchain_chroma import Chroma
from backend.ingestion.embedder import get_embedding_model

def get_retriever():

    embeddings = get_embedding_model()

    vectorstore = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embeddings
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k":3}
    )

    return retriever