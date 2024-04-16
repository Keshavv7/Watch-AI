from azure.storage.blob import BlobServiceClient
import json

def save_annotated_data_to_azure(storage_connection_string, container_name, dataset):
    blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    
    # Convert dataset to JSON format
    data_json = {"data": dataset}
    data_str = json.dumps(data_json)
    
    # Upload data to Azure Blob Storage
    blob_client = container_client.get_blob_client("dataset.json")
    blob_client.upload_blob(data_str, overwrite=True)


def save_violations_to_azure(storage_connection_string: str, container_name: str, violations):
    blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    
    # Convert violations to JSON format
    violations_json = {"violations": violations}
    violations_str = json.dumps(violations_json)
    
    # Upload violations to Azure Blob Storage
    blob_client = container_client.get_blob_client("violations.json")
    blob_client.upload_blob(violations_str, overwrite=True)