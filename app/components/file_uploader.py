import streamlit as st

def file_uploader():
    uploaded_file = st.file_uploader(
        "Choose PDF/JSON/Text file",
        type=["pdf", "json", "txt"],
        key=st.session_state.current_session  # per-session uploader
    )
    if not st.session_state.chat_sessions:
        return None
    if uploaded_file is not None:
        st.session_state.chat_sessions[st.session_state.current_session]["current_file"] = uploaded_file.name
        st.session_state.chat_sessions[st.session_state.current_session]["files"].add(uploaded_file.name)
        st.session_state.metadata_file[st.session_state.current_session] = uploaded_file
        return uploaded_file

    saved_file = st.session_state.chat_sessions[st.session_state.current_session].get("current_file", "")
    if saved_file:
        return st.session_state.metadata_file[st.session_state.current_session]
    return None
