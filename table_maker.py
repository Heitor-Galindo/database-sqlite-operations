""" Table Maker """

import pandas as pd

FULL_TABLE = './full_table.csv'

nome_item = []
quantidade_item = []
quantidade_grandeza = []
preco_unidade = []
preco_pago = []
nome_mercado = []
cnpj_mercado = []
endereco_mercado = []
data = []
hora = []

def table_maker ():

    """ Table Maker """

    csv_table = pd.DataFrame({
        'Item': nome_item,
        'Grandeza': quantidade_grandeza,
        'Quantidade': quantidade_item,
        'Preço unitario': preco_unidade,
        'Preço total': preco_pago,
        'Data': data,
        'Hora': hora,
        'Estabelecimento': nome_mercado,
        'CNPJ': cnpj_mercado,
        'Endereço': endereco_mercado
    })
    csv_table.to_csv(FULL_TABLE)
