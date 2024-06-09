import streamlit as st
import warnings
from document_conversion import pdf_to_images
from ocr_processing import extract_text_from_image
from preprocessing import preprocess_text
from llm_integration import initialize_llm, llm_infer
from information_extraction import extract_information
from document_classification import classify_document
from translation import translate_text, detect_language, format_translation_output

warnings.filterwarnings("ignore", category=UserWarning)

st.title("AI-Powered Document Processing Chatbot")

uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file is not None:
    st.write("Processing document...")
    
    # Save uploaded file
    with open(f"./data/input/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Convert PDF to images
    image_paths = pdf_to_images(f"./data/input/{uploaded_file.name}", "./data/output/")
    text = ""
    for image_path in image_paths:
        text += extract_text_from_image(image_path) + " "
    
    # Preprocess text
    sentences = preprocess_text(text)
    original_text = " ".join(sentences)
    
    # Detect language
    detected_lang = detect_language(original_text)
    
    # Translate text to English
    translated_text = translate_text(original_text, src_lang=detected_lang, tgt_lang="en")
    
    # Load LLM
    model, tokenizer = initialize_llm("facebook/bart-large-cnn")
    
    # LLM summary
    summary = llm_infer(model, tokenizer, translated_text)
    
    # Extract Information
    extracted_info = extract_information(translated_text)
    
    # Classify Document
    classification = classify_document(translated_text)
    
    # Format translation output
    formatted_translation_output = format_translation_output(original_text, translated_text, detected_lang, "English")
    
    st.markdown(formatted_translation_output)
    st.write("Summary:", summary)
    st.write("Extracted Information:", extracted_info)
    st.write("Document Classification:", classification)
