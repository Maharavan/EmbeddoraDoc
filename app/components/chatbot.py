import streamlit as st


def display_chat_messages():
    if st.session_state.chat_sessions:
        for msg in st.session_state.chat_sessions[st.session_state.current_session]["messages"]:
            avatar = '🤖' if msg['role'] == 'assistant' else '🧑🏻‍💻'
            with st.chat_message(msg['role'], avatar=avatar):
                st.write(msg['content'])

def user_query(query):
    if query:
        st.session_state.chat_sessions[st.session_state.current_session]["messages"].append(
            {"role": "user", "content": query}
        )
        with st.chat_message("user", avatar="🧑🏻‍💻"):
            st.write(query)

def assistant_reply(ai_response):
    st.session_state.chat_sessions[st.session_state.current_session]["messages"].append(
        {"role": "assistant", "content": ai_response}
    )
    with st.chat_message("assistant", avatar="🤖"):
        st.write(ai_response)
