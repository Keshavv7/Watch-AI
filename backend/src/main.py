from services.azure_connection_service import fetch_documents_from_azure
from fastapi import FastAPI
import json
import openai
from services.rule_extraction_service import extract_rules_from_documents

# Initialize OpenAI ChatGPT API with fine-tuned model
openai.api_key = "YOUR_OPENAI_API_KEY"
model_name = "gpt-3.5-turbo"  # Fine-tuned model name

app = FastAPI()

@app.post("/update_rules/")
async def update_rules():
    storage_connection_string = "YOUR_AZURE_STORAGE_CONNECTION_STRING"
    container_name = "YOUR_CONTAINER_NAME"
    
    # Fetch documents from Azure Blob Storage
    documents = fetch_documents_from_azure(storage_connection_string, container_name)
    
    # Extract and generate rules
    rules = extract_rules_from_documents(documents)
    
    # Save rules to database or return for further processing
    # For demonstration, we are returning the rules as JSON
    return json.dumps(rules)


@app.post("/generate_response/")
async def generate_response(prompt: str):
    response = openai.Completion.create(
        engine=model_name,
        prompt=prompt,
        max_tokens=150  # Adjust as needed
    )
    
    return {"response": response.choices[0].text.strip()}