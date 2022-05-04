""" Call a method to add a new url to nfce url table """

from os.path import exists as file_exists
from sqlite3 import Error
from database_operations.database_operations import DatabaseOperation
from database_operations.create_table_nfce_url import create_nfce_table

nfce_db_file = './database_operations/database/nfce_url.db'
QR_CODE_URL = './database_operations/database/QR_CODE_URL.txt'

def nfce_database():
    """ Call a method to add a new url to nfce url table """
    with open(QR_CODE_URL, 'r', encoding='utf-8') as url_file:

        if not file_exists(nfce_db_file):
            print("NFCE database not found! Creating...")
            create_nfce_table()
            print("NFCE database created!")

        lines = url_file.readlines()
        length = len(lines)

        try:
            print("Inserting qr-code links into nfce table...")
            with DatabaseOperation(nfce_db_file) as db:
                for i in range(length):
                    line = lines[i].strip()
                    db.db_execute("""INSERT INTO nfce_url (url) VALUES (?); """, (line, ))
            print(f"Finish. {length} qr-code links added to table!")
        except Error as e:
            print("Query failed!")
            print(e)
