from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


def create_and_save_vector_db(file_content,index_path="faiss_index"):
    embeddings  = OpenAIEmbeddings()

    textsplitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap = 50,
        length_function = len
    )

    chunks = textsplitter.split_documents(file_content)
    vector_store = FAISS.from_documents(chunks,embeddings)
    
    vector_store.save_local(index_path)