# 🏥 Medical RAG Chatbot

An **Enterprise Medical RAG (Retrieval-Augmented Generation) Chatbot** built with **Python, LangChain, OpenAI, FAISS, and Streamlit**.

The chatbot answers medical questions by retrieving information from multiple medical PDF documents instead of relying only on the language model's pretrained knowledge.

---

## 🚀 Features

* 📚 Multi-PDF Medical Knowledge Base
* 🔎 Semantic Search using OpenAI Embeddings
* 🧠 Retrieval-Augmented Generation (RAG)
* 🤖 AI-powered Medical Question Answering
* 📄 Supports Multiple Medical Documents
* 💬 Interactive Streamlit Chat Interface
* ⚡ FAISS Vector Database for Fast Retrieval
* 🔒 Environment Variable Support using `.env`
* ☁️ Ready for Streamlit Cloud Deployment

---

## 🛠️ Tech Stack

* Python
* OpenAI API
* LangChain
* FAISS
* Streamlit
* PyPDF
* OpenAI Embeddings
* Vector Database
* Retrieval-Augmented Generation (RAG)

---

## 📂 Project Structure

```text
Medical-RAG-Chatbot
│
├── app.py
├── ingest.py
├── rag.py
├── prompts.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── data/
│   ├── cancer.pdf
│   ├── Diabetes.pdf
│   ├── asthma.pdf
│   ├── kidney.pdf
│   ├── liver.pdf
│   ├── malaria.pdf
│   ├── dengue.pdf
│   ├── arthritis.pdf
│   ├── obesity.pdf
│   ├── Hypertension.pdf
│   ├── High-Blood-Pressure.pdf
│   ├── Sleep-Disorders.pdf
│   ├── heart_attack_signs.pdf
│   └── Thyroid.pdf
│
├── vectorstore/
│
└── utils/
    └── pdf_loader.py
```

---

## 📖 Medical Knowledge Base

The chatbot searches across multiple medical documents, including:

* Cancer
* Diabetes
* Hypertension
* High Blood Pressure
* Kidney Disease
* Liver Disease
* Asthma
* Thyroid Disorders
* Heart Attack Signs
* Malaria
* Dengue
* Arthritis
* Obesity
* Sleep Disorders

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/thirupathi3333/Medical-RAG-Chatbot.git
```

Go to the project folder:

```bash
cd Medical-RAG-Chatbot
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```text
OPENAI_API_KEY=your_openai_api_key
```

---

## 📥 Build the Vector Database

Run:

```bash
python ingest.py
```

This will:

* Load all PDFs
* Split documents into chunks
* Generate OpenAI embeddings
* Create a FAISS vector database

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 💬 Example Questions

* What are the symptoms of diabetes?
* Explain hypertension.
* What causes liver disease?
* What are the warning signs of a heart attack?
* How is kidney disease diagnosed?
* What are the symptoms of thyroid disorders?
* Explain dengue fever.
* What treatments are available for asthma?

---

## 🧠 How It Works

1. Medical PDFs are loaded from the `data/` folder.
2. Documents are split into smaller chunks.
3. OpenAI generates embeddings for each chunk.
4. FAISS stores the embeddings in a vector database.
5. User asks a question.
6. FAISS retrieves the most relevant document chunks.
7. GPT-4o Mini generates an answer using the retrieved context.
8. The chatbot displays the answer along with the source documents.

---

## 📊 Project Workflow

```text
Medical PDFs
       │
       ▼
PDF Loader
       │
       ▼
Text Chunking
       │
       ▼
OpenAI Embeddings
       │
       ▼
FAISS Vector Database
       │
       ▼
User Question
       │
       ▼
Similarity Search
       │
       ▼
Relevant Context
       │
       ▼
GPT-4o Mini
       │
       ▼
Medical Answer + Sources
```

---

## 📸 Application Preview

* 🏥 Interactive Streamlit Interface
* 💬 Chat-Based Medical Question Answering
* 📚 Source-Based Responses
* ⚡ Fast Semantic Search

---

## 🎯 Future Improvements

* PDF Upload from UI
* Conversation Memory
* Source Citations with Page Numbers
* Chat History Export
* FastAPI Backend
* Docker Support
* Multi-Agent Medical Assistant
* Medical Report Generation
* Voice Input Support

---

## 👨‍💻 Author

**M. Thirupathi**

MBA in Business Analytics | AI Engineer Aspirant

GitHub: https://github.com/thirupathi3333

---

## ⭐ If you like this project

Please consider giving it a **Star ⭐** on GitHub.
