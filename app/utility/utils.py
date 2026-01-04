import streamlit as st


def load_css():
    st.markdown("""
                <style>
                .stDownloadButton > button, .stButton > button,.stButton > button *{
                    font-size: 25px; ! important;
                    background-color: transparent !important;
                    border: none !important;
                    box-shadow: none !important;
                    align-items:left !important;
                    font-family: "Source Sans Pro", sans-serif'  !important;
                    font-weight: 700 !important;
                }
                </style>
                """,unsafe_allow_html=True)