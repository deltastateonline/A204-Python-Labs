import sys
import os
import logging
from dotenv import load_dotenv
from azure.identity import ClientSecretCredential , DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.core.exceptions import AzureError
import datetime
load_dotenv()


logging.basicConfig(level=logging.INFO)

def main():
    print("Start Processing ")
    suffix1 = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    suffix = '1'
    
    clientCreds : ClientSecretCredential = ClientSecretCredential(os.getenv("TENANTID"), 
                                                                  os.getenv("CLIENTID"),
                                                                  os.getenv("CLIENTSECRET"))
    
    print(os.getenv("BC"))
    """
    https://staiwclientapp001.blob.core.windows.net/movies/IMG_1834.JPG
    https://staiwclientapp001.blob.core.windows.net/movies1/backofhouse20240301104833.jpg
    """

    #clientCreds = DefaultAzureCredential()

    with getServiceClient(os.getenv("BLOBURL"), clientCreds) as serviceClient :
        try:
            containerName = f"{os.getenv('BC')}{suffix}"
            logging.info(f"Creating container -  {containerName}")                   

            blobClient = serviceClient.get_blob_client(container=containerName, blob=f"backofhouse{suffix1}.jpg" )

            logging.info(f"Uploading File to {containerName}")

            with open(file="data\\backofhouse.jpg", mode="rb") as data:
                blobClient.upload_blob(data , tags={"createdBy":"Python"} , blob_type="BlockBlob")
            

        except AzureError as ex:
            error_message = f"Error Uploading Blob:\n{str(ex)}"
            logging.critical(error_message)


def getServiceClient(account_url : str, client_creds: ClientSecretCredential):

    try:
        return BlobServiceClient(account_url=account_url , credential=client_creds)
        #return BlobServiceClient.from_connection_string(os.getenv('BLOBCONNECTION'))          

    except AzureError  as  ex:
        error_message = f"Error connecting to blob: {str(ex)}"
        # logging.critical(error_message)
        sys.exit()

    
     


if __name__ == "__main__":
    main()