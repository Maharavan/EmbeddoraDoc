import streamlit as st

def file_uploader():
    uploaded_file = st.file_uploader(
        "Choose PDF/JSON/Text file",
        type=["pdf", "json", "txt"],
        key=st.session_state.current_session  # per-session uploader
    )

    if uploaded_file is not None:
        st.session_state.chat_sessions[st.session_state.current_session]["files"] = uploaded_file.name
        st.session_state.metadata_file[st.session_state.current_session] = uploaded_file
        return uploaded_file

    saved_file = st.session_state.chat_sessions[st.session_state.current_session].get("files", "")
    if saved_file:
        st.info(f"Previously uploaded: **{saved_file}** (still linked to this session)")
        return st.session_state.metadata_file[st.session_state.current_session]
    return None
