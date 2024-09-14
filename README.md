# Lang Vision

**Lang Vision** is a web application for language detection and translation. It allows users to input text, select a target language, and get translations using a user-friendly interface. Built with Flask, it integrates with language detection and translation services to provide accurate results.

## Features

- **Language Detection:** Automatically detects the language of the input text.
- **Text Translation:** Translates the detected text into the selected target language.
- **User-Friendly Interface:** Simple and intuitive web interface built with Bootstrap.
- **Support for Multiple Languages:** Provides translation options for a wide range of languages.

## Technologies

- **Flask:** Web framework for building the application.
- **Bootstrap:** Frontend framework for styling the application.
- **Langdetect:** Library for detecting the language of the input text.
- **Google Translate API:** Service for translating text into different languages.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/lang-vision.git
    cd lang-vision
    ```

2. **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application:**

    ```bash
    python app.py
    ```

5. **Open Your Browser:**

    Navigate to `http://127.0.0.1:5000` to access the application.

## Usage

1. **Enter Text:** Type the text you want to detect and translate into the provided text area.
2. **Select Target Language:** Choose the target language for translation from the dropdown menu.
3. **Submit Form:** Click the "Translate" button to get the detected language and translated text.

## Project Structure

```
lang-vision/
│
├── app.py                # Flask application code
├── templates/
│   └── index.html         # HTML template for the user interface
├── static/
│   └── style.css          # Custom styles (if any)
├── requirements.txt      # Python package dependencies
└── README.md             # Project documentation
```

## Requirements

- Python 3.x
- Flask
- Bootstrap (for frontend styling)
- Langdetect
- Googletrans

