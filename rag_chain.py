from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA, LLMChain, ConversationalRetrievalChain
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from typing import List, Union
from langchain_core.retrievers import BaseRetriever
from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()
DEEPSEE_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEE_BASE_URL = os.getenv("DEEPSEEK_API_BASE")

def create_rag_chain(retriever):
    """
    Create a Conversational RAG chain using DeepSeek-compatible LLM.
    """

    llm = ChatOpenAI(
        temperature=0,
        model="deepseek-chat",  # Optional: use DeepSeek's model name if required
        base_url=DEEPSEE_BASE_URL,
        api_key=DEEPSEE_API_KEY
    )

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
        You are an AI assistant with access to the following context:

        {context}

        Answer the following question conversationally:

        Question: {question}
        """
            )

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        combine_docs_chain_kwargs={"prompt": prompt}
    )

    return chain


def ask_question(chain, query):
    """
    Asks a question using the provided chain.

    Args:
        chain: The RAG chain created by `create_rag_chain`.
        query: The user question as a string.

    Returns:
        str: The generated answer.
    """
    response = chain.invoke({"question": query})
    return response["answer"]



def create_multi_collection_rag_chain(retrievers: Union[BaseRetriever, List[BaseRetriever]]):
    """
    Create a RAG chain that uses all retrievers (collections) together.
    """
    # Ensure we have a list of retrievers
    if not isinstance(retrievers, list):
        retrievers = [retrievers]

    # Memory for conversation
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # Prompt template
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
                You are an AI assistant. Use the following context to answer the question conversationally.

                Context:
                {context}

                Question:
                {question}
                """
                )

    # LLM instance
    llm = ChatOpenAI(temperature=0, model="deepseek-chat")  # add API key/base_url if needed

    # Define a custom "retriever-like" callable for all collections
    class MultiRetriever(BaseRetriever):
        def get_relevant_documents(self, query: str):
            all_docs = []
            for retriever in retrievers:
                docs = retriever.get_relevant_documents(query)
                all_docs.extend(docs)
            return all_docs

    # Use MultiRetriever in RAG chain
    multi_retriever = MultiRetriever()
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=multi_retriever,
        memory=memory,
        combine_docs_chain_kwargs={"prompt": prompt}
    )

    return chain