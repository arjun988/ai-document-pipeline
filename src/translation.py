from transformers import MarianMTModel, MarianTokenizer
from langdetect import detect

def detect_language(text):
    return detect(text)

def translate_text(text, src_lang, tgt_lang="en"):
    model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    translated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))
    tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)[0]
    return tgt_text

def format_translation_output(original_text, translated_text, src_lang, tgt_lang):
    return (
        f"### Translation from {src_lang} to {tgt_lang}:\n"
        f"**Original Text ({src_lang}):**\n{original_text}\n\n"
        f"**Translated Text ({tgt_lang}):**\n{translated_text}"
    )
