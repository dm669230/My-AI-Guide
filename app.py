import streamlit as st
import tempfile
import os

from embedder import create_chroma_collection, get_retriever
from loader import load_all_documents
from chunker import split_text
from rag_chain import create_rag_chain, ask_question

# --- Page setup ---
st.set_page_config(page_title="AI RAG Assistant", layout="wide")
st.title("🧠 AI RAG Chat with Your Documents")

# --- Session State Setup ---
if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

if "retriever" not in st.session_state:
    st.session_state.retriever = None

if "uploaded_file_name" not in st.session_state:
    st.session_state.uploaded_file_name = None

# --- File Upload ---
uploaded_file = st.file_uploader("📁 Upload a PDF, DOCX, or TXT file", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    # Save uploaded file with original filename
    original_filename = uploaded_file.name
    upload_dir = "uploaded_files"
    os.makedirs(upload_dir, exist_ok=True)  # Ensure folder exists

    tmp_path = os.path.join(upload_dir, original_filename)

    with open(tmp_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success(f"✅ File '{original_filename}' uploaded and saved successfully!")

    # Load, Split, Embed
    documents = load_all_documents(tmp_path)
    chunks = split_text(documents[original_filename])

    # Generate collection name
    collection_name = os.path.splitext(original_filename)[0].replace(" ", "_").lower()

    # Create and store in Chroma
    create_chroma_collection(chunks, collection_name=collection_name)

    # Store in session state
    st.session_state.uploaded_file_name = collection_name
    st.session_state.rag_chain = None
    st.session_state.retriever = None

    st.success("✅ Document processed and stored in vector database.")



# --- Question Input ---
question = st.text_input("💬 Ask a question from your uploaded document:")

if st.button("Submit Question") and question:
    if not st.session_state.uploaded_file_name:
        st.warning("⚠️ Please upload and process a document first.")
    else:
        # Create retriever only once
        if st.session_state.retriever is None:
            retriever_list = get_retriever(collection_name=collection_name)
            st.session_state.retriever = retriever_list[collection_name]['retriever']  # Use first retriever

        # Create RAG chain only once
        if st.session_state.rag_chain is None:
            st.session_state.rag_chain = create_rag_chain(st.session_state.retriever)

        # Ask question
        answer = ask_question(st.session_state.rag_chain, question)

        # Show answer
        st.markdown("### 🤖 Answer:")
        st.write(answer)

