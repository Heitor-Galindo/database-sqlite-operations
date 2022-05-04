""" Web-Scrapper """

import re
from bs4 import BeautifulSoup
import requests

from database_folder.select_nfce_url import get_max, get_url
from database_folder.insert_products import insert_item

nfce_db_file = './database_folder/database/nfce_url.db'
products_db_file = './database_folder/database/products.db'

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

def web_scraper ():

    """ Web-Scrapper funtion """

    max_row = get_max()
    current_row = get_url()
    for row in range(int(current_row[1]), max_row):
        link = get_url(str(row))

        url = link[0]

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'
            }

        page = requests.get(url, headers=headers).content
        soup = BeautifulSoup(page, "html.parser")

        for item in soup.find_all("tr"):
            linha = item.findChildren("span")

            nome_item.append(re.sub(r"(\sKg.*$)","",(linha[0].text)))
            quantidade_item.append(re.sub(r"\s+","",(linha[2].text)).split(":")[1])
            quantidade_grandeza.append(re.sub(r"\s+","",(linha[3].text)).split(":")[1])
            preco_unidade.append(re.sub(r"\s+","",(linha[4].text)).split(":")[1])
            preco_pago.append(linha[5].text)

            dados_cadastrais = soup.find(class_="txtCenter").find_all(class_="text")
            nome_mercado.append(soup.find("div", class_="txtTopo").text)
            cnpj_mercado.append(re.sub(r"CNPJ\:|\s*","",(dados_cadastrais[0].text)))
            endereco_mercado.append(re.sub("\n\t*","",(dados_cadastrais[1].text)))

            emissao = (re.sub(r"[A-Z]+|[a-z]+|\-|\n","",(soup.find("ul").find_all("strong"))[3].next_sibling)).split(" ")
            data.append(emissao[0])
            hora.append(emissao[1])

    lenght = len(nome_item)
    for i in range(lenght):
        ITEM = (nome_item[i],
                quantidade_grandeza[i],
                quantidade_item[i],
                preco_unidade[i],
                preco_pago[i],
                data[i],
                hora[i],
                nome_mercado[i],
                cnpj_mercado[i],
                endereco_mercado[i])

        insert_item(ITEM = ITEM)

web_scraper()
