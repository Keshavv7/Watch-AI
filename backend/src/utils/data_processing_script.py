# Import required modules
from services.dataset_preparation_service import prepare_dataset
from services.annotation_service import annotate_dataset
from services.azure_blob_service import save_annotated_data_to_azure
from services.azure_connection_service import fetch_documents_from_azure

def process_data_and_save_to_azure(storage_connection_string, container_name, file_path):
    # Step 1: Read data from guidelines.txt
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Convert text data to dictionary format (assuming each line contains a separate guideline)
    documents = {'guidelines.txt': text}
    
    # Step 2: Prepare dataset
    dataset = prepare_dataset(documents)
    
    # Step 3: Annotate datasetexi
    annotated_dataset = annotate_dataset(dataset)
    
    # Step 4: Save annotated data to Azure Blob
    save_annotated_data_to_azure(storage_connection_string, container_name, annotated_dataset)

if __name__ == "__main__":
    # Azure Blob Storage connection string and container name
    STORAGE_CONNECTION_STRING = "YOUR_AZURE_STORAGE_CONNECTION_STRING"
    CONTAINER_NAME = "YOUR_CONTAINER_NAME"
    
    # File path for guidelines.txt
    FILE_PATH = "path/to/guidelines.txt"
    
    # Process data and save to Azure
    process_data_and_save_to_azure(STORAGE_CONNECTION_STRING, CONTAINER_NAME, FILE_PATH)
