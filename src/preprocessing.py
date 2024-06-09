import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\W+', ' ', text)
    return text

def preprocess_text(text):
    text = clean_text(text)
    sentences = text.split('.')
    return sentences
