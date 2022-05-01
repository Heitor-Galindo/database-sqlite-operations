""" Call a method to add a new url to nfce url table """

from database_connection import DatabaseOperation

URL = ('http://www.fazenda.pr.gov.br/nfce/qrcode?p=4122030147286100072'
      '0650140002039781843966740|2|1|1|DE2BE4479B6E8B0E62BB1BA887E6CE3834B103C5')

with DatabaseOperation('./database_folder/nfce_url.db') as db:
    db.db_execute(""" INSERT INTO nfce_url (url)
                      VALUES (?); """, (URL, ))
