from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import JSONLoader
from pathlib import Path

def load_pdf(file_path):
    return PyPDFLoader(file_path).load()

def load_json(file_path):
    return JSONLoader(file_path).load()

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
    print('Processing files:',document)
    return document