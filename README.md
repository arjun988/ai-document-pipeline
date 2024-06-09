# AI-Powered Document Processing Pipeline

This project provides a robust solution for processing PDF documents using AI techniques. It converts PDFs to images, extracts text via OCR, preprocesses the text, translates it to English (if necessary), summarizes the content, extracts key information, and classifies the document.

## Features
1. PDF to Images Conversion: Converts each page of a PDF document into an image.

2. OCR (Optical Character Recognition): Extracts text from images.

3. Text Preprocessing: Cleans and structures the extracted text.

4. Language Detection and Translation: Detects the language of the input text and translates it to English if it is not already in English.

5. Summarization: Summarizes the translated text using a pre-trained language model.

6. Information Extraction: Identifies and extracts named entities from the text.

7. Document Classification: Classifies the document into predefined categories.

8. Streamlit UI: Provides an interactive user interface for uploading PDFs and viewing the processed results.

## Installation
Prerequisites
Python 3.7 or higher
pip (Python package installer)

1. Install Dependencies

2. Clone the repository 

3. Move to your directory
```
cd your-project
```
Install required Python packages:

```
pip install -r requirements.txt
```
### Install Tesseract OCR:

1. Windows: Download the installer from here and install it.
https://github.com/UB-Mannheim/tesseract/wiki

2. macOS: Use Homebrew to install:

brew install tesseract

3. Linux: Use your package manager:

sudo apt-get install tesseract-ocr


### Configuration

Ensure Tesseract is added to your system's PATH.

Specify the path to the Tesseract executable in ocr_processing.py:
```
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```
### Streamlit UI
Run the Streamlit application:
```
streamlit run src/chatbot_ui.py
```
Open your browser and go to http://localhost:8501.

1. Upload a PDF document and view the processed results, including the translated text, summary, extracted information, and document classification.

2. Command Line
Place your input PDF in the ./data/input/ directory.
Run the pipeline:
```
python src/run_pipeline.py
```

## Project Structure
1. src/document_conversion.py: Contains the function to convert PDF pages to images.

2. src/ocr_processing.py: Contains the function to extract text from images using Tesseract OCR.

3. src/preprocessing.py: Contains text preprocessing functions.

4. src/llm_integration.py: Contains functions to initialize the language model and generate text summaries.

5. src/information_extraction.py: Contains functions to extract named entities from the text.

6. src/document_classification.py: Contains the function to classify the document.

7. src/translation.py: Contains functions for language detection and translation.

8. src/chatbot_ui.py: Contains the Streamlit UI code.

9. run_pipeline.py: Contains the main function to run the entire pipeline from the command line.

## Detailed Workflow

1. PDF to Images: The pdf_to_images function in document_conversion.py converts each page of a PDF to an image and saves it to the specified output folder.


2. OCR: The extract_text_from_image function in ocr_processing.py uses Tesseract OCR to extract text from each image.


3. Text Preprocessing: The preprocess_text function in preprocessing.py cleans the extracted text and splits it into sentences.


4. Language Detection and Translation: The detect_language function in translation.py detects the language of the preprocessed text. If the text is not in English, the translate_text function translates it to English.

5. Summarization: The llm_infer function in llm_integration.py generates a summary of the translated text using a pre-trained language model.

6. Information Extraction: The extract_information function in information_extraction.py identifies and extracts named entities from the text using a named entity recognition (NER) model.

7. Document Classification: The classify_document function in document_classification.py classifies the document into predefined categories using a zero-shot classification model.

8. Streamlit UI: The chatbot_ui.py script provides a user-friendly interface for uploading PDF documents and viewing the processed results.

## Example
To run an example with a sample PDF:

Place sample1.pdf in the ./data/input/ directory.

Run the pipeline:
```
python src/run_pipeline.py
```
    