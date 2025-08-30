import streamlit as st

def file_uploader():
    uploaded_file = st.file_uploader("Choose PDF/JSON/Text file",type=["pdf","json","txt"])

    
    if uploaded_file is None:
        st.info('No files uploaded')
    return uploaded_file