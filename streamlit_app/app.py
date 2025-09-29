import streamlit as st
import requests

st.set_page_config(page_title="LangGraph Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 LangGraph Chatbot")
st.write("Powered by FastAPI + Google AI + Streamlit")

# Session state for conversation
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.history.append(("You", user_input))

    response = requests.post("http://127.0.0.1:8000/chat", json={"message": user_input})
    bot_reply = response.json()["reply"]

    st.session_state.history.append(("Bot", bot_reply))

for sender, text in st.session_state.history:
    if sender == "You":
        st.chat_message("user").write(text)
    else:
        st.chat_message("assistant").write(text)
