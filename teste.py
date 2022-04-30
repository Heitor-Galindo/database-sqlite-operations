""" Select all links from nfce table """
import re
from database_folder.database_connection import DatabaseOperation

with DatabaseOperation('./database_folder/nfce_url.db') as db:
    for link in db:
        link = db.db_query(""" SELECT url FROM nfce_url """)
        print(link)
