from langchain_groq import ChatGroq

def get_llm(temperature=0.2):
    return ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=temperature,
        max_tokens=3000
    )