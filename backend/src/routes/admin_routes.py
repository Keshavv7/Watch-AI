from fastapi import APIRouter, File, UploadFile, Depends, HTTPException
from utils.gpt_setup import fine_tune_model
from utils.pdf_to_text import extract_sentences_from_pdf
from services.annotation_service import annotate_dataset
from services.azure_blob_service import save_annotated_data_to_azure, save_violations_to_azure
from services.gpt3_service import load_rules_from_azure, check_prompt_against_rules
from services.rule_generation_service import extract_rules_from_documents, save_rules_to_azure
from auth.auth import get_current_user
from models.admin import Admin

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

@router.post("/check_violations/")
async def check_violations(prompt: str, storage_connection_string: str = "YOUR_AZURE_STORAGE_CONNECTION_STRING", container_name: str = "YOUR_CONTAINER_NAME"):
    rules = load_rules_from_azure(storage_connection_string, container_name)
    violations = check_prompt_against_rules(prompt, rules)
    
    if violations:
        # Save violations to Azure Blob
        save_violations_to_azure(storage_connection_string, container_name, violations)
        
        return {"response": f"This is invalid and goes against the following guidelines: {violations}"}
    
    return {"response": "No violations found."}
