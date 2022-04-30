""" Select all links from nfce table """

from database_connection import DatabaseOperation

with DatabaseOperation('./database_folder/nfce_url.db') as db:
    products = db.db_query(""" SELECT url FROM nfce_url """)
    print(products)
