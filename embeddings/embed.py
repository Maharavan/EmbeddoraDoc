from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAI, ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()
def embed_vector(file_content,query):
    
    textsplitter = RecursiveCharacterTextSplitter(
        chunk_size=250,
        chunk_overlap = 0,
        length_function = len
    )

    chunks = textsplitter.split_text(file_content)
    embeddings  = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(chunks,embeddings)

    #vector_store.save_local('faiss')
    
    #docs_and_scores = vector_store.similarity_search_with_relevance_scores(query)
    retriever = vector_store.as_retriever()
    llm = ChatOpenAI(model="gpt-4o-mini",temperature=0.5)
    system_prompt = (
    """
    You are Embeddoradoc, an intelligent assistant specialized in analyzing data stored in a vector database.  
    Your role is to:
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
    
    

    prompt = PromptTemplate(
        template=system_prompt,input_variables=["context","query"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm = llm,
        retriever = retriever,
        chain_type_kwargs={"prompt":prompt}
    )

    response = qa_chain.run(query)
    print(response)