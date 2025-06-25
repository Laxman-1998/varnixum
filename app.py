import streamlit as st
from openai import OpenAI
import os

# Setup OpenAI API Key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
client = OpenAI()

# Function to generate GPT explanation
def generate_explanation(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a teacher who explains complex topics using simple visual-friendly explanations."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7,
    )
    return response.choices[0].message.content

# Streamlit UI
st.set_page_config(page_title="Varnixum", layout="centered")
st.title("🌱 Varnixum")
st.subheader("Learn anything — visually and simply")

question = st.text_input("Ask a question you'd like to understand:")

if st.button("Explain with Visual"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("🧠 Thinking..."):
            explanation = generate_explanation(question)

        st.markdown("### 📘 Explanation:")
        st.write(explanation)

        st.markdown("### 🖼️ Visual Aid:")
        st.image("https://via.placeholder.com/512x300.png?text=Visual+coming+soon")
