import streamlit as st
import requests

# FastAPI Backend URL (Ensure FastAPI is running on your laptop)
API_URL = "https://connecxite-backend.onrender.com/generate_message_generate_message_post"

# Sidebar for chat history
with st.sidebar:
    st.title("Chat History")
    chat_history = st.session_state.get("chat_history", [])

    for chat in chat_history:
        st.markdown(f"**You:** {chat['user_url']} → {chat['target_url']}")

    if st.button("Clear Chat"):
        st.session_state.chat_history = []

# Main content
st.title("LinkedIn Connection Message Generator")

st.write("Enter your LinkedIn URL and your target's LinkedIn URL to generate a personalized connection message.")

# Input fields
user_linkedin_url = st.text_input("Your LinkedIn Profile URL", placeholder="Enter your LinkedIn URL")
target_linkedin_url = st.text_input("Target's LinkedIn Profile URL", placeholder="Enter target's LinkedIn URL")

# Submit button
if st.button("Generate Message"):
    if user_linkedin_url and target_linkedin_url:
        with st.spinner("Generating connection message..."):
            response = requests.post(API_URL, json={"user_url": user_linkedin_url, "target_url": target_linkedin_url})

            if response.status_code == 200:
                ai_message = response.json().get("message", "No response received.")

                # Display response
                st.subheader("Generated Message:")
                st.write(ai_message)

                # Save chat history
                if "chat_history" not in st.session_state:
                    st.session_state.chat_history = []
                st.session_state.chat_history.append({
                    "user_url": user_linkedin_url,
                    "target_url": target_linkedin_url
                })
            else:
                st.error("Error: Failed to connect to the backend.")
    else:
        st.warning("Please enter both LinkedIn URLs.")
