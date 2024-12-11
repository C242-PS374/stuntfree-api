from google.cloud import storage
import os

def upload_image_to_gcs(bucket_name: str, source_file_name: bytes, destination_blob_name: str):
    """Uploads an image to Google Cloud Storage and returns the URL."""
    
    # Initialize a storage client
    storage_client = storage.Client()
    
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    
    blob.upload_from_string(source_file_name, content_type='image/jpeg')
    
    blob.make_public()
    
    return blob.public_url