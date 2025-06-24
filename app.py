import streamlit as st

st.set_page_config(page_title="Varnixum", layout="centered")
st.title("🌱 Varnixum")
st.subheader("Learn anything — visually and simply")

question = st.text_input("Ask a question you'd like to understand:")

if st.button("Explain with Visual"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        st.info("🧠 Generating explanation...")
        st.info("🖼️ Generating visual...")
        st.success("✅ This is just a placeholder. We'll add real AI soon.")
        st.write(f"**Your Question:** {question}")
        st.write("**Answer will appear here**")
        st.image("https://via.placeholder.com/512x300.png?text=Varnixum+Visual+Goes+Here")
