import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="LinkedIn Bio Roaster",
    page_icon="🔥",
    layout="centered"
)

st.title("🔥 LinkedIn Bio Roaster")
st.caption("Powered by LLaMA 3 via Groq")
st.divider()

# Groq client
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Roast intensity selector
intensity = st.select_slider(
    "Roast Intensity",
    options=["Mild", "Medium", "Savage", "Brutal"],
    value="Savage"
)

PROMPTS = {
    "Mild": """You are a kind but honest LinkedIn bio reviewer.
Point out cliches and buzzwords with light humour.
Be encouraging. End with 2 specific genuine compliments.
Keep it short and simple.""",

    "Medium": """You are a witty LinkedIn bio roaster.
Call out buzzwords and humble-brags with sharp humour.
Be funny but not cruel. End with one genuine compliment.
Keep sentences short and casual.""",

    "Savage": """You are a savage LinkedIn bio roaster.
Destroy buzzwords and cliches. Be hilarious and cutting.
End with one tiny genuine compliment.
Use short punchy sentences.""",

    "Brutal": """You are the most ruthless LinkedIn bio critic.
Tear this bio apart brutally but funny.
End with one honest sentence of feedback.
Use very simple short sentences."""
}

bio = st.text_area(
    "Paste your LinkedIn bio here",
    height=200,
    placeholder="Passionate results-driven thought leader who leverages synergies..."
)

if st.button("Roast Me", type="primary", use_container_width=True):
    if not bio.strip():
        st.warning("Paste a bio first.")
    else:
        with st.spinner("Roasting..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": PROMPTS[intensity]},
                    {"role": "user", "content": f"Roast this LinkedIn bio:\n\n{bio}"}
                ]
            )

            roast = response.choices[0].message.content

        st.divider()
        st.subheader(f"{intensity} Roast 🔥")
        st.write(roast)

st.divider()
st.caption("Built at DataYard | Powered by Groq + LLaMA 3")
