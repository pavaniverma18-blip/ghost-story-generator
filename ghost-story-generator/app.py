import streamlit as st
from transformers import pipeline
import torch

st.set_page_config(page_title="Ghost Story Generator", page_icon="👻", layout="centered")
st.title("👻 Ghost Story Generator")
st.caption("Create spooky stories with an open-weight AI model running on your machine.")

st.info(
    "This app uses Google's open-weight FLAN-T5-small model through Hugging Face Transformers. "
    "The model downloads the first time you run it; after it is cached, generation can run locally."
)

@st.cache_resource(show_spinner="Loading the AI model for the first time...")
def load_generator():
    device = 0 if torch.cuda.is_available() else -1
    return pipeline("text2text-generation", model="google/flan-t5-small", device=device)

with st.form("story_form"):
    topic = st.text_input("Story idea", placeholder="A student hears footsteps in an empty college corridor...")
    mood = st.selectbox("Choose the mood", ["Spooky", "Mysterious", "Funny", "Folklore-inspired"])
    length = st.selectbox("Story length", ["Short (about 100 words)", "Medium (about 180 words)", "Long (about 250 words)"])
    setting = st.text_input("Where does it happen? (optional)", placeholder="An old library at midnight")
    generate = st.form_submit_button("Generate my story 👻")

if generate:
    if not topic.strip():
        st.warning("Please enter a story idea first.")
    else:
        word_target = {
            "Short (about 100 words)": "about 100 words",
            "Medium (about 180 words)": "about 180 words",
            "Long (about 250 words)": "about 250 words",
        }[length]
        place = f" The setting is {setting.strip()}." if setting.strip() else ""
        prompt = (
            f"Write an original {mood.lower()} ghost story in {word_target}. "
            f"Story idea: {topic.strip()}.{place} "
            "Make it engaging, coherent, suitable for a general audience, and give it a title. "
            "Do not explain the story; write only the story."
        )
        try:
            with st.spinner("Writing your story..."):
                generator = load_generator()
                result = generator(
                    prompt,
                    max_new_tokens=220 if "Short" in length else (320 if "Medium" in length else 420),
                    do_sample=True,
                    temperature=0.9,
                    top_p=0.92,
                    repetition_penalty=1.15,
                    truncation=True,
                )
            story = result[0]["generated_text"].strip()
            st.subheader("Your story")
            st.write(story)
            st.download_button("Download story as a text file", data=story, file_name="my_ghost_story.txt", mime="text/plain")
        except Exception as exc:
            st.error("The model could not generate a story. Check your internet connection on the first run and try again.")
            st.caption(f"Technical details: {type(exc).__name__}: {exc}")

with st.expander("How does it work?"):
    st.write(
        "Streamlit provides the interface. Hugging Face Transformers loads the open-weight FLAN-T5-small model. "
        "The prompt combines your idea, mood, setting, and length, then the model generates a story. "
        "Output quality can vary, so review stories before sharing."
    )

st.divider()
st.caption("Built for learning and open-source experimentation.")
