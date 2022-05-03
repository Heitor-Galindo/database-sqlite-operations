""" Create SQLite table for nfce links
 with id and url, all url will be unique.  """

from database_folder.database_operations import DatabaseOperation

nfce_db_file = './database_folder/database/nfce_url.db'

def create_nfce_table():

    """ Create SQLite table for nfce links
         with id and url, all url will be unique.  """

    with DatabaseOperation(nfce_db_file) as db:
        db.db_execute("""
                CREATE TABLE IF NOT EXISTS nfce_url (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    url VARCHAR(255) NOT NULL UNIQUE
                );
                """)
