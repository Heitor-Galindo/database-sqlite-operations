""" Create SQLite table for nfce links
 with id and url, all url will be unique.  """

from database_connection import DatabaseOperation

with DatabaseOperation('./database_folder/nfce_url.db') as db:
    db.db_execute("""
               CREATE TABLE IF NOT EXISTS nfce_url (
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   url VARCHAR(255) NOT NULL UNIQUE
               );
               """)
