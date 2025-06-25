import streamlit as st
import yaml
import streamlit_authenticator as stauth

# ---------------------- Step 0: Session State Setup ----------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# ---------------------- Step 1: Load Config ----------------------
with open("config.yaml") as file:
    config = yaml.safe_load(file)

# ---------------------- Step 2: Authentication ----------------------
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, auth_status, username = authenticator.login("Login", location="main")

# ---------------------- Step 3: App Logic ----------------------
if auth_status:
    st.session_state.logged_in = True
    st.session_state.username = username

    # Layout with logout button
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("🌱 Varnixum")
        st.write(f"Welcome, **{st.session_state.username}**! 👋")
    with col2:
        if st.button("🚪 Logout"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.rerun()

    # App Body
    st.markdown("### Ask a question you'd like to understand:")
    question = st.text_input("")

    if question:
        st.markdown("📘 **Explanation:**")
        st.markdown(f"🤖 This is a mock response to your question: '{question}'")
        st.markdown("🖼️ **Visual Aid:**")
        st.image("https://placehold.co/600x400?text=Coming+Soon")

elif auth_status is False:
    st.error("Invalid credentials. Please try again.")

elif auth_status is None:
    st.warning("Please enter your credentials.")
