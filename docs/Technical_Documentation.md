# Technical Documentation: RAG-Based Customer Support Assistant

## 1. Introduction
### What is RAG
Retrieval-Augmented Generation (RAG) is a technique used to "ground" Large Language Models (LLMs) in specific, factual data. It retrieves relevant snippets from a local knowledge base and provides them as context to the LLM.

### Why it is Needed
Standard LLMs have a "knowledge cutoff" and often hallucinate when asked about private or specific company data. RAG ensures accuracy by forcing the model to answer based on provided documents.

### Use Case Overview
This project implements a Customer Support Assistant that answers queries based on a PDF manual. It ensures customers get accurate help while escalating complex issues to human agents.

## 2. System Architecture Explanation
### Detailed Explanation of HLD
The system uses a "Decoupled Workflow" architecture. The **Ingestion Pipeline** (PDF -> Chunks -> ChromaDB) runs independently of the **Query Pipeline** (Question -> LangGraph -> Answer).

### Component Interactions
- **Document Processing**: `PyPDFLoader` extracts text.
- **Vector Storage**: `ChromaDB` stores embeddings for semantic search.
- **Workflow Orchestration**: `LangGraph` coordinates the state transition between retrieval and response generation.

## 3. Design Decisions
### Chunk Size Choice
- **Decision**: 1000 characters with 200 overlap.
- **Rationale**: Balances context retention with memory efficiency.

### Embedding Strategy
- **Decision**: `all-MiniLM-L6-v2`.
- **Rationale**: Fast local execution with 384-dimensional accuracy.

### Retrieval Approach
- **Decision**: Top-3 Cosine Similarity.
- **Rationale**: High precision retrieval for specific support instructions.

### Prompt Design Logic
- **Decision**: Zero-Shot Grounding.
- **Rationale**: Prevents hallucinations by explicitly forbidding "guessing" if context is missing.

## 4. Workflow Explanation
### LangGraph Usage
We use a stateful directed graph to manage the lifecycle of a query. This allows us to handle complex branching (like human escalation) that linear chains cannot.

### Node Responsibilities
- `retrieve`: Searches the vector database.
- `generate`: Synthesizes the final answer.
- `human`: Handles fallback/escalation.

### State Transitions
Data flows through a `GraphState` TypedDict, ensuring that each node has access to the user's question, retrieved documents, and confidence scores.

## 5. Conditional Logic
### Intent Detection
The system evaluates the retrieved documents to determine if the user's intent matches the knowledge base.

### Routing Decisions
If the confidence score (based on retrieval results) is below 0.5, the router redirects the flow to the `human` node.

## 6. HITL Implementation
### Role of Human Intervention
The Human-in-the-Loop (HITL) module acts as a safety valve. It identifies queries the LLM cannot answer reliably and marks them for human review.

### Benefits & Limitations
- **Benefits**: Eliminates incorrect answers and builds user trust.
- **Limitations**: Increases latency for complex queries requiring human input.

## 7. Challenges & Trade-offs
### Retrieval Accuracy vs Speed
Using a lightweight embedding model (`MiniLM`) provides sub-second retrieval but may miss extremely subtle semantic nuances compared to much larger, slower models.

### Chunk Size vs Context Quality
Smaller chunks are faster to retrieve but may cut off critical instructions; larger chunks provide more context but increase LLM costs.

### Cost vs Performance
By using `Groq` and `Llama 3.3`, we achieve near-GP4 performance with significantly lower latency and cost.

## 8. Testing Strategy
### Testing Approach
We utilized "Golden Query" testing, comparing system outputs against known facts in the PDF.

### Sample Queries
- "How do I reset my password?" (Expected: Specific instructions from PDF)
- "What is your return policy?" (Expected: Accurate retrieval)
- "Who won the World Cup?" (Expected: Escalation to human)

## 9. Future Enhancements
### Multi-Document Support
Expanding the vector store to handle multiple PDFs across different product lines.

### Feedback Loop
Implementing a "Thumb Up/Down" system to fine-tune the retriever.

### Memory Integration
Adding `SqliteSaver` to LangGraph to allow the bot to remember previous user interactions.

### Deployment
Containerizing the application with Docker and deploying to a cloud-based GPU provider or edge device.
