import openai
import re
import json
from azure.storage.blob import BlobServiceClient

def extract_rules_from_documents(documents):
    rules = []

    for doc_name, text in documents.items():
        # Split the text into sentences or paragraphs
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)

        for sentence in sentences:
            # Fine-tuned GPT-3.5 for context-based rule adherence
            prompt = f"Formulate a rule for responsible use of AI based on the document {doc_name}. 
            The content should align with: {sentence}. 
            Only respond with the rule and do not add any unnecessary leading or trailing text. "
            response = openai.Completion.create(
                engine="gpt-3.5-turbo",
                prompt=prompt,
                max_tokens=100  # Adjust as needed
            )
            
            # Extract the rule from the response
            rule = response.choices[0].text.strip()
            if rule:
                rules.append({"document": doc_name, "rule": rule})
    
    return rules

def save_rules_to_azure(storage_connection_string: str, container_name: str, rules):
    blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    
    # Convert rules to JSON format
    rules_json = {"rules": rules}
    rules_str = json.dumps(rules_json)
    
    # Upload rules to Azure Blob Storage
    blob_client = container_client.get_blob_client("rules.json")
    blob_client.upload_blob(rules_str, overwrite=True)
