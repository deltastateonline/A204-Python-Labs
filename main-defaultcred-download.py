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
    
    clientCreds : DefaultAzureCredential = DefaultAzureCredential()
    
    print(os.getenv("BC"))

    with getServiceClient(os.getenv("BLOBURL"), clientCreds) as serviceClient :
        try:
            containerName = f"{os.getenv('BC')}{suffix}"
            logging.info(f"Getting Container Client -  {containerName}")

            container_client = serviceClient.get_container_client(containerName)

            for x in container_client.list_blob_names():
                downloadPath = f"movies\\{x}"
                print(f"Downloading blobname : {x}")
                with open(file= downloadPath , mode="wb") as df:
                    df.write(container_client.download_blob(x).readall())
                
                
            

        except AzureError as ex:
            error_message = f"Error creating container:\n{str(ex)}"
            logging.critical(error_message)


def getServiceClient(account_url : str, client_creds: DefaultAzureCredential):

    try:
        return BlobServiceClient(account_url=account_url , credential=client_creds)        

    except AzureError  as  ex:
        error_message = f"Error connecting to blob: {str(ex)}"
        # logging.critical(error_message)
        sys.exit()

    
     


if __name__ == "__main__":
    main()