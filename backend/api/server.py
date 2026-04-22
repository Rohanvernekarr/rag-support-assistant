from fastapi import FastAPI
from backend.workflow.graph import build_graph

app = FastAPI()

graph = build_graph()

@app.post("/query")
def query_system(question: str):

    result = graph.invoke({
        "question": question
    })

    return {
        "answer": result["answer"]
    }