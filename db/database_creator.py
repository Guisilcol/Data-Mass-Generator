#Make sure the "requests" library is installed. https://requests-docs-pt.readthedocs.io/pt_BR/latest/user/quickstart.html

import os
import sqlite3
import requests


DATABASE_FILE = './database.db'
DATABASE_CREATION_SCRIPT = 'https://pastebin.com/raw/u75M5qUz'

def main():
    
    # Wait for user confirmation to continue process
    while True:
        option = input("O processo a seguir irá resetar o banco de dados. Deseja continuar? S/N  ").lower().strip()
        if option == 'n':
            exit()
        elif option == 's':
            break

    # Make the request to get the table creation script and delete the .db file from the folder
    
    try:
        response = requests.get(DATABASE_CREATION_SCRIPT)
        if os.path.exists(DATABASE_FILE):
            os.remove(DATABASE_FILE)
    except Exception as exception: 
        print('Error: ' , exception)
        exit()
    
    # Transforms each CREATE TABLE statement into an array and executes one by one
    script = response.text.split(';')
    
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    for statement in script:
        cursor.execute(statement)

    cursor.close
    connection.close

if __name__ == "__main__":
    main()