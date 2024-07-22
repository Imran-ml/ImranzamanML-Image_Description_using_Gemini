import os
import streamlit as st
import google.generativeai as genai
from PIL import Image
import base64

# Function to set the Google API key
def set_api_key(api_key):
    os.environ["GOOGLE_API_KEY"] = api_key
    genai.configure(api_key=api_key)

# Function to get description from the image
def get_image_description(image, user_prompt=None):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    prompt = user_prompt if user_prompt else "What is in this photo?"
    response = model.generate_content([prompt], images=[image])
    return response.text

# Helper function to convert image to base64
def get_base64_of_image(image_path):
    with open(image_path, "rb") as image_file:
        base64_str = base64.b64encode(image_file.read()).decode()
    return base64_str

def main():
    st.set_page_config(page_title="Talk to Image", layout="wide")

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/png;base64,{get_base64_of_image('image.png')});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Image Description using Gemini!")

    st.subheader("Upload your Image File")
    uploaded_file = st.file_uploader("Upload your image file", type=["png", "jpg", "jpeg"])

    st.sidebar.header("Configuration")
    api_key = st.sidebar.text_input("Google API Key:", type="password")

    if st.sidebar.button("Set API Key"):
        if api_key:
            set_api_key(api_key)
            st.sidebar.success("API Key set successfully.")
        else:
            st.sidebar.error("Please enter a valid API Key.")

    prompt = st.text_input("Enter your prompt (optional):", value="What is in this photo?")

    if st.button("Describe Image") and uploaded_file:
        if "GOOGLE_API_KEY" in os.environ and os.environ["GOOGLE_API_KEY"]:
            try:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Image", use_column_width=True)

                with st.spinner("Generating description..."):
                    description = get_image_description(image, prompt)
                    st.write("**Description:** ", description)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter your Google API key and click 'Set API Key'.")

    st.markdown("---")
    st.write("Happy to Connect:")
    kaggle, linkedin, google_scholar, youtube, github = st.columns(5)

    image_urls = {
        "kaggle": "https://www.kaggle.com/static/images/site-logo.svg",
        "linkedin": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/600px-LinkedIn_logo_initials.png",
        "google_scholar": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Google_Scholar_logo.svg/768px-Google_Scholar_logo.svg.png",
        "youtube": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/YouTube_social_white_square_%282017%29.svg/640px-YouTube_social_white_square_%282017%29.svg.png",
        "github": "https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png"
    }

    social_links = {
        "kaggle": "https://www.kaggle.com/muhammadimran112233",
        "linkedin": "https://www.linkedin.com/in/muhammad-imran-zaman",
        "google_scholar": "https://scholar.google.com/citations?user=ulVFpy8AAAAJ&hl=en",
        "youtube": "https://www.youtube.com/@consolioo",
        "github": "https://github.com/Imran-ml"
    }

    kaggle.markdown(f'<a href="{social_links["kaggle"]}"><img src="{image_urls["kaggle"]}" width="50" height="50"></a>', unsafe_allow_html=True)
    linkedin.markdown(f'<a href="{social_links["linkedin"]}"><img src="{image_urls["linkedin"]}" width="50" height="50"></a>', unsafe_allow_html=True)
    google_scholar.markdown(f'<a href="{social_links["google_scholar"]}"><img src="{image_urls["google_scholar"]}" width="50" height="50"></a>', unsafe_allow_html=True)
    youtube.markdown(f'<a href="{social_links["youtube"]}"><img src="{image_urls["youtube"]}" width="50" height="50"></a>', unsafe_allow_html=True)
    github.markdown(f'<a href="{social_links["github"]}"><img src="{image_urls["github"]}" width="50" height="50"></a>', unsafe_allow_html=True)
    st.markdown("---")

if __name__ == "__main__":
    main()
