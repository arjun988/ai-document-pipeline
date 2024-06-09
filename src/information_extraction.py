from transformers import pipeline

def extract_information(text):
    model_name = "dbmdz/bert-large-cased-finetuned-conll03-english"
    nlp = pipeline("ner", model=model_name, tokenizer=model_name)
    ner_results = nlp(text)

    entities = {}
    for entity in ner_results:
        entity_type = entity['entity']
        entity_text = entity['word']
        if entity_type in entities:
            entities[entity_type].append(entity_text)
        else:
            entities[entity_type] = [entity_text]

    return entities
