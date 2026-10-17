
# Task 1: Import the Libraries
import streamlit as st
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from PyPDF2 import PdfReader, PdfWriter
from tempfile import NamedTemporaryFile
import base64
from htmlTemplates import css, bot_template, user_template, expander_css



def main():
    
    load_dotenv()
    
    st.set_page_config(page_title="Interactive Reader",   # browser tab title
                       page_icon=":books:",               # emoji, or a path/URL to an image file
                       layout="wide",                # "centered" (default) or "wide"
                       initial_sidebar_state="auto",) # "auto", "expanded" or "collapsed"   

    st.write(css, unsafe_allow_html=True)
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "N" not in st.session_state:
        st.session_state.N = 0

    st.session_state.col1, st.session_state.col2 = st.columns([1, 1])
    st.session_state.col1.header("Interactive Reader :books:")
    user_question = st.session_state.col1.text_input("Ask a question on the contents of the uploaded PDF:")
    st.session_state.expander1 = st.session_state.col1.expander('Your Chat', expanded=True)
    st.session_state.col1.markdown(expander_css, unsafe_allow_html=True) 
    # Task 5: Load and Process the PDF 
    

    
    # Task 7: Handle Query and Display Pages
    
       



if __name__ == '__main__':
    main()

