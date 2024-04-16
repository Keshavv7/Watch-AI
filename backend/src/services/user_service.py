from azure.storage.blob import BlobServiceClient
import json
from models.user import User

def create_user(storage_connection_string: str, container_name: str, user: User):
    blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    
    # Convert user data to JSON format
    user_json = user.dict()
    user_str = json.dumps(user_json)
    
    # Upload user data to Azure Blob Storage
    blob_client = container_client.get_blob_client(f"user_{user.username}.json")
    blob_client.upload_blob(user_str, overwrite=True)


def update_user_violations_to_azure(storage_connection_string: str, container_name: str, username: str, violations_count: int):
    blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    
    # Load existing users
    blob_client = container_client.get_blob_client("users.json")
    users_str = blob_client.download_blob().readall().decode('utf-8')
    
    users = json.loads(users_str)
    
    # Update violations count for the user
    for user in users:
        if user["username"] == username:
            user["rules_violated"] += violations_count
            break
    
    # Upload updated users to Azure Blob Storage
    blob_client.upload_blob(json.dumps(users), overwrite=True)