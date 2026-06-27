from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from prompts import SYSTEM_PROMPT

client = OpenAI()


# Load Vector Database
embeddings = OpenAIEmbeddings()

vector_db = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)


def ask_question(question):

    docs = vector_db.similarity_search(
        question,
        k=4
    )

    context = ""

    sources = []

    for doc in docs:

        context += doc.page_content + "\n\n"

        source = doc.metadata.get("source", "Unknown")

        page = doc.metadata.get("page", "Unknown")

        sources.append(f"{source} (Page {page+1})")

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"""
Medical Context:

{context}

Question:

{question}
"""
            }
        ],

        temperature=0.2
    )

    answer = response.choices[0].message.content

    return answer, list(set(sources))