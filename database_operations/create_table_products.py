""" Create SQLite table for products with
 id,item, grandeza, quantidade, preco_unitario,
 preco_total, data, hora, estabelecimento, cnpj and endereco."""

from database_operations.database_operations import DatabaseOperation

products_db_file = './database_operations/database/products.db'

def create_products_table():
    """ Create SQLite table for products with
         id,item, grandeza, quantidade, preco_unitario,
         preco_total, data, hora, estabelecimento, cnpj and endereco."""
    with DatabaseOperation(products_db_file) as db:
        db.db_execute("""
                    CREATE TABLE IF NOT EXISTS produtos (
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        item VARCHAR(255) NOT NULL,
                        grandeza VARCHAR(255) NOT NULL,
                        quantidade VARCHAR(255) NOT NULL,
                        preco_unitario VARCHAR(255) NOT NULL,
                        preco_total VARCHAR(255) NOT NULL,
                        data VARCHAR(255) NOT NULL,
                        hora VARCHAR(255) NOT NULL,
                        estabelecimento VARCHAR(255) NOT NULL,
                        cnpj VARCHAR(255) NOT NULL,
                        endereco VARCHAR(255) NOT NULL
                    );""")
