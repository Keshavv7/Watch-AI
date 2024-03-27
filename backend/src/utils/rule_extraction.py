import spacy
import openai

# Initialize SpaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Initialize OpenAI ChatGPT API
openai.api_key = "YOUR_OPENAI_API_KEY"

def extract_rules_from_documents(documents):
    rules = {}
    
    for doc_name, text in documents.items():
        # SpaCy for Named Entity Recognition
        doc = nlp(text)
        entities = [ent.text for ent in doc.ents if ent.label_ in ['ORG', 'LAW', 'POLICY']]
        
        # ChatGPT for context-based rule generation
        prompt = f"Generate monitoring rule for {doc_name}. Relevant entities: {', '.join(entities)}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=50
        )
        
        rules[doc_name] = response.choices[0].text.strip()
    
    return rules
