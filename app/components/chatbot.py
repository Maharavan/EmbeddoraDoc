import streamlit as st

def display_chat_messages():
    if st.session_state.messages:
        for msg in st.session_state.messages:
            avatar = '🤖'  if msg['role']=='assistant' else '🧑🏻‍💻'
            with st.chat_message(msg['role'],avatar=avatar):
                st.markdown(msg['content'])


def user_query(query):
    if query:
        st.session_state.messages.append({'role':'user','content':query})

def assistant_reply(ai_response):
    st.session_state.messages.append({'role':'assistant','content':ai_response})   
