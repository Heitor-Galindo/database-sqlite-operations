""" . """
from database_folder.select_nfce_url import get_max, get_url

def select():
    """ . """
    max_row = get_max()
    next_row = get_url()[1]
    print(f"max row: {max_row}", type(max_row))
    print(f"next row: {next_row}", type(next_row), "\n")

    while int(next_row) <= max_row:

        print(f"max row: {max_row}", type(max_row))
        print(f"next row: {next_row}", type(next_row))

        actual_row = get_url(str(next_row)[0])
        print(f"actual row: {actual_row[1]}", type(actual_row), "\n")
        next_row = 1 + int(next_row)

select()

def teste():
    """ . """
    x = 11
    y = 1

    while y <= x:
        print(y)
        y = 1 + y
