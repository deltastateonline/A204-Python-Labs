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
    suffix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    suffix = ''

    with getServiceClient() as serviceClient :
        try:
            containerName = f"{os.getenv('BLOBCONTAINER')}{suffix}"
            logging.info(f"Creating container -  {containerName}")

            #if serviceClient.get_container_client(containerName) :

            container_client = serviceClient.create_container(containerName)
            logging.info(f"Container Created {containerName}")

            blobClient = serviceClient.get_blob_client(container=containerName, blob="phones.png")

            logging.info(f"Uploading File to {containerName}")

            with open(file="data\\01-head1.png", mode="rb") as data:
                blobClient.upload_blob(data)


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