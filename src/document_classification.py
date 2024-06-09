from transformers import pipeline

def classify_document(text, model_name="distilbert-base-uncased"):
    classifier = pipeline("zero-shot-classification", model=model_name)
    labels = ["invoice", "receipt", "letter", "report"]
    result = classifier(text, candidate_labels=labels)
    return result
