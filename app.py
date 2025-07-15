import streamlit as st
from utils.code_fixer import check_code_errors, correct_code_with_llm
from utils.chat_explainer import ask_mixtral
from utils.security import is_safe_code, get_block_reason
from utils.safe_executor import run_safe_code

print("✅ All imports working!")

st.markdown(
    """
    <div style='text-align: center;'>
        🌐 Connect: 
        <a href='https://github.com/explore1-hack' target='_blank'>GitHub</a> |
        <a href='https://www.linkedin.com/in/ashutosh-pandey-b492ba371?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app' target='_blank'>LinkedIn</a> |
        <a href='https://legendcolumn.xyz' target='_blank'>Blog</a>
    </div>
    """, 
    unsafe_allow_html=True
)
st.set_page_config(page_title="PyTosh - AI Python Editor", layout="wide")
st.markdown("""
<style>
.floating-yt-button {
    position: fixed;
    bottom: 25px;
    right: 25px;
    background-color: red;
    color: white;
    padding: 12px 18px;
    border-radius: 30px;
    font-weight: bold;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    z-index: 9999;
    text-align: center;
}
.floating-yt-button a {
    color: white;
    text-decoration: none;
}
</style>

<div class="floating-yt-button">
    <a href="www.youtube.com/@GenesisProtocol.AIgenz" target="_blank">
        ▶️ Watch on YouTube
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .chatbot-box {
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 320px;
        background-color: #fff;
        border: 1px solid #ccc;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        z-index: 9999;
    }
    .chat-toggle {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background-color: #4CAF50;
        color: white;
        padding: 12px 20px;
        border-radius: 30px;
        cursor: pointer;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        z-index: 9998;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .main { background-color: #f9f9fc; }
    .logo-img { width: 100px; margin-bottom: -20px; }
    </style>
""", unsafe_allow_html=True)
st.info("👨‍💻 Made by Ashutosh Pandey — LLM Developer & AI Innovator")


st.image("pytosh_logo.png", use_container_width=False, width=200)

st.title("🐍 PyTosh - Learn Python with Confidence")
st.caption("Built for students & beginners who fear Python ✨")

code_input = st.text_area("📝 Paste your Python code here:", height=300, key="code_area")

col1, col2, col3 = st.columns(3)

if col1.button("🔍 Check Error"):
    if is_safe_code(code_input):
        with st.spinner("Analyzing with Code LLaMA..."):
            feedback = check_code_errors(code_input)
        st.info("🔧 Code Feedback:")
        st.code(feedback, language="python")
    else:
        st.error(get_block_reason(code_input))


if col2.button("✅ Correct Code"):
    if is_safe_code(code_input):
        with st.spinner("Fixing with Code Pytosh..."):
            corrected = correct_code_with_llm(code_input)
        st.success("✅ Code corrected:")
        st.code(corrected, language="python")

        st.download_button(
            label="⬇️ Download Corrected Code",
            data=corrected,
            file_name="pytosh_output.py",
            mime="text/plain"
        )
    else:
        st.error(get_block_reason(code_input))



if col3.button("🧪 Run Safe Code"):
    if is_safe_code(code_input):
        with st.spinner("Executing safely..."):
            result = run_safe_code(code_input)
        st.success("🔎 Output:")
        st.code(result)
    else:
        st.error(get_block_reason(code_input))

st.markdown("---")
st.subheader("💬 Ask PyTosh Chatbot")
user_q = st.text_input("Ask a question about your code, errors, or Python itself:", key="chat")

if user_q:
    if is_safe_code(code_input):
        with st.spinner("Mixtral is thinking..."):
            reply = ask_mixtral(user_q, context=code_input)
        st.success("💡 PyTosh says:")
        st.write(reply)
    else:
        st.error(get_block_reason(code_input))

st.markdown("---")
st.caption("🚫 PyTosh blocks dangerous code. No access to GPU, file system, or shell.")
# Floating Chat UI
chat_toggle = st.checkbox("💬 Chat with PyTosh", value=False)

if chat_toggle:
    with st.container():
        st.markdown('<div class="chatbot-box">', unsafe_allow_html=True)

        st.markdown("#### 🤖 PyTosh Chatbot")
        user_q = st.text_input("Ask me anything about your code:", key="floating_chat")

        if user_q:
            if is_safe_code(code_input):
                with st.spinner("Pytosh is thinking..."):
                    reply = ask_mixtral(user_q, context=code_input)
                st.success("💡 PyTosh says:")
                st.write(reply)
            else:
                st.error(get_block_reason(code_input))

        st.markdown("</div>", unsafe_allow_html=True)
