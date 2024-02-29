import sys
import os
import logging
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.core.exceptions import AzureError
import datetime
load_dotenv()


logging.basicConfig(level=logging.INFO)

def main():
    print("Start Processing ")
    suffix1 = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    suffix = ''

    with getServiceClient() as serviceClient :
        try:
            containerName = f"{os.getenv('BLOBCONTAINER')}{suffix}"
            logging.info(f"Creating container -  {containerName}")

            container_client = serviceClient.get_container_client(containerName)

            
            logging.info(f"Container Created {containerName}")

            blobClient = serviceClient.get_blob_client(container=containerName, blob=f"backofhouse{suffix1}.jpg" )

            #container_client.upload_blob() can upload blob from container client

            logging.info(f"Uploading File to {containerName}")

            with open(file="data\\backofhouse.jpg", mode="rb") as data:
                blobClient.upload_blob(data , tags={"createdBy":"Python"}, overwrite=True, metadata={"Dept":"IT"})


        except AzureError as ex:
            error_message = f"Error creating container:\n{str(ex)}"
            logging.critical(error_message)


def getServiceClient():

    try:
        return BlobServiceClient.from_connection_string(os.getenv('BLOBCONNECTION'))          

    except AzureError  as  ex:
        error_message = f"Error connecting to blob: {str(ex)}"
        # logging.critical(error_message)
        sys.exit()

    
     


if __name__ == "__main__":
    main()