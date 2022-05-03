""" . """

from database_folder.select_nfce_url import get_max, get_url

def select():
    """ . """
    max_row = get_max()
    next_row = get_url()[1]

    while int(next_row) <= int(max_row):

        print(f"max row: {max_row}")
        print(f"next row: {next_row}")

        url_link = get_url(str(next_row)[0])
        print(f"actual row: {url_link[1]}")
        next_row = 1 + int(next_row)

select()

def teste():
    """ . """
    x = 11
    y = 1

    while y <= x:
        print(y)
        y = 1 + y
