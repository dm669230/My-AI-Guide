# 🧠 Personal Document Q&A Assistant (LangChain + RAG + Vector DB)

A beginner-friendly project that turns your personal documents (PDFs, DOCX, TXT) into a smart assistant using **LangChain**, **OpenAI**, and **Chroma VectorDB**. Just upload files and start asking questions — it will find the right answers from your files using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- 📄 Upload and read documents (PDF, DOCX, TXT)
- 🔍 Ask questions about your uploaded files
- 🧠 Retrieval-Augmented Generation (RAG) using LangChain
- 🔧 Optional tools like Calculator and Web Search
- 💬 Clean Streamlit-based web interface
- ⚡ Powered by OpenAI LLMs + VectorDB (Chroma)

---

## 🧰 Tech Stack

| Component     | Technology Used           |
|---------------|----------------------------|
| LLM           | OpenAI GPT-3.5 / GPT-4     |
| Framework     | LangChain                  |
| Embeddings    | OpenAI Embeddings          |
| Vector DB     | ChromaDB                   |
| File Parsing  | pdfminer, python-docx, unstructured |
| Frontend      | Streamlit                  |
| Environment   | Python 3.8+                |

---

personal-assistant/
│
├── app.py # Main Streamlit interface
├── loader.py # File loader for PDFs, DOCX, TXT
├── chunker.py # Chunking text using LangChain
├── embedder.py # Embedding + storing in Vector DB
├── rag_chain.py # Retrieval + LLM response logic
├── tools.py # Custom tools (calculator etc.)
├── config.py # Global config settings
├── .env # Secret keys (not committed)
├── requirements.txt # All dependencies
└── data/
└── my_docs/ # Folder for uploaded documents

---

### 1. Clone the Repository

```
bash
git clone https://github.com/your-username/personal-assistant.git
cd personal-assistant
```
### 2. Create Virtual Environment
```
# python -m venv venv
for windows ---
> venv\Scripst\activate
for Linux ---
> source venv/bin/activate  # On Windows: venv\Scripts\activate
# pip install -r requirements.txt

```
### 3 .env structure
```
Create a file .env in the root with:
DEEPSEEK_API_KEY=
DOCS_DIRECTORY=data\my_docs
DEEPSEEK_API_BASE=https://api.deepseek.com/v1

```
### 4 Run the streamlit application
```
# streamlit run app.py
```


## 🗂️ Project Structure

