from azure.storage.blob import BlobServiceClient
import json
from models.admin import Admin

def create_admin(storage_connection_string: str, container_name: str, admin: Admin):
    blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    
    # Convert admin data to JSON format
    admin_json = admin.dict()
    admin_str = json.dumps(admin_json)
    
    # Upload admin data to Azure Blob Storage
    blob_client = container_client.get_blob_client(f"admin_{admin.username}.json")
    blob_client.upload_blob(admin_str, overwrite=True)
