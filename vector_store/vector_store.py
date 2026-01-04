"""Module for creating and saving a hybrid vector database using FAISS and BM25."""
import os
import pickle
import streamlit as st
from rank_bm25 import BM25Okapi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from openai import AuthenticationError, RateLimitError

def create_and_save_vector_db(file_content, index_path="faiss_index"):
    """
    Docstring for create_and_save_vector_db
    
    :param file_content: Extracted content from the file
    :param index_path: FAISS index save path
    """
    api_key = st.session_state.OPENAI_API_KEY
    if not api_key:
        st.error("Please set OPENAI_API_KEY")
        return
    try:
        embeddings  = OpenAIEmbeddings()
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(file_content)

        vector_store = FAISS.from_documents(chunks, embeddings)
        vector_store.save_local(index_path)

        tokenized_docs = [c.page_content.split() for c in chunks]
        bm25 = BM25Okapi(tokenized_docs)

        with open("bm25_store.pkl", "wb") as f:
            pickle.dump({"chunks": chunks, "bm25": bm25}, f)
    except AuthenticationError:
        st.error("❌ Invalid OpenAI API key. Please check and try again.")
    except RateLimitError:
        st.error("⚠️ OpenAI rate limit reached. Please try again later.")
    except Exception as e:
        st.error("❌ Failed to create vector database")
