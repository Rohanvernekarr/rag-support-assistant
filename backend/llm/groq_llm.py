import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_answer(context, question):

    prompt = f"""
You are a customer support assistant.

Use the provided context to answer the question. If the context is not sufficient to answer the question, strictly say: "I don't know the answer based on the provided context."

Context:
{context}

Question:
{question}
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"user","content":prompt}
        ],
        temperature=0
    )

    return completion.choices[0].message.content