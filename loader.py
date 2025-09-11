from pdfminer.high_level import extract_text
from docx import Document
import os
import traceback
from chunker import split_text
from embedder import create_chroma_collection

def load_documents(directory_path: str = "data\my_docs") -> dict:
    """
    Loads text content from all PDF, DOCX, and TXT files in a directory.

    Args:
        directory_path (str): Path to the directory.

    Returns:
        dict: Dictionary with filename as key and extracted text as value.
    """
    try:
        documents = {}
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if filename.lower().endswith(".pdf"):
                documents[filename] = extract_text_from_pdf(file_path)
            elif filename.lower().endswith(".docx"):
                documents[filename] = load_docx(file_path)
            elif filename.lower().endswith(".txt"):
                documents[filename] = load_txt(file_path)
        return documents
    except Exception as e:
        traceback.print_exc()
        return f"Error due to : {e}"

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts text from a PDF file.

    Args:
        pdf_path (str): The full path to the PDF file.

    Returns:
        str: The extracted text from the PDF.
    """
    try:
        text = extract_text(pdf_path)
        return text
    except Exception as e:
        return f"Error extracting text: {e}"


def load_docx(file_path: str) -> str:
    """
    Extracts text from a .docx file.

    Args:
        file_path (str): Path to the .docx file.

    Returns:
        str: Extracted text.
    """
    try:
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        return f"Error reading DOCX: {e}"
    

def load_txt(file_path: str) -> str:
    """
    Loads text from a .txt file.

    Args:
        file_path (str): Path to the .txt file.

    Returns:
        str: File content.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading TXT: {e}"

text_dict = load_documents()

text = "\n".join(text_dict.values())
chunks = split_text(text)

# print(chunks)
vector_srore = create_chroma_collection(chunks=chunks,collection_name="My_study_material")

print(vector_srore)