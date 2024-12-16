import streamlit as st
import requests

st.title("ChatGPT-like Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You: ", "")

if st.button("Send"):
    if user_input:
        st.session_state.history.append({"role": "user", "content": user_input})
        response = requests.post("http://localhost:8000/chat/", json={"content": user_input})
        if response.status_code == 200:
            bot_response = response.json().get("response")
            st.session_state.history.append({"role": "bot", "content": bot_response})
        else:
            st.error("Error: Unable to get response from the server.")

st.sidebar.title("Chat History")
for chat in st.session_state.history:
    if chat["role"] == "user":
        st.sidebar.write(f"You: {chat['content']}")
    else:
        st.sidebar.write(f"Bot: {chat['content']}")
