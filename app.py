import streamlit as st
import json

# Load users from JSON
def load_users():
    with open("users.json", "r") as file:
        return json.load(file)

# Basic login UI
def login():
    st.title("🔐 Login to Varnixum")
    users = load_users()
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        for user in users:
            if user["username"] == username and user["password"] == password:
                st.success(f"Welcome, {username}!")
                st.session_state.logged_in = True
                st.session_state.username = username
                return True
        st.error("Invalid credentials")
    return False

# Initial state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login or show main app
if not st.session_state.logged_in:
    login()
else:
    st.title("🌱 Varnixum")
    st.write(f"Welcome, **{st.session_state.username}**! 👋")
    st.write("Ask a question you'd like to understand:")

    question = st.text_input("📌 Your Question:")
    if question:
        # For now, mock explanation
        st.subheader("📘 Explanation:")
        st.info(f"🤖 This is a mock explanation for: '{question}'")

        st.subheader("🖼️ Visual Aid:")
        st.image("https://placehold.co/400x200?text=Coming+Soon", caption="Visuals coming soon!")
