import re
from langdetect import detect

def preprocess_text(text):
    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def detect_language(text):
    try:
        return detect(text)
    except:
        return "en"
