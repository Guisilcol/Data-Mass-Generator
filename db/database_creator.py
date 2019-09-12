#Make sure the "requests" library is installed. https://requests-docs-pt.readthedocs.io/pt_BR/latest/user/quickstart.html

import os
import sqlite3
import requests

DATABASE_FILE = './database.db'
DATABASE_CREATION_SCRIPT = 'https://pastebin.com/raw/u75M5qUz'
DATABASE_INSERT_SCRIPT = 'https://pastebin.com/raw/FbWpfg2Y'

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
        response_database_creation_script = requests.get(DATABASE_CREATION_SCRIPT)
        response_database_insert_script = requests.get(DATABASE_INSERT_SCRIPT)
        if os.path.exists(DATABASE_FILE):
            os.remove(DATABASE_FILE)
    except Exception as exception: 
        print('Error: ' , exception)
        exit()
    
    # Transforms each statement into an array and executes one by one

    script = response_database_creation_script.text + response_database_insert_script.text
    script = script.split(';')
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    script.remove("")

    for statement in script:
        print(statement + ";")
        cursor.execute(statement + ";")

    connection.commit()
    cursor.close
    connection.close

if __name__ == "__main__":
    main()