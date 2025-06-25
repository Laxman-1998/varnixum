import streamlit as st

st.set_page_config(page_title="Varnixum", layout="centered")
st.title("🌱 Varnixum")
st.subheader("Learn anything — visually and simply")

question = st.text_input("Ask a question you'd like to understand:")

def generate_mock_explanation(user_question):
    # Simple mock explanations based on keywords
    if "earth" in user_question.lower():
        return "🌍 The Earth is round due to gravity pulling matter equally in all directions, forming a sphere over time."
    elif "stars" in user_question.lower():
        return "✨ Stars twinkle because their light is distorted by Earth's atmosphere, especially when near the horizon."
    elif "fractions" in user_question.lower():
        return "📐 Multiplying 1/2 × 1/3 means taking one half of one third. Visually, it's like overlapping two shaded regions — the result is 1/6."
    else:
        return f"🤖 This is a mock response to your question: '{user_question}'. Varnixum AI will soon generate visual explanations for it."

if st.button("Explain with Visual"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("🧠 Thinking..."):
            explanation = generate_mock_explanation(question)
        st.markdown("### 📘 Explanation:")
        st.write(explanation)

        # Mock visual
        st.markdown("### 🖼️ Visual Aid:")
        st.image("https://via.placeholder.com/512x300.png?text=Varnixum+Mock+Visual")
