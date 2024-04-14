def extract_rules_from_documents(documents):
    rules = {}
    
    for doc_name, text in documents.items():
        # Fine-tuned GPT-3.5 for context-based rule adherence
        prompt = f"Adhere to monitoring rule for {doc_name}. The content should align with: {text}"
        response = openai.Completion.create(
            engine=model_name,
            prompt=prompt,
            max_tokens=300  # Adjust as needed
        )
        
        rules[doc_name] = response.choices[0].text.strip()
    
    return rules