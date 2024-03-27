from azure.storage.blob import BlobServiceClient

def fetch_documents_from_azure(storage_connection_string, container_name):
    blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    
    documents = {}
    
    for blob in container_client.list_blobs():
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob.name)
        documents[blob.name] = blob_client.download_blob().readall().decode('utf-8')
    
    return documents
