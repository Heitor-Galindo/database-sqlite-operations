""" Web-Scrapper """

import re
from bs4 import BeautifulSoup
import requests

from database_folder.database_connection import DatabaseOperation



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

    with DatabaseOperation('./database_folder/nfce_url.db') as db:
        link = db.db_query(""" SELECT url FROM nfce_url """)
        print(link)

            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'
                }

            page = requests.get(link, headers=headers).content
            soup = BeautifulSoup(page, "html.parser")

            for item in soup.find_all("tr"):
                linha = item.findChildren("span")

                nome_item.append(re.sub("(\sKg.*$)","",(linha[0].text)))
                quantidade_item.append(re.sub("\s+","",(linha[2].text)).split(":")[1])
                quantidade_grandeza.append(re.sub("\s+","",(linha[3].text)).split(":")[1])
                preco_unidade.append(re.sub("\s+","",(linha[4].text)).split(":")[1])
                preco_pago.append(linha[5].text)

                dados_cadastrais = soup.find(class_="txtCenter").find_all(class_="text")
                nome_mercado.append(soup.find("div", class_="txtTopo").text)
                cnpj_mercado.append(re.sub("CNPJ\:|\s*","",(dados_cadastrais[0].text)))
                endereco_mercado.append(re.sub("\n\t*","",(dados_cadastrais[1].text)))

                emissao = (re.sub("[A-Z]+|[a-z]+|\-|\n","",(soup.find("ul").find_all("strong"))[3].next_sibling)).split(" ")
                data.append(emissao[0])
                hora.append(emissao[1])

    nfce_file.close()

select_table_nfce_url()