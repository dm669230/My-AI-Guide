from pdfminer.high_level import extract_text
from docx import Document
import os
import traceback
from chunker import split_text
from embedder import create_chroma_collection, get_retriever
from rag_chain import ask_question, create_rag_chain
from dotenv import load_dotenv


load_dotenv()
docs_derectory = os.getenv("DOCS_DIRECTORY")

def load_all_documents(path: str = docs_derectory):
    """
    Load content from a single file or all files in a directory.

    Args:
        path (str): File path or directory path.

    Returns:
        dict: {filename: text}
    """
    try:
        documents = {}

        if os.path.isfile(path):  # Single file
            filename = os.path.basename(path)
            print("uploaded_file_name = ", filename)
            if filename.endswith(".pdf"):
                documents[filename] = extract_text_from_pdf(path)
            elif filename.endswith(".docx"):
                documents[filename] = load_docx(path)
            elif filename.endswith(".txt"):
                documents[filename] = load_txt(path)

        elif os.path.isdir(path):  # Directory
            for filename in os.listdir(path):
                file_path = os.path.join(path, filename)
                if filename.endswith(".pdf"):
                    documents[filename] = extract_text_from_pdf(file_path)
                elif filename.endswith(".docx"):
                    documents[filename] = load_docx(file_path)
                elif filename.endswith(".txt"):
                    documents[filename] = load_txt(file_path)

        else:
            raise ValueError("Invalid path")

        return documents

    except Exception as e:
        traceback.print_exc()
        return f"Document Error due to: {e}"


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

def load_data_in_vector(document = None):
    if not document:
        document_list = load_all_documents()
    else:
        document_list = [{"new_document": document}]
    collection_dict = {}
    print("document_list", document_list)
    for collection_name, data in document_list.items():
        collection = collection_name.replace(" ", "_").lower().split(".")[0]
        chunks = split_text(data)
        vector_store = create_chroma_collection(chunks=chunks,collection_name=collection)
        collection_dict[collection] = vector_store
    return collection_dict

# collection_vector_dict= load_data_in_vector()
# print(collection_vector_dict)

# collection_name = list(collection_vector_dict.keys())[0]
# my_vector_data = get_retriever(collection_name)
# my_vector_data = {
#     "my_collection": {
#         "vectorstore": vectorstore,
#         "retriever": vectorstore.as_retriever()
#     }
# }
def get_similarity_search(my_vector_data, query = "list vs tuple"):
    result = []
    for collection, vector_Data in my_vector_data.items():
        vector_search = vector_Data["vectorstore"].similarity_search(query, k=5)
        result.extend(vector_search)
    # print(search)
    return result

# result = get_similarity_search(my_vector_data, query = "list vs tuple")
# # print("result ====>", result)
# for i, search in enumerate(result):
#     print(f"============> {i}-{search}")

# rag_chain = create_rag_chain(my_vector_data[collection_name]["retriever"])

# print(rag_chain)
# reply = ask_question(chain=rag_chain,query="what is the deffrence between list and tuple ?")
# print(f"reply from llm : {reply}")
