def route_decision(state):

    confidence = state["confidence"]

    if confidence < 0.5:
        return "human"

    return "output"