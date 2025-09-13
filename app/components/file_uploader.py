import streamlit as st

def file_uploader():
    uploaded_file = st.file_uploader("Choose PDF/JSON/Text file",
                                     type=["pdf","json","txt"],
                                     key=st.session_state.current_session)

    
    if uploaded_file is not None:
        st.session_state.chat_sessions[st.session_state.current_session]["files"] = uploaded_file.name
    return uploaded_file if uploaded_file else None