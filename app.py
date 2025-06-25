import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Load credentials from YAML
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Authenticate
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Sidebar Login Section
st.sidebar.title("🔐 Login or Continue as Guest")
login_option = st.sidebar.radio("Choose Access Mode:", ["Login", "Continue as Guest"])

if login_option == "Login":
    name, auth_status, username = authenticator.login("Login", location="sidebar")

    if auth_status == False:
        st.sidebar.error("Invalid credentials. Please try again.")
    elif auth_status == None:
        st.sidebar.warning("Please enter your credentials.")
    elif auth_status:
        authenticator.logout("Logout", "sidebar")
        st.success(f"Welcome back, **{name}** 👋")
        st.title("🌱 Varnixum — Visual Learning Dashboard")
        st.write("You're logged in and ready to go!")
        st.write("✅ We’ll soon personalize your experience based on your role.")
        # Insert main app content here

elif login_option == "Continue as Guest":
    st.success("You're browsing as a guest 👀")
    st.title("🌱 Varnixum — Learn Visually and Simply")
    st.write("Feel free to try out the app with limited access.")
    # You can restrict some features here later
