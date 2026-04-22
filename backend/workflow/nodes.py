from backend.retrieval.retriever import get_retriever
from backend.llm.groq_llm import generate_answer

retriever = get_retriever()

def retrieve_node(state):

    question = state["question"]

    docs = retriever.get_relevant_documents(question)

    return {
        "documents": docs
    }


def generate_node(state):

    question = state["question"]
    docs = state["documents"]

    context = "\n".join([doc.page_content for doc in docs])

    answer = generate_answer(context, question)

    confidence = 0.9 if docs else 0.3

    return {
        "answer": answer,
        "confidence": confidence
    }