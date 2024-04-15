from fastapi import FastAPI
import openai
import json
from services.azure_connection_service import fetch_documents_from_azure
from services.rule_extraction_service import extract_rules_from_documents
from routes.user_routes import router as user_router
from routes.admin_routes import router as admin_router

# Initialize OpenAI ChatGPT API with fine-tuned model
openai.api_key = "YOUR_OPENAI_API_KEY"
model_name = "gpt-3.5-turbo"  # Fine-tuned model name

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(admin_router, prefix="/admin", tags=["admin"])

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
