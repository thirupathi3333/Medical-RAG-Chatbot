from dotenv import load_dotenv

load_dotenv()

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from utils.pdf_loader import load_all_pdfs

print("=" * 60)
print("🏥 MEDICAL RAG INGESTION STARTED")
print("=" * 60)

documents = load_all_pdfs("data")

print(f"\nTotal PDF Pages Loaded : {len(documents)}")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)

chunks = splitter.split_documents(documents)

print(f"Total Chunks Created : {len(chunks)}")

print("\nGenerating OpenAI Embeddings...")

embeddings = OpenAIEmbeddings()

vector_db = FAISS.from_documents(
    chunks,
    embeddings
)

vector_db.save_local("vectorstore")

print("\n✅ Vector Database Saved Successfully!")

print("=" * 60)
print("🎉 INGESTION COMPLETED")
print("=" * 60)