import openai

def annotate_dataset(dataset, documents):
    dataset = []
    model_name = "gpt-3.5-turbo"  # Fine-tuned model name (alternatively use "text-davinci-002" for general responses)
    
    for doc_name, text in documents.items():
        # Split the text into sentences or paragraphs
        sentences = text.split("\n")  # Assuming each line represents a sentence
        
        for sentence in sentences:

            # Fine-tuned GPT-3.5 for context-based rule adherence
            prompt = f"Adhere to monitoring rule for responsible use of AI for the document {doc_name}. The content should align with: {sentence}"
            response = openai.Completion.create(
                engine=model_name,
                prompt=prompt,
                max_tokens=300  # Adjust as needed
            )
            
            # Create dataset entry
            entry = {
                "messages": [
                    {"role": "system", "content": "You are an AI assistant providing information based on organizational guidelines."},
                    {"role": "user", "content": sentence},
                    {"role": "assistant", "content": response.choices[0].text.strip()}
                ]
            }
            
            dataset.append(entry)
    
    return dataset
