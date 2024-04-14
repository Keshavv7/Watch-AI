from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import json

def save_annotated_data_to_azure(storage_connection_string, container_name, dataset):
    blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    
    # Convert dataset to JSON format
    data_json = {"data": data}
    data_str = json.dumps(data_json)
    
    # Upload data to Azure Blob Storage
    blob_client = container_client.get_blob_client("dataset.json")
    blob_client.upload_blob(data_str, overwrite=True)
