import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader


GEMINI_API_KEY = "AIzaSyCELoqmwfAEnM9iqHVeTckw2f4M47LXCHs" 
genai.configure(api_key=GEMINI_API_KEY)
st.set_page_config(page_title="Acharya Dhanvantre Summarizer", layout="centered")
st.title("📄 Smart Document Summarizer")
st.subheader("Team Acharya Dhanvantre")
st.write("Upload a PDF and get AI-powered insights in seconds.")
