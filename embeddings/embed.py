import pickle
from rank_bm25 import BM25Okapi
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI,OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def embed_vector(query,index_path='faiss_index'):

    embeddings = OpenAIEmbeddings()
    llm = ChatOpenAI(model="gpt-4o-mini",temperature=0)

    vector_store = FAISS.load_local(index_path,embeddings,allow_dangerous_deserialization=True)
    docs_vector = vector_store.similarity_search(query, k=5)

    print(f"FAISS hits: {len(docs_vector)}")

    try:
        with open("bm25_store.pkl","rb") as f:
            data = pickle.load(f)
        chunks = data["chunks"]
        bm25:BM25Okapi = data["bm25"]
        docs_bm25_raw = bm25.get_top_n(query.split(), chunks, n=5)
        print(f"BM25 hits: {len(docs_bm25_raw)}")
    except FileNotFoundError:
        print("BM25 store not found — run embedding first.")
        docs_bm25_raw = []

    combined_docs = list({d.page_content for d in docs_vector} | {c.page_content for c in docs_bm25_raw})
    context = "\n---\n".join(combined_docs)

    if not combined_docs:
        return "No results from FAISS or BM25 — reprocess documents."

    system_prompt = ("""
    You are Embeddoradoc, a document-based reasoning assistant.

    You must:
    - Read the context carefully.
    - Understand the user's question.
    - Know the content format is text/pdf/json documents.
    - Extract information relevant to the user's question.
    - If related information exists, answer using it in your own words.
    - If information truly does NOT exist, reply exactly: "Not found in embeddings."

    First think step-by-step inside your reasoning (not visible to user).
    Then produce the final answer clearly.

    -----------------
    Context:
    {context}
    -----------------

    Question:
    {question}

    Final Answer:
    """)


    prompt = PromptTemplate.from_template(system_prompt)
    chain = prompt | llm | StrOutputParser()

    return chain.invoke({"context":context,"question":query})
