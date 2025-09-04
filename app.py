import streamlit as st
import requests

st.set_page_config(page_title="AI Multi-Agent Assistant", page_icon="🤖")

st.title("🎙️ AI Multi-Agent Voice Assistant")
st.write("Ask me about stock trends, analysis, and recommendations!")

query = st.text_input("Your Question:")
if st.button("Ask"):
    if query:
        response = requests.get(f"http://127.0.0.1:8000/ask?query={query}").json()
        st.success(response["response"])
