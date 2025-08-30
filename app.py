import streamlit as st
from gemini_model import ask_gemini

st.title("GitHub Helper Chatbot 🤖")

question = st.text_input("Ask a Git or GitHub question:")

if st.button("Ask"):
    if question:
        with st.spinner("Thinking..."):
            reply = ask_gemini(question)
            st.markdown("### 💬 Gemini Says:")
            st.write(reply)
    else:
        st.warning("Please enter a question.")
