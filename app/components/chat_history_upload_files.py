import streamlit as st
from PIL import Image
def conversation_history_uploaded_files(docname,filepath):

    with st.sidebar:
        st.title('Uploaded Files 📁')
        uploaded_files(docname,filepath)



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