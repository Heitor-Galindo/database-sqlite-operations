""" Call a method to add a new url to nfce url table """

from os.path import exists as file_exists
from sqlite3 import Error
from database_folder.database_operations import DatabaseOperation
from database_folder.create_table_nfce_url import create_nfce_table

nfce_db_file = './database_folder/database/nfce_url.db'
QR_CODE_URL = './database_folder/database/QR_CODE_URL.txt'

def nfce_database():
    """ Call a method to add a new url to nfce url table """
    with open(QR_CODE_URL, 'r', encoding='utf-8') as url_file:

        if not file_exists(nfce_db_file):
            create_nfce_table()

        lines = url_file.readlines()
        length = len(lines)

        try:
            with DatabaseOperation(nfce_db_file) as db:
                for i in range(length):
                    line = lines[i].strip()
                    db.db_execute("""INSERT INTO nfce_url (url) VALUES (?); """, (line, ))
        except Error as e:
            print(e)
