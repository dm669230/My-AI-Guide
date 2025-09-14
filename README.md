# 🧠 Personal Document Q&A Assistant (LangChain + RAG + Vector DB)

A beginner-friendly project that turns your personal documents (PDFs, DOCX, TXT) into a smart assistant using **LangChain**, **OpenAI**, and **Chroma VectorDB**. Just upload files and start asking questions — it will find the right answers from your documents using **Retrieval-Augmented Generation (RAG)**.

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

| Component     | Technology Used                    |
|---------------|-------------------------------------|
| LLM           | OpenAI GPT-3.5 / GPT-4             |
| Framework     | LangChain                          |
| Embeddings    | OpenAI Embeddings                  |
| Vector DB     | ChromaDB                           |
| File Parsing  | pdfminer, python-docx, unstructured|
| Frontend      | Streamlit                          |
| Environment   | Python 3.8+                        |

---

## 📂 Project Structure


personal-assistant/
│
├── app.py # Main Streamlit interface
├── loader.py # File loader for PDFs, DOCX, TXT
├── chunker.py # Text chunking logic
├── embedder.py # Embedding & storing in ChromaDB
├── rag_chain.py # RAG logic: retrieval + LLM response
├── tools.py # Custom tools (calculator, etc.)
├── config.py # Global constants and config settings
├── .env # API keys and other environment vars
├── requirements.txt # Required Python packages
└── data/
└── my_docs/ # Folder containing your uploaded files


## 🧑‍💻 Getting Started

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/your-username/personal-assistant.git
cd personal-assistant

🔹 2. Set Up Virtual Environment
# Create virtual environment
python -m venv venv

# Activate:
# On Windows
venv\Scripts\activate

# On Linux/macOS
source venv/bin/activate

🔹 3. Install Requirements
pip install -r requirements.txt

🔹 4. Set Up Environment Variables

Create a .env file in the root of the project with one of the following structures:

🧠 For DeepSeek API
DEEPSEEK_API_KEY=your-deepseek-api-key
DEEPSEEK_API_BASE=https://api.deepseek.com/v1
DOCS_DIRECTORY=data/my_docs

🤖 For OpenAI API
OPENAI_API_KEY=your-openai-api-key
DOCS_DIRECTORY=data/my_docs

🔹 5. Run the Streamlit App
streamlit run app.py


Then open the browser link (usually http://localhost:8501)

⚙️ How It Works

Upload documents → PDF, DOCX, TXT

Extract and chunk text → Break into manageable parts

Generate embeddings → Using DeepSeek/OpenAI

Store in Chroma vector DB → For similarity-based search

Ask questions → Query is matched with relevant content

LLM responds → Answer generated with document context

🛠 Tools Integration (Optional)

Inside tools.py, you can add utility tools that the assistant can call when needed:

Tool	Purpose
Calculator	Solve math queries
Summarizer	Summarize large text content
SearchTool	Pull info from the web (optional)

Tools can be registered with LangChain’s Tool API.

📦 requirements.txt
langchain
openai
chromadb
streamlit
tiktoken
unstructured
pdfminer.six
python-docx
python-dotenv

✅ To-Do (Optional Improvements)

 Add chat history and memory support

 Dockerize the entire application

 Support multiple users with sessions

 Improve UI styling with Streamlit themes

 Add option to switch between LLM providers (DeepSeek/OpenAI/Ollama)

🧑 Author

Vaibhav Srivastava
Python Developer | FastAPI | LLMs | Backend
📧 vaibhav.srivastava405@gmail.com

📍 Mumbai, India
