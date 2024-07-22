# Image Description using Google Gemini Generative AI

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-brightgreen.svg)

## Overview

This project demonstrates how to build a Streamlit application that allows users to upload images and generate descriptions using the power of Google Generative AI. Users can provide a custom prompt or use a default prompt to describe the content of the images.

## Features

- Upload and process image files.
- Use Google Generative AI to generate descriptions for the images.
- Configure and customize the description prompt.
- Display the uploaded image along with the generated description.

## Installation

### Prerequisites

- Python 3.7 or higher
- [Streamlit](https://streamlit.io/)
- [Pillow](https://pypi.org/project/Pillow/)
- [google-generativeai](https://pypi.org/project/google-generativeai/)

To use this project, clone the repository and set up the environment as follows:

1. **Clone the Repository**:
    ```bash
    https://github.com/Imran-ml/Image_Description_using_Google_GenerativeAI.git
    ```
2. **Setup the Environment**:
    - Navigate to the project directory and activate the virtual environment.
    - Install the dependencies from `requirements.txt`.

### Steps

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/image-description-using-google-generativeai.git
    cd image-description-using-google-generativeai
    ```

2. Create and activate a virtual environment:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up your Google API key:

    Create a `.env` file in the project root and add your Google API key:

    ```env
    GOOGLE_API_KEY=your_google_api_key
    ```

5. Run the Streamlit app:

    ```sh
    streamlit run app.py
    ```

## Usage

1. Open the Streamlit app in your browser.
2. Upload your image files in the provided section.
3. Configure your prompt from the input field (optional).
4. Enter your Google API key and click 'Set API Key'.
5. Click 'Describe Image' to generate the description for the uploaded image.

## Code Explanation

The main components of the code are:

- **API Key Handling**: Allows the user to set their Google API key for generative AI.
- **Image Upload**: Users can upload images, which are displayed and processed to generate descriptions.
- **Description Generation**: Uses Google Generative AI to generate descriptions based on the provided or default prompt.
- **UI Components**: Provides a user-friendly interface for uploading images, setting the API key, and viewing results.

## Configuration

You can configure the following settings from the Streamlit sidebar:

- **Google API Key**: Enter your Google API key to enable generative AI features.
- **Prompt**: Enter a custom prompt or use the default prompt for generating image descriptions.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## About Author

- **Name**: Muhammad Imran Zaman
- **Email**: [imranzaman.ml@gmail.com](mailto:imranzaman.ml@gmail.com)
- **Professional Links**:
    - Kaggle: [Profile](https://www.kaggle.com/muhammadimran112233)
    - LinkedIn: [Profile](https://www.linkedin.com/in/muhammad-imran-zaman)
    - Google Scholar: [Profile](https://scholar.google.com/citations?user=ulVFpy8AAAAJ&hl=en)
    - YouTube: [Channel](https://www.youtube.com/@consolioo)
- **Project Repository**: [GitHub Repo](https://github.com/Imran-ml/Image_Description_using_Google_GenerativeAI.git)
