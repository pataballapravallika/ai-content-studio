import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("open-ai")

st.title("🎨 AI Content Studio")

# User prompt for story
user_prompt = st.text_input("Enter your theme/story idea:")

# Step 1: Generate story
if st.button("Generate Story"):
    with st.spinner("Generating story..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": f"Write a short story about: {user_prompt}"}
            ]
        )
        story = response.choices[0].message["content"]
        st.subheader("📖 Generated Story")
        st.write(story)

        # Step 2: Generate image from story using DALL·E
        if st.button("Generate Illustration (DALL·E)"):
            with st.spinner("Generating image..."):
                dalle_response = openai.Image.create(
                    prompt=story,
                    n=1,
                    size="512x512"
                )
                img_url = dalle_response['data'][0]['url']
                st.image(img_url, caption="🖼️ AI-Generated Illustration")

# Step 3: Input for RunwayML video
video_link = st.text_input("Paste your RunwayML video link (optional):")
if video_link:
    st.video(video_link)
