import streamlit as st
from utils.script_generator import generate_script
from persona_prompts import PERSONAS

st.set_page_config(page_title="🎬 YouTube Script Generator", layout="centered")

st.title("🎬 YouTube Script Generator")
st.markdown("Create engaging, persona-driven YouTube scripts using **LLaMA 3 + Groq**.")

topic = st.text_input("🎯 Enter your video topic", placeholder="e.g. How AI is changing education")
persona = st.selectbox("🧍 Choose a Persona", list(PERSONAS.keys()))
duration = st.slider("⏱ Approximate video length (minutes)", 1, 20, 5)

if st.button("Generate Script"):
    with st.spinner("Crafting your script..."):
        script = generate_script(topic, persona, duration)
        st.subheader(f"🧠 Script ({persona} Style):")
        st.write(script)
        st.download_button("📥 Download Script", data=script, file_name=f"{topic}.txt")

st.markdown("---")
st.caption("Built with 💡 LangChain + Groq + Streamlit")
