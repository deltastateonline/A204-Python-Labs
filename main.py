import pyodbc
import os
import logging
from dotenv import load_dotenv
load_dotenv()


def main():
    print("Start Processing ")

    getConnection()


def getConnection():

    try:
        return  pyodbc.connect(os.getenv('SQLCONNECTION'))            

    except pyodbc.Error  as  ex:
        error_message = f"Error connecting to the database: {str(ex)}"
        logging.critical(error_message)

    
    return 


if __name__ == "__main__":
    main()