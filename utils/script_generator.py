import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def generate_script(topic, persona, duration):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "❌ Missing GROQ_API_KEY in .env file."

    # Choose LLaMA 3 model
    llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=api_key)

    template = PromptTemplate.from_template(
        """You are a {persona} creating a YouTube video script.

        Topic: {topic}
        Approx Duration: {duration} minutes

        Structure your output as:
        1. Title
        2. Hook (1 paragraph)
        3. Introduction (1 short paragraph)
        4. Main Content (3-5 bullet sections)
        5. Closing (1 paragraph)

        Tone: Match the chosen persona’s style.
        Keep it conversational, engaging, and natural for YouTube.
        """
    )

    prompt = template.format(topic=topic, persona=persona, duration=duration)
    response = llm.invoke(prompt)
    return response.content.strip()
