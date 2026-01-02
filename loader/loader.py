"""
Module for loading different file formats into Document objects.
"""
import json
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
import streamlit as st

def load_pdf(file_path):
    """
    Docstring for load_pdf
    
    :param file_path: PDF File path
    :return: List of Document objects
    """
    return PyPDFLoader(file_path).load()

def load_json(file_path):
    """
    Docstring for load_json
    
    :param file_path: JSON File path
    :return: List of Document objects
    """
    with open(file_path,'r') as f:
        data = json.load(f)
    
    if isinstance(data,list):
        doc = [ Document(page_content=json.dumps(item,indent=2)) for item in data]
    else:
        doc = [ Document(page_content=json.dumps(data,indent=2))]

    return doc

def load_text(file_path):
    """
    Docstring for load_text
    
    :param file_path: Text File path
    :return: List of Document objects
    """
    return TextLoader(file_path).load()

def file_format_wrapper(func):
    """
    Docstring for file_format_wrapper
    
    :param func: Function to wrap
    :return: Wrapped function that loads file based on its format
    """ 
    def wrap(file_path):
        """
        Docstring for wrap
        
        :param file_path: Path to the file
        :return: Loaded Document objects
        """         
        document = None
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
    """
    Docstring for load_file
    
    :param document: List of Document objects
    :return: List of Document objects with added session_id metadata
    """
    for doc in document:
        print(type(doc))
        if doc.metadata is None:
            doc.metadata = {}
        doc.metadata["session_id"] = st.session_state.current_session
    return document