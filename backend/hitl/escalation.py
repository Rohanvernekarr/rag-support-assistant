def human_escalation(state):

    question = state["question"]

    return {
        "answer": f"This query requires human assistance. Support ticket created for: {question}"
    }