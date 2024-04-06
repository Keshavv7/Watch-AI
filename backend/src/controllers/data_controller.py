from services.dataset_preparation_service import prepare_dataset
from services.annotation_service import annotate_dataset
from services.azure_blob_service import save_annotated_data_to_azure
from services.azure_connection_service import fetch_documents_from_azure
from azure.storage.blob import BlobServiceClient

def process_data_and_save_to_azure(storage_connection_string, container_name):
    # Fetch documents from Azure Blob
    documents = fetch_documents_from_azure(storage_connection_string, container_name)
    
    # Prepare dataset
    dataset = prepare_dataset(documents)
    
    # Annotate dataset
    annotated_dataset = annotate_dataset(dataset)
    
    # Save annotated data to Azure Blob
    save_annotated_data_to_azure(storage_connection_string, container_name, annotated_dataset)
