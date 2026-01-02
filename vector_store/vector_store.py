"""Module for creating and saving a hybrid vector database using FAISS and BM25."""
import pickle
from rank_bm25 import BM25Okapi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

def create_and_save_vector_db(file_content, index_path="faiss_index"):
    """
    Docstring for create_and_save_vector_db
    
    :param file_content: Extracted content from the file
    :param index_path: FAISS index save path
    :return: Confirmation message with paths to saved vector store and BM25 store
    """
    embeddings  = OpenAIEmbeddings()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(file_content)

    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local(index_path)

    tokenized_docs = [c.page_content.split() for c in chunks]
    bm25 = BM25Okapi(tokenized_docs)

    with open("bm25_store.pkl", "wb") as f:
        pickle.dump({"chunks": chunks, "bm25": bm25}, f)

    return f"Hybrid DB saved → Vector:{index_path} + BM25:bm25_store.pkl"
