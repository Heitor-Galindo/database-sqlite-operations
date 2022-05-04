""" Call a method to add new products to products table """

from os.path import exists as file_exists
from database_operations.database_operations import DatabaseOperation
from database_operations.create_table_products import create_products_table

products_db_file = './database_operations/database/products.db'

def insert_item(ITEM):
    """ Call a method to add new products to products table """

    if not file_exists(products_db_file):
        create_products_table()

    with DatabaseOperation(products_db_file) as products_table:
        products_table.db_executemany("""INSERT INTO produtos
                                        (item,
                                        grandeza,
                                        quantidade,
                                        preco_unitario,
                                        preco_total,
                                        data,
                                        hora,
                                        estabelecimento,
                                        cnpj,
                                        endereco)
                                        VALUES (?,?,?,?,?,?,?,?,?,?);""", [ITEM])
