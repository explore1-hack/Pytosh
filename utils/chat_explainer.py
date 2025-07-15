import requests
import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

TOGETHER_API_KEY = st.secrets["TOGETHER_API_KEY"]
MIXTRAL_MODEL = "mistralai/Mixtral-8x7B-Instruct-v0.1"

HEADERS = {
    "Authorization": f"Bearer {TOGETHER_API_KEY}",
    "Content-Type": "application/json"
}

TOGETHER_URL = "https://api.together.xyz/v1/chat/completions"


def ask_mixtral(question: str, context: str = "") -> str:
    prompt = f"""
You are an AI Python tutor named PyTosh. Help the user understand Python code.
Context (code):
{context}

User's Question:
{question}

Answer clearly and helpfully.
"""

    payload = {
        "model": MIXTRAL_MODEL,
        "max_tokens": 512,
        "temperature": 0.5,
        "messages": [
            {"role": "system", "content": "You are a helpful Python tutor who explains code and errors simply."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        res = requests.post(TOGETHER_URL, headers=HEADERS, json=payload)
        res.raise_for_status()
        return res.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"❌ Mixtral Error: {str(e)}"
