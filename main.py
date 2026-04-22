from backend.ingestion.pdf_loader import load_pdf
from backend.ingestion.chunker import chunk_documents
from backend.vectorstore.chroma_store import create_vector_store

docs = load_pdf("data/support.pdf")

chunks = chunk_documents(docs)

create_vector_store(chunks)

print("Knowledge base indexed successfully.")