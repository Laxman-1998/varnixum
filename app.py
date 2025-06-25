import streamlit as st
import streamlit_authenticator as stauth
import yaml
import openai
from yaml.loader import SafeLoader

# Load config.yaml
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Create authenticator object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Display login form in main area (not sidebar)
name, auth_status, username = authenticator.login('Login', location='main')

# Title
st.markdown("""
    <h1 style='text-align: center;'>🌱 Varnixum</h1>
    <h3 style='text-align: center;'>Learn anything — visually and simply</h3>
""", unsafe_allow_html=True)

# Check auth status
if auth_status == False:
    st.error("Invalid credentials. Please try again.")
elif auth_status is None:
    st.warning("Please enter your credentials.")
elif auth_status:
    authenticator.logout('Logout', location='sidebar')
    st.success(f"Welcome {name}! You are logged in as {username}.")

    # App Body
    question = st.text_input("Ask a question you'd like to understand:")

    if question:
        st.subheader("📘 Explanation:")
        st.markdown(f"🤖 This is a mock response to your question: '{question}'. Varnixum AI will soon generate visual explanations for it.")

        st.subheader("🖼️ Visual Aid:")
        st.image("https://placehold.co/600x400?text=AI+Visual+Here", caption="(Coming soon with real visual generation)")
else:
    st.info("🔐 Please login or continue as guest.")
