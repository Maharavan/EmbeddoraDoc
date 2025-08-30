import tempfile
import streamlit as st

def get_uploaded_path(document):
    
    get_file_type = document.type
    if 'pdf' in get_file_type:
        get_extension = '.pdf'
    elif 'json' in get_file_type:
        get_extension = '.json'
    else:
        get_extension = '.txt'


    temporary_file = tempfile.NamedTemporaryFile(suffix=get_extension,delete=False)

    temporary_file.write(document.getbuffer())
    temporary_file.close()
    return temporary_file.name