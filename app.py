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
    uploaded_file = st.file_uploader("Upload your document (PDF)", type=['pdf'])

if uploaded_file is not None:
    with st.spinner("Reading document and generating summary..."):
        try:
            # 1. Extract Text [cite: 38, 39]
            reader = PdfReader(uploaded_file)
            text_content = ""
            for page in reader.pages:
                text_content += page.extract_text()
                prompt_prefix = {
                "Executive Summary": "Provide a concise executive summary of the following text:",
                "Bullet-point Key Takeaways": "Extract the most important key takeaways as a bulleted list from this text:",
                "Detailed Summary": "Provide a comprehensive and detailed summary of the following content:",
                "Section-wise Summary": "Break down and summarize the following text section by section:"
            }
