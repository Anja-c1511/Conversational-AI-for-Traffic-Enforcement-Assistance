import streamlit as st
import requests

st.title("🚦 Traffic Enforcement Chatbot")

user_input = st.text_input("Ask a traffic-related question:")

if st.button("Ask"):
    response = requests.post("http://127.0.0.1:8000/chat", json={"question": user_input})
    st.write("Chatbot:", response.json()["response"])

# To Run : streamlit run ui.py