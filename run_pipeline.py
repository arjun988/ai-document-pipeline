import os
import warnings
from src.document_conversion import pdf_to_images
from src.ocr_processing import extract_text_from_image
from src.preprocessing import preprocess_text
from src.llm_integration import initialize_llm, llm_infer
from src.information_extraction import extract_information
from src.document_classification import classify_document
from src.translation import translate_text, detect_language, format_translation_output

warnings.filterwarnings("ignore", category=UserWarning)

def main(input_pdf_path):
    output_folder = "./data/output/"
    
    # Convert PDF to images
    image_paths = pdf_to_images(input_pdf_path, output_folder)
    
    # Extract text from images using OCR
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
    model, tokenizer = initialize_llm("facebook/bart-large-cnn")  # Using a different model for summarization
    
    # LLM summary
    summary = llm_infer(model, tokenizer, translated_text)
    
    # Extract Information
    extracted_info = extract_information(translated_text)
    
    # Classify Document
    classification = classify_document(translated_text)
    
    # Format and print translation output
    formatted_translation_output = format_translation_output(original_text, translated_text, detected_lang, "English")
    print(formatted_translation_output)
    
    print("Summary:", summary)
    print("Extracted Information:", extracted_info)
    print("Document Classification:", classification)

if __name__ == "__main__":
    input_pdf_path = "./data/input/sample1.pdf"  # Replace with your input PDF path
    main(input_pdf_path)
