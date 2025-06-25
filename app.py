import streamlit as st
import openai
import yaml
import streamlit_authenticator as stauth
from yaml.loader import SafeLoader
import random

# Load credentials
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Authenticator setup
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config.get('preauthorized')
)

# Access mode selection
access_mode = st.radio("🔐 Login or Continue as Guest", ["Login", "Continue as Guest"])

# Define session states
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = None

# Handle login
if access_mode == "Login":
    name, auth_status, username = authenticator.login("Login", location='main')
    if auth_status:
        st.session_state.authenticated = True
        st.session_state.username = username
    elif auth_status is False:
        st.error("Invalid credentials. Please try again.")
    else:
        st.warning("Please enter your credentials.")

elif access_mode == "Continue as Guest":
    st.session_state.authenticated = True
    st.session_state.username = "Guest"

# If logged in or guest, show app
if st.session_state.authenticated:
    user_display = st.session_state.username
    st.title("🌱 Varnixum")
    st.markdown("**Learn anything — visually and simply**")
    st.markdown(f"Welcome {'Admin Varnixum' if user_display.startswith('admin') else user_display}! You are logged in as `{user_display}`.\n")

    question = st.text_input("Ask a question you'd like to understand:")

    # --- Generate explanation using GPT (mock for now) ---
    def generate_explanation(prompt):
        # Real API (enable when billing works)
        # response = client.chat.completions.create(
        #     model="gpt-3.5-turbo",
        #     messages=[{"role": "user", "content": prompt}],
        #     temperature=0.7,
        # )
        # return response.choices[0].message.content.strip()

        # MOCK MODE
        return f"🤖 This is a mock response to your question: '{prompt}'. Varnixum AI will soon generate visual explanations for it."

    # --- Generate visual (mock or real via DALL·E) ---
    def generate_visual(prompt, use_mock=True):
        if use_mock:
            return f"https://via.placeholder.com/600x400.png?text=Mock+Image+{random.randint(1, 100)}"
        else:
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1
            )
            return response.data[0].url

    if question:
        explanation = generate_explanation(question)
        image_url = generate_visual(explanation, use_mock=True)

        st.subheader("📘 Explanation:")
        st.success(explanation)

        st.subheader("🖼️ Visual Aid:")
        st.image(image_url, caption="Generated Visual", use_column_width=True)
