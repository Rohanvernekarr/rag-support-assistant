import os
from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_answer(context, question):

    prompt = f"""
You are a customer support assistant.

Use the provided context to answer the question.

Context:
{context}

Question:
{question}
"""

    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role":"user","content":prompt}
        ],
        temperature=0
    )

    return completion.choices[0].message.content