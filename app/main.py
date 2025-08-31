from collections import defaultdict
import os
import sys
from components.file_uploader import file_uploader
from components.chat_history_upload_files import conversation_history_uploaded_files
from utility.temp_file_helper import get_uploaded_path
from components.chatbot import assistant_reply, user_query, display_chat_messages
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from loader.loader import load_file
from vector_store.vector_store import create_and_save_vector_db
from embeddings.embed import embed_vector
import streamlit as st
from PIL import Image
logo = Image.open("assets/logo.png")


st.set_page_config(
    page_icon=logo,
    page_title='EmbeddoraDoc'
)

if "uploaded_file_url" not in st.session_state:
    st.session_state.uploaded_file_url = defaultdict(list)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "faiss_upload" not in st.session_state:
    st.session_state.faiss_upload = True

col1,col2 = st.columns([1,4], gap="small")
with col1:
    
    st.image(logo, width=125) 
with col2:
    st.title("EmbeddoraDoc 🧠🤖")



content_file = file_uploader()
tmp_path = get_uploaded_path(content_file)
if content_file:
    conversation_history_uploaded_files(content_file.name,tmp_path)
else:
    conversation_history_uploaded_files(None,tmp_path)

if content_file is None:
    st.session_state.faiss_upload = True
    st.session_state.messages.clear()

display_chat_messages()



if content_file is not None and st.session_state.faiss_upload:
    with st.spinner('Uploading into FAISS ..'):
        content = load_file(tmp_path)
        create_and_save_vector_db(content)
        st.session_state.faiss_upload = False


query = st.chat_input('Hello from EmbeddoraDoc!')
if content_file is not None:
    if query:
        user_query(query)
        with st.spinner('Loading ..'):
            ai_response = 'embed_vector(query)'
            assistant_reply(ai_response)
