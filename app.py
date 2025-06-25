import streamlit as st
import pandas as pd
import datetime
import streamlit_authenticator as stauth

# ----------------- USER DATA -----------------
import yaml
from yaml.loader import SafeLoader

# Fake user data (You can expand later)
config = {
    'credentials': {
        'usernames': {
            'demo_user': {
                'email': 'demo@example.com',
                'name': 'Demo User',
                'password': '$2b$12$KIX0iD6zJ6kgM4NTF47u3ODW4RuNYuR2BNl5YTbDp9VZpl/0MJ7G2'  # hashed "demo123"
            }
        }
    },
    'cookie': {
        'expiry_days': 15,
        'key': 'varnixum_cookie',
        'name': 'varnixum_login'
    },
    'preauthorized': {
        'emails': []
    }
}

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']

)

# ----------------- LOGIN SECTION -----------------
name, auth_status, username = authenticator.login("Login", location="main")

if auth_status is False:
    st.error("Invalid username or password.")
elif auth_status is None:
    st.warning("Please enter your credentials.")
elif auth_status:
    authenticator.logout("Logout", "sidebar")
    
    # -------------- Main App --------------
    st.set_page_config(page_title="Varnixum", layout="centered")
    st.title("🌱 Varnixum")
    st.subheader(f"Learn anything — visually and simply\nWelcome, {name}!")

    # Question Input
    question = st.text_input("Ask a question you'd like to understand:")

    if st.button("Explain with Visual"):
        if question.strip() == "":
            st.warning("Please enter a question.")
        else:
            with st.spinner("🧠 Thinking..."):
                explanation = f"🤖 This is a mock response to your question: '{question}'. Varnixum AI will soon generate visual explanations for it."

            st.markdown("### 📘 Explanation:")
            st.write(explanation)
            st.markdown("### 🖼️ Visual Aid:")
            st.image("https://via.placeholder.com/512x300.png?text=Visual+coming+soon")
