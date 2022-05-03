""" Select URL from database """

import re
from database_folder.database_operations import DatabaseOperation

nfce_db_file = './database_folder/database/nfce_url.db'
readed_rows = []

def get_url():
    """ Select URL from database """
    with DatabaseOperation(nfce_db_file) as nfce_url:
        links = nfce_url.db_query(""" SELECT * FROM nfce_url """)
        row = str(links)[1:-1].split(',', maxsplit=1)
        readed_rows.append(row[0])
        url = re.sub(r"\s|'","",row[1])
        return url
