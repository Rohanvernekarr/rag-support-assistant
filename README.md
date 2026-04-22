# RAG-Based Customer Support Assistant

Welcome to the **RAG-Based Customer Support Assistant**! This project was built to bridge the gap between static support manuals and real-time user needs using state-of-the-art AI.

## The Problem
Every day, customer support teams are flooded with the same repetitive questions. Users, on the other hand, often struggle to find answers buried in long, complex PDF manuals. This leads to:
- **Slower response times** for customers.
- **Agent burnout** from answering the same "How-to" questions.
- **Inaccurate guesses** when users try to find info themselves.

## The Solution
I built an intelligent **Retrieval-Augmented Generation (RAG)** system that acts as a 24/7 first-line support agent. 

### How it works:
1. **Knowledge Ingestion**: The system reads your official support PDFs and breaks them into smart "chunks."
2. **Brainy Search**: When a user asks a question, the system searches those chunks for the exact answer using semantic embeddings.
3. **AI-Powered Answers**: It uses a Large Language Model (Llama 3 via Groq) to write a natural, helpful response based *only* on your documents.
4. **Human Safety Net (HITL)**: If the AI isn't 100% sure about an answer, it doesn't guess. Instead, it automatically flags the query for a human agent to review.

## Key Features
- **Lightning Fast**: Powered by **Groq** for near-instant responses.
- **Always Grounded**: No hallucinations! If it's not in the PDF, the bot knows to ask for help.
- **Smart Workflows**: Built with **LangGraph** to handle complex logic and decision-making.
- **Scalable Storage**: Uses **ChromaDB** to manage and retrieve thousands of document snippets efficiently.

## 🎓 Insights
Building this project gave me deep insights into the future of AI-driven support:
- **RAG is a Game Changer**: I learned that the key to useful AI is not just the model's size, but the **quality of the context** I provide it. RAG transforms a general AI into a domain expert.
- **Stateful Control with LangGraph**: Moving beyond simple linear "chains," I understood how to manage AI logic as a **state machine**. This allows for loops, conditions, and complex decision-making that feels robust.
- **The Value of the Safety Net**: The **Human-in-the-Loop** component taught me that the most reliable AI systems are the ones that know their own limits and know exactly when to escalate to a human.
- **Performance & Latency**: Working with **Groq** showed me that sub-second response times are critical for maintaining a conversational flow in customer support.

## Tech Stack
- **Framework**: FastAPI
- **AI Orchestration**: LangChain & LangGraph
- **Vector Database**: ChromaDB
- **LLM**: Llama 3.3 (via Groq API)
- **Embeddings**: HuggingFace (MiniLM)

## Getting Started

### 1. Setup Environment
Clone the repo and install the dependencies:
```bash
pip install -r requirements.txt
```

### 2. Configure API Keys
Create a `.env` file and add your Groq API Key:
```env
GROQ_API_KEY=your_key_here
```

### 3. Run the App
Start the backend server:
```bash
uvicorn backend.api.server:app --reload
```

---
