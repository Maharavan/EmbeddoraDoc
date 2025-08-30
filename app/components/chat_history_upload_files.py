import streamlit as st



def conversation_history_uploaded_files(docname,filepath):
    with st.sidebar:
        st.title('Uploaded Files 📁')
        uploaded_files(docname,filepath)



def uploaded_files(name,url):
    if name is not None:
        st.session_state.uploaded_file_url[name] = url

    for doc, link in st.session_state.uploaded_file_url.items():
        with open(link,'rb') as file:
            st.download_button(
                label=f"📄 {doc}",
                data=file,
                file_name=doc,
                type='tertiary'
            )