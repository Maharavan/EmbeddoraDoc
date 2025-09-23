import json
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from pathlib import Path
import streamlit as st
def load_pdf(file_path):
    return PyPDFLoader(file_path).load()

def load_json(file_path):
    
    with open(file_path,'r') as f:
        data = json.load(f)
    
    if isinstance(data,list):
        doc = [ Document(page_content=json.dumps(item,indent=2)) for item in data]
    else:
        doc = [ Document(page_content=json.dumps(data,indent=2))]

    return doc

def load_text(file_path):
    return TextLoader(file_path).load()

def file_format_wrapper(func):
    def wrap(file_path):
        get_ext = Path(file_path).suffix.lower()
        if get_ext == '.pdf':
            document = load_pdf(file_path)
        elif get_ext == '.json':
            document = load_json(file_path)
        elif get_ext in ['.txt']:
            document = load_text(file_path)
        return func(document)
    return wrap

@file_format_wrapper
def load_file(document):
    for doc in document:
        print(type(doc))
        if doc.metadata is None:
            doc.metadata = {}
        doc.metadata["session_id"] = st.session_state.current_session
    return document