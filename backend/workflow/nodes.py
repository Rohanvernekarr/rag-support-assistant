from backend.retrieval.retriever import get_retriever
from backend.llm.groq_llm import generate_answer

retriever = get_retriever()

def retrieve_node(state):

    question = state["question"]

    docs = retriever.invoke(question)

    return {
        "documents": docs
    }


def generate_node(state):

    question = state["question"]
    docs = state["documents"]

    context = "\n".join([doc.page_content for doc in docs])

    answer = generate_answer(context, question)

    # Trigger escalation if LLM cannot find answer in context
    if "I don't know" in answer or not docs:
        confidence = 0.3
    else:
        confidence = 0.9

    return {
        "answer": answer,
        "confidence": confidence
    }