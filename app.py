import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader


GEMINI_API_KEY = "AIzaSyCELoqmwfAEnM9iqHVeTckw2f4M47LXCHs" # 1. Get key from Google AI Studio
genai.configure(api_key=GEMINI_API_KEY)
