from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.schema import Document
from typing import List

def create_chroma_collection(chunks: List[str], collection_name: str):
    """
    Creates a Chroma vector store collection from a list of text chunks.

    Args:
        chunks (List[str]): List of text chunks.
        collection_name (str): Name of the Chroma collection to create.

    Returns:
        Chroma: A Chroma vector store object.
    """
    # Initialize sentence transformer embedding model
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    # Convert chunks into Document objects (required by LangChain)
    documents = [Document(page_content=chunk) for chunk in chunks]

    # Create and return the Chroma vector store
    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embedding_function,
        collection_name=collection_name
    )

    return vectorstore
