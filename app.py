from flask import Flask, render_template, request
from langdetect import detect
from deep_translator import GoogleTranslator
from deep_translator.constants import GOOGLE_LANGUAGES_TO_CODES

app = Flask(__name__)

# Function to detect and translate text
def detect_and_translate(text, target_lang):
    # Detect the input text's language
    detected_lang = detect(text)

    # Translate text using GoogleTranslator
    translator = GoogleTranslator(source=detected_lang, target=target_lang)
    translate_text = translator.translate(text)

    return detected_lang, translate_text

# Home page route
@app.route('/')
def index():
    # Convert the available languages for dropdown
    languages = {value: key for key, value in GOOGLE_LANGUAGES_TO_CODES.items()}
    return render_template('index.html', languages=languages)

# Translation route
@app.route('/trans', methods=['POST'])
def trans():
    translation = ""
    detected_lang = ""

    if request.method == 'POST':
        text = request.form['text']  # Get the input text
        target_lang = request.form['target_lang']  # Get the target language
        detected_lang, translation = detect_and_translate(text, target_lang)  # Detect and translate the text

    # Convert the available languages for dropdown
    languages = {value: key for key, value in GOOGLE_LANGUAGES_TO_CODES.items()}
    
    return render_template('index.html', translation=translation, detected_lang=detected_lang, languages=languages)

if __name__ == '__main__':
    app.run(debug=True)
