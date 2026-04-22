# High-Level Design (HLD): RAG-Based Customer Support Assistant

## 1. System Overview
### Problem Definition
Customer support teams often handle repetitive queries that could be answered using existing documentation. However, static FAQs are often insufficient, and searching through large PDF manuals is time-consuming for both customers and support agents.

### Scope
The system is a Retrieval-Augmented Generation (RAG) assistant designed to:
- Ingest and index a PDF knowledge base.
- Retrieve relevant context based on user queries.
- Generate accurate, context-aware responses using a Large Language Model (LLM).
- Manage complex control logic (retrieval, generation, and escalation) using a stateful graph workflow.
- Escalate low-confidence queries to a human support channel.

---

## 2. Architecture Diagram

![System Architecture Diagram](assets/architecture.png)

---

## 3. Component Description

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Document Loader** | `PyPDFLoader` | Extracts text and metadata from PDF files. |
| **Chunking Strategy** | `RecursiveCharacterTextSplitter` | Breaks documents into 1000-character chunks with 200-character overlap to maintain context. |
| **Embedding Model** | `all-MiniLM-L6-v2` | A lightweight HuggingFace model used to convert text chunks into numerical vectors. |
| **Vector Store** | `ChromaDB` | A high-performance, local vector database for storing and searching embeddings. |
| **Retriever** | `VectorStoreRetriever` | Searches ChromaDB for the Top-3 most relevant chunks using cosine similarity. |
| **LLM** | `Llama-3.3-70b-versatile` | Hosted on Groq for ultra-low latency inference. |
| **Workflow Engine** | `LangGraph` | Manages the state and transition logic between retrieval, generation, and escalation. |
| **HITL Module** | `human_escalation` | Simulates escalation by flagging low-confidence queries for human review. |

---

## 4. Data Flow
1. **Ingestion**: A PDF is loaded, chunked, and embedded into ChromaDB.
2. **Query**: The user submits a question via the FastAPI `/query` endpoint.
3. **Retrieval**: The `retrieve` node fetches the Top-3 relevant document snippets.
4. **Generation**: The `generate` node passes the context and question to Llama 3.3.
5. **Routing**: The system evaluates confidence based on document presence:
    - If documents are found, it generates an answer.
    - If confidence is low, it routes to the `human` node.
6. **Output**: The user receives either a specific answer or an escalation notification.

---

## 5. Technology Choices
- **ChromaDB**: Chosen for its simplicity and local persistence, making it ideal for a self-contained support bot.
- **LangGraph**: Used instead of a linear chain to allow for cycles, conditional routing, and state management (essential for HITL).
- **Groq/Llama 3.3**: Groq provides near-instant response times, which is critical for customer satisfaction in support scenarios.

---

## 6. Scalability Considerations
- **Indexing**: For larger document sets, the ingestion can be moved to an asynchronous background worker (e.g., Celery).
- **Latency**: Using Groq minimizes LLM latency; embedding retrieval is optimized by ChromaDB's indexing.
- **Concurrency**: FastAPI's asynchronous nature allows handling multiple user queries simultaneously.
