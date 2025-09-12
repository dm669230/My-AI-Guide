from langchain.vectorstores import Chroma
# from langchain.embeddings import SentenceTransformerEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from typing import List
import chromadb
from chromadb.config import Settings


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
    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    # embedding_function = OpenAIEmbeddings()

    # Convert chunks into Document objects (required by LangChain)
    documents = [Document(page_content=chunk) for chunk in chunks]

    # Create and return the Chroma vector store
    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embedding_function,
        collection_name=collection_name
    )

    return vectorstore



def get_retriever(collection_name: str = None):
    """
    Get Chroma retriever(s) by collection name.
    If collection_name is provided, returns a single Chroma retriever.
    Otherwise, returns a list of retrievers for all existing collections.

    Args:
        collection_name (str): Name of the Chroma collection to load.  
                               If None, loads all available collections.

    Returns:
        Chroma or List[Chroma]: Chroma retriever instance or list of retrievers.
    """
    # Initialize embedding function
    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    all_retrievers = []
    if collection_name:
        # Load specific collection
        vectorstore = Chroma(
            collection_name=collection_name,
            embedding_function=embedding_function
        )
        all_retrievers.append(vectorstore)
        return all_retrievers

    # Load all existing collections
    client = chromadb.Client(Settings())
    all_collections = client.list_collections()

    for collection in all_collections:
        vectorstore = Chroma(
            collection_name=collection.name,
            embedding_function=embedding_function
        )
        all_retrievers.append(vectorstore)

    return all_retrievers
