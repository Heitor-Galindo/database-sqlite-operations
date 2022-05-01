""" Call a method to add new products to products table """

from database_connection import DatabaseOperation

nome_item = []
quantidade_grandeza = []
quantidade_item = []
preco_unidade = []
preco_pago = []
data = []
hora = []
nome_mercado = []
cnpj_mercado = []
endereco_mercado = []

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
