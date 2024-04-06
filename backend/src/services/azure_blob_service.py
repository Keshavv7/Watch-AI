from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def save_annotated_data_to_azure(storage_connection_string, container_name, dataset):
    blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    
    for data in dataset:
        blob_name = f"{data['doc_name']}_annotated.txt"
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        
        # Convert data to string format
        annotated_data = f"{data['interaction']},{data['label']}\n"
        
        # Upload annotated data to Azure Blob
        blob_client.upload_blob(annotated_data, overwrite=True)
