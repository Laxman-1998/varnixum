# Step 1: Add Role to secrets.toml or config dictionary
# You might have it hardcoded or in Streamlit Secrets.
# Here's how you structure the user roles if using Python config:

import streamlit_authenticator as stauth

# User credentials with roles
config = {
    'credentials': {
        'usernames': {
            'laxman1998': {
                'name': 'Laxman',
                'password': stauth.Hasher(['demo123']).generate()[0],
                'email': 'laxman@example.com',
                'role': 'admin',
            },
            'testuser': {
                'name': 'Test User',
                'password': stauth.Hasher(['test123']).generate()[0],
                'email': 'test@example.com',
                'role': 'user',
            },
        }
    },
    'cookie': {
        'name': 'varnixum_cookie',
        'key': 'some_signature_key',
        'expiry_days': 30
    },
    'preauthorized': {
        'emails': []
    }
}

# Step 2: Access and Use Role After Login

import streamlit as st

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)

name, auth_status, username = authenticator.login("Login", location="main")

if auth_status:
    role = config['credentials']['usernames'][username]['role']

    if role == 'admin':
        st.success(f"Welcome Admin {name} 👑")
        st.markdown("### Admin Dashboard")
        st.info("📊 You'll soon see analytics and content logs here.")
    else:
        st.success(f"Welcome {name}")
        question = st.text_input("Ask a question you'd like to understand:")
        if st.button("Explain with Visual"):
            if question.strip():
                st.write(f"**Question:** {question}")
                st.write("**Mock Explanation:** This is how Varnixum will explain it visually.")
                st.image("https://via.placeholder.com/512x300.png?text=Coming+Soon")
            else:
                st.warning("Please enter a question.")
elif auth_status == False:
    st.error("Invalid credentials")
elif auth_status is None:
    st.warning("Please enter your credentials")
