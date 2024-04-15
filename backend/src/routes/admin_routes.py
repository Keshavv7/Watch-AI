from fastapi import APIRouter, File, UploadFile
from utils.pdf_to_text import extract_sentences_from_pdf
from services.annotation_service import annotate_dataset
from services.azure_blob_service import save_annotated_data_to_azure

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
    dataset = annotate_dataset({}, {"guidelines.txt": pdf_text})
    
    # Save annotated dataset to Azure Blob Storage
    save_annotated_data_to_azure("YOUR_AZURE_STORAGE_CONNECTION_STRING", "YOUR_CONTAINER_NAME", dataset)
    
    return {"message": "PDF uploaded and dataset annotated successfully"}
