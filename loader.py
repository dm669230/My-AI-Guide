from pdfminer.high_level import extract_text
from docx import Document
import os
import traceback
from chunker import split_text
from embedder import create_chroma_collection, get_retriever
from dotenv import load_dotenv


load_dotenv()
docs_derectory = os.getenv("DOCS_DIRECTORY")

def load_documents(directory_path: str = docs_derectory):
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

def load_data_in_vector():
    document_list = load_documents()
    for collection_name, data in document_list.items():
        # text = "\n".join(text_dict.values())
        collection = collection_name.replace(" ", "_").lower().split(".")[0]
        print("collection name ====> ", collection)
        # quit()
        chunks = split_text(data)
        # print(chunks)
        vector_store = create_chroma_collection(chunks=chunks,collection_name=collection)
    return vector_store

vector_store = load_data_in_vector()
print(vector_store)

# my_vector = get_retriever(collection_name="all_interview_questions_and_answers")
my_vector_data = get_retriever()
def get_similarity_search(my_vector_data, query = "list vs tuple"):
    print(my_vector_data)
    result = []
    for vector_Data in my_vector_data:
        vector_search = vector_Data.similarity_search(query, k=5)
        result.extend(vector_search)
    # print(search)
    return result

result = get_similarity_search(my_vector_data,query = "list vs tuple")
# print("result ====>", result)
for i, search in enumerate(result):
    print(f"============> {i}")