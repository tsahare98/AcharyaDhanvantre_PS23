import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader


GEMINI_API_KEY = "AIzaSyCELoqmwfAEnM9iqHVeTckw2f4M47LXCHs" 
genai.configure(api_key=GEMINI_API_KEY)
st.set_page_config(page_title="Acharya Dhanvantre Summarizer", layout="centered")
