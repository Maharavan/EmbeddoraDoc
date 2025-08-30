from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI,OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()
embeddings  = OpenAIEmbeddings()


def create_and_save_vector_db(file_content,index_path="faiss_index"):
    textsplitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap = 50,
        length_function = len
    )

    chunks = textsplitter.split_documents(file_content)
    vector_store = FAISS.from_documents(chunks,embeddings)

    vector_store.save_local(index_path)

def embed_vector(query,index_path='faiss_index'):
    system_prompt = (
    """
    You are Embeddoradoc, an intelligent assistant specialized in analyzing data stored in a vector database.  
    Your role is to
    - Understand user queries in natural language.
    - Retrieve relevant context from the vector store using embeddings.
    - Provide clear, concise, and accurate answers based on retrieved information.
    - If data is insufficient, indicate that confidently that does not exist in embeddings instead of predicting.
    
    Always keep responses user-friendly and structured when needed.

    Context : {context}
    Question : {question}
    Answer:

    """
    )

    llm = ChatOpenAI(model="gpt-4o-mini",temperature=0.5)
    vector_store = FAISS.load_local(index_path,embeddings,allow_dangerous_deserialization=True)
    retriever = vector_store.as_retriever(search_kwargs={"k":5})
    

    prompt = PromptTemplate(
        template=system_prompt,input_variables=["context","question"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm = llm,
        retriever = retriever,
        chain_type_kwargs={"prompt":prompt}
    )

    response = qa_chain.run(query)
    print(response)