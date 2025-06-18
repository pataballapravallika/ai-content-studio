# 🎨 AI Content Studio

A Generative Storytelling Web App built with Streamlit, GPT-4, and DALL·E.

## 🔍 Overview

This app allows users to input a theme or story idea, generates a short story using OpenAI's GPT-4, and creates an AI-generated illustration using DALL·E. It optionally supports video embedding via RunwayML links.

## 🚀 Features

- ✨ Generate creative stories from simple prompts using GPT-4  
- 🖼️ Create illustrations with DALL·E based on the generated story  
- 🎥 Embed RunwayML videos for enhanced multimedia storytelling  
- ⚡ Simple and fast web UI built with Streamlit  

## 🧰 Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **AI Models**: OpenAI GPT-4 (ChatCompletion), DALL·E  
- **Secrets Handling**: Streamlit secrets / dotenv  
- **Optional**: RunwayML video embedding

## 📦 Setup Instructions

1. Clone this repo:

   ```bash
   git clone https://github.com/pataballapravallika/ai-content-studio.git
   cd ai-content-studio
2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
4. Install dependencies
   ```bash
   pip install -r requirements.txt
5. Add your OpenAI API key to .streamlit/secrets.toml:
   ```bash
   OPENAI_API_KEY = "your-api-key-here"
6.  Run the app:
    ```bash
    streamlit run ai_content_studio.py
      
