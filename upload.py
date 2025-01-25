from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Get the connection string and container name from environment variables
CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")  # Ensure to set this in your .env file
CONTAINER_NAME = "vmgit"  # Replace with your container name

# Function to upload a file to Azure Blob Storage
def upload_file_to_blob(local_file_path, blob_name):
    try:
        # Create a BlobServiceClient object
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

        # Get the container client
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)

        # Check if the container exists
        try:
            container_client.get_container_properties()  # If the container doesn't exist, this will raise an exception
        except Exception:
            # Create the container if it doesn't exist
            container_client.create_container()
            print(f"Container '{CONTAINER_NAME}' created.")

        # Get the blob client for the specified blob
        blob_client = container_client.get_blob_client(blob_name)

        # Upload the file to the blob
        with open(local_file_path, "rb") as file:
            blob_client.upload_blob(file, overwrite=True)

        print(f"File '{local_file_path}' successfully uploaded to blob '{blob_name}' in container '{CONTAINER_NAME}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Path to the local file to upload
    local_file_path = "C:/Users/janih/ainews/test.txt"  # Replace with your local file path

    # Name of the blob in Azure Storage
    blob_name = os.path.basename(local_file_path)  # Use the file name as the blob name

    # Upload the file
    upload_file_to_blob(local_file_path, blob_name)
