import sys
import os
import logging
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.core.exceptions import AzureError
import datetime
load_dotenv()


#logging.basicConfig(level=logging.INFO)
#logging.getLogger(__name__).setLevel(logging.INFO)


def main():
    print("Start Processing ")
    suffix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    suffix = ''

    with getServiceClient() as serviceClient :
        try:
            containerName = f"{os.getenv('BLOBCONTAINER')}{suffix}"
            logging.info(f"Getting  container -  {containerName}")

            container_client = serviceClient.get_container_client(containerName)            

            for x in container_client.list_blob_names():
                downloadPath = f"data\\{x}"
                with open(file= downloadPath , mode="wb") as df:
                    df.write(container_client.download_blob(x).readall())
                #blob_client.download_blob() 




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