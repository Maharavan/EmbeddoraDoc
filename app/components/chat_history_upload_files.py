import streamlit as st
import sys
import os
from PIL import Image
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utility import base64converter
from components.session_exporter import chat_session_exporter

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
            st.session_state.chat_sessions[st.session_state.current_session] = {"messages":[],"files": set(),"faiss_upload":False,"current_file":""}
            st.rerun()
        chat_session_exporter()
        
        st.header('Uploaded Files in current session 📁')
        uploaded_files(docname,filepath)
        st.header('Chat sessions 💬')
        display_chat_sessions()

def display_chat_sessions():
    for chat, ses in reversed(st.session_state.chat_sessions.items()):
        current = False
        if chat==st.session_state.current_session:
            current = True
        with st.expander(chat,expanded=current):
            col1,col2 = st.columns(2)
            with col1:
                st.metric("📱 Messages",len(ses['messages']))
            with col2:
                st.metric("🗃️ File count", len(ses['files']))
            
            if st.session_state.get(f"renaming_{chat}", False):
                new_name = st.text_input("New session name:", key=f"rename_input_{chat}")
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("✅ Confirm", key=f"confirm_rename_{chat}"):
                        if new_name.strip():
                            rename_chat_session(chat, new_name.strip())
                            st.session_state[f"renaming_{chat}"] = False
                with col2:
                    if st.button("❌ Cancel", key=f"cancel_rename_{chat}"):
                        st.session_state[f"renaming_{chat}"] = False
                        st.rerun()
            else:
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("🚀Switch", key=f"switch_{chat}"):
                        st.session_state.current_session = chat
                        st.rerun()
                with col2:
                    if st.button("💥Delete", key=f"delete_{chat}"):
                        delete_chat_session(chat)
                with col3:
                    if st.button("🏷️Rename", key=f"rename_{chat}"):
                        st.session_state[f"renaming_{chat}"] = True
                        st.rerun()

def rename_chat_session(old_name, new_name):
    if old_name in st.session_state.chat_sessions and new_name:
        session_data = st.session_state.chat_sessions[old_name]
        st.session_state.chat_sessions[new_name] = session_data
        del st.session_state.chat_sessions[old_name]
        
        if st.session_state.current_session == old_name:
            st.session_state.current_session = new_name
            
        st.rerun()
def delete_chat_session(chat):
    if chat in st.session_state.chat_sessions:
        del st.session_state.chat_sessions[chat]
    if st.session_state.current_session == chat:

        if st.session_state.chat_sessions:
            st.session_state.current_session = list(st.session_state.chat_sessions.keys())[0]
        else:
            st.session_state.current_session = "New chat"
            st.session_state.chat_sessions[st.session_state.current_session] = {"messages":[],"files": set(),"faiss_upload":False,"current_file":""}
    st.rerun()

def uploaded_files(name,url):
    if name is not None or st.session_state.uploaded_file_url:
        
        if name is not None:
            if name not in st.session_state.uploaded_file_url:
                st.session_state.uploaded_file_url[name]={}
            st.session_state.uploaded_file_url[name]["path"] = url 
            st.session_state.uploaded_file_url[name]['session']=st.session_state.current_session

            icon_map = {
                'pdf':  Image.open('assets/pdf.png'),
                'json': Image.open('assets/json.png'),
                'text': Image.open('assets/text.png'),
                'document': Image.open('assets/document.png')
            }

            icon = next((icon_map[key] for key in icon_map if key in url), icon_map['document'])
            st.session_state.uploaded_file_url[name]['icon']=icon
        column1, column2 = 1,5
        for doc, link in st.session_state.uploaded_file_url.items():
            if st.session_state.current_session==link['session']:
                col1,col2 = st.columns([column1,column2])
                with col1:
                    st.image(link['icon'])
                with col2:
                    with open(link['path'],'rb') as file:
                        st.download_button(
                            label=doc,
                            data=file,
                            file_name=doc,
                            type='tertiary'
                        )
    else:
        st.write('Doc yet to upload')