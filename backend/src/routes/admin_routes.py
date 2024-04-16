from fastapi import APIRouter, File, UploadFile, Depends, HTTPException
from azure.storage.blob import BlobServiceClient
from utils.gpt_setup import fine_tune_model
from utils.pdf_to_text import extract_sentences_from_pdf
from services.annotation_service import annotate_dataset
from services.azure_blob_service import save_annotated_data_to_azure
from services.gpt3_service import load_rules_from_azure
from services.rule_generation_service import extract_rules_from_documents, save_rules_to_azure
from auth.auth import get_current_user
from models.admin import Admin
import json

router = APIRouter()


@router.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    # Save PDF to backend/public/uploads
    file_location = f"backend/public/uploads/{file.filename}"
    with open(file_location, "wb") as buffer:
        buffer.write(file.file.read())
    
    # Extract text from PDF
    pdf_text = extract_sentences_from_pdf(file_location)
    
    # Annotate dataset
    dataset = annotate_dataset({"guidelines.txt": pdf_text})

    # Fine-tune model
    checkpoint = fine_tune_model(dataset, "gpt-3.5-turbo")

    # Save model to Azure Blob Storage
    
    
    # Save annotated dataset to Azure Blob Storage
    save_annotated_data_to_azure("YOUR_AZURE_STORAGE_CONNECTION_STRING", "YOUR_CONTAINER_NAME", dataset)
    
    return {"message": "PDF uploaded and dataset annotated successfully"}


@router.post("/update_rules/")
async def update_rules(file: UploadFile = File(...), current_user: Admin = Depends(get_current_user)):
    # Save PDF to backend/public/uploads
    file_location = f"backend/public/uploads/{file.filename}"
    with open(file_location, "wb") as buffer:
        buffer.write(file.file.read())
    
    # Extract rules from the PDF
    documents = {"guidelines.txt": open(file_location, 'r').read()}
    rules = extract_rules_from_documents(documents)
    
    # Save rules to Azure Blob
    save_rules_to_azure("YOUR_AZURE_STORAGE_CONNECTION_STRING", "YOUR_CONTAINER_NAME", rules)
        
    
    return {"message": "PDF uploaded and rules generated and saved successfully"}


@router.post("/insert_rule/")
async def insert_rule(rule: dict, storage_connection_string: str = "YOUR_AZURE_STORAGE_CONNECTION_STRING", container_name: str = "YOUR_CONTAINER_NAME"):
    # Load existing rules
    rules = load_rules_from_azure(storage_connection_string, container_name)
    
    # Insert new rule
    rules.append(rule)
    
    # Save updated rules to Azure Blob
    save_rules_to_azure(storage_connection_string, container_name, rules)
    
    return {"message": "Rule inserted successfully"}

@router.get("/view_rules/")
async def view_rules(storage_connection_string: str = "YOUR_AZURE_STORAGE_CONNECTION_STRING", container_name: str = "YOUR_CONTAINER_NAME"):
    rules = load_rules_from_azure(storage_connection_string, container_name)
    return {"rules": rules}

@router.put("/update_rule/")
async def update_rule(updated_rule: dict, storage_connection_string: str = "YOUR_AZURE_STORAGE_CONNECTION_STRING", container_name: str = "YOUR_CONTAINER_NAME"):
    # Load existing rules
    rules = load_rules_from_azure(storage_connection_string, container_name)
    
    # Update rule
    for rule in rules:
        if rule["rule"] == updated_rule["rule"]:
            rule.update(updated_rule)
            break
    
    # Save updated rules to Azure Blob
    save_rules_to_azure(storage_connection_string, container_name, rules)
    
    return {"message": "Rule updated successfully"}

@router.delete("/delete_rule/")
async def delete_rule(rule_to_delete: str, storage_connection_string: str = "YOUR_AZURE_STORAGE_CONNECTION_STRING", container_name: str = "YOUR_CONTAINER_NAME"):
    # Load existing rules
    rules = load_rules_from_azure(storage_connection_string, container_name)
    
    # Delete rule
    rules = [rule for rule in rules if rule["rule"] != rule_to_delete]
    
    # Save updated rules to Azure Blob
    save_rules_to_azure(storage_connection_string, container_name, rules)
    
    return {"message": "Rule deleted successfully"}

@router.get("/get_user_violations/")
async def get_user_violations(storage_connection_string: str = "YOUR_AZURE_STORAGE_CONNECTION_STRING", container_name: str = "YOUR_CONTAINER_NAME"):
    blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    
    # Load existing users
    blob_client = container_client.get_blob_client("users.json")
    users_str = blob_client.download_blob().readall().decode('utf-8')
    
    users = json.loads(users_str)
    
    # Get violations count for the user
    for user in users:
        return {"username": user["username"], "rules_violated": user["rules_violated"]}
    
    return {"message": "No violations found"}
