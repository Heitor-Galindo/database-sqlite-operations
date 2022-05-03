""" Select URL from database """

import re
from database_folder.database_operations import DatabaseOperation

nfce_db_file = './database_folder/database/nfce_url.db'

def get_max():
    """ Get last row id in table """
    with DatabaseOperation(nfce_db_file) as nfce_url:
        MAX_ROW = nfce_url.db_query(""" SELECT MAX(id) FROM nfce_url """)
    return MAX_ROW[0]

def get_url(ID="1"):
    """ Select URL from database """
    with DatabaseOperation(nfce_db_file) as nfce_url:
        links = nfce_url.db_query(""" SELECT * FROM nfce_url WHERE id = ? """, ID)
        row = str(links)[1:-1].split(',', maxsplit=1)
        ID = row[0]
        url = re.sub(r"\s|'","",row[1])
    return url, ID
