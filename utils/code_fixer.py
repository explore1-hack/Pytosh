import requests
import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

TOGETHER_API_KEY = st.secrets["TOGETHER_API_KEY"]
CODE_LLAMA_MODEL = "mistralai/Mixtral-8x7B-Instruct-v0.1"


HEADERS = {
    "Authorization": f"Bearer {TOGETHER_API_KEY}",
    "Content-Type": "application/json"
}

TOGETHER_URL = "https://api.together.xyz/v1/chat/completions"

def call_code_llama(prompt: str) -> str:
    payload = {
        "model": CODE_LLAMA_MODEL,
        "max_tokens": 512,
        "temperature": 0.3,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant that fixes and explains beginner Python code."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    try:
        res = requests.post(TOGETHER_URL, headers=HEADERS, json=payload)
        res.raise_for_status()
        return res.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"❌ Code LLaMA Error: {str(e)}"
def check_code_errors(code: str) -> str:
    prompt = f"""
Analyze the following Python code for bugs or issues.
List each issue with an explanation in simple terms:
```python
{code} """
    return call_code_llama(prompt)


# ✅ This returns human-readable error feedback using LLM.



### 🔧 Step 5: Define `correct_code_with_llm()` function


def correct_code_with_llm(code: str) -> str:
    prompt = f"""
You are a Python expert. Fix any syntax or logic errors in the code below.
Return only the corrected version without explanation:

```python
{code} """
    return call_code_llama(prompt)
