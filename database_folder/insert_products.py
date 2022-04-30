""" Create SQLite database for products """

from database_connection import DatabaseOperation

nome_item = 12
quantidade_grandeza = 12
quantidade_item = 12
preco_unidade = 12
preco_pago = 12
data = 12
hora = 12
nome_mercado = 12
cnpj_mercado = 12
endereco_mercado = 12

PRODUCT_INFO = (nome_item, quantidade_grandeza,
                quantidade_item, preco_unidade,
                preco_pago, data,
                hora, nome_mercado,
                cnpj_mercado, endereco_mercado)

with DatabaseOperation('./database_folder/products.db') as db:
    db.db_executemany(""" INSERT INTO produtos (item, grandeza,
                            quantidade, preco_unitario,
                            preco_total, data,
                            hora, estabelecimento,
                            cnpj, endereco)
                            VALUES (?,?,?,?,?,?,?,?,?,?); """, [PRODUCT_INFO])
