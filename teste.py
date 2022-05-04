""" . """
from database_folder.select_nfce_url import get_max, get_url

def select():
    """ . """
    max_row = get_max()
    current_row = get_url()
    for row in range(int(current_row[1]), max_row):
        link = get_url(str(row))
        print(link[0])

select()
