import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader


GEMINI_API_KEY = "AIzaSyCELoqmwfAEnM9iqHVeTckw2f4M47LXCHs" 
genai.configure(api_key=GEMINI_API_KEY)
st.set_page_config(page_title="Acharya Dhanvantre Summarizer", layout="centered")
st.title("📄 Smart Document Summarizer")
st.subheader("Team Acharya Dhanvantre")
st.write("Upload a PDF and get AI-powered insights in seconds.")
with st.sidebar:
    st.header("Summarization Strategy")
    mode = st.selectbox(
        "Choose Mode:",
        ["Executive Summary", "Bullet-point Key Takeaways", "Detailed Summary", "Section-wise Summary"]
    )
    st.info(f"Using Google Gemini 3 Flash for {mode}")
