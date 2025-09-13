import streamlit as st
import sys
import os
from PIL import Image
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utility import base64converter

def conversation_history_uploaded_files(docname,filepath):
    base64_logo = base64converter.get_base64_string("assets/logo.png")
    with st.sidebar:
        st.markdown(
            f'<img src="data:image/png;base64,{base64_logo}" id="side-logo">',
            unsafe_allow_html=True
        )
        if st.button('New chat 🤖 🌐'):
            st.session_state.current_session = f"New chat {len(st.session_state.chat_sessions)}"
            st.query_params["session"] = st.session_state.current_session
            st.session_state.chat_sessions[st.session_state.current_session] = {}
            st.session_state.chat_sessions[st.session_state.current_session] = {"messages":[],"files": ""}

        st.header('Uploaded Files 📁')
        uploaded_files(docname,filepath)
        st.header('Chat sessions 💬')
        display_chat_sessions()

def display_chat_sessions():
    for chat,ses in reversed(st.session_state.chat_sessions.items()):
        if st.button(str(chat)):
            st.session_state.current_session = chat
    print(st.session_state.chat_sessions)


def uploaded_files(name,url):
    if name is not None or st.session_state.uploaded_file_url:
        
        if name is not None:
            st.session_state.uploaded_file_url[name].append(url)

            icon_map = {
                'pdf':  Image.open('assets/pdf.png'),
                'json': Image.open('assets/json.png'),
                'text': Image.open('assets/text.png'),
                'document': Image.open('assets/document.png')
            }

            icon = next((icon_map[key] for key in icon_map if key in url), icon_map['document'])
            st.session_state.uploaded_file_url[name].append(icon)
        column1, column2 = 1,5
        for doc, link in st.session_state.uploaded_file_url.items():
            col1,col2 = st.columns([column1,column2])
            with col1:
                st.image(link[1])
            with col2:
                with open(link[0],'rb') as file:
                    st.download_button(
                        label=doc,
                        data=file,
                        file_name=doc,
                        type='tertiary'
                    )
    else:
        st.write('Doc yet to upload')