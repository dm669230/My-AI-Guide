from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List

def split_text(text: str, chunk_size: int = 300, chunk_overlap: int = 50) :
    """
    Splits the input text into chunks using LangChain's RecursiveCharacterTextSplitter.

    Args:
        text (str): The input text to split.
        chunk_size (int): The maximum size of each chunk.
        chunk_overlap (int): The number of overlapping characters between chunks.

    Returns:
        List[str]: A list of text chunks.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = splitter.split_text(text)
    return chunks


