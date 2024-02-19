from gettext import gettext

from bs4 import BeautifulSoup
import requests
from wheel.metadata import _

URL = 'https://www.polipet.com.br/produto/racao-golden-formula-racas-pequenas-cachorros-adultos-frango-e-arroz-mini-bits-15-0kg-94862'

# no google pesquisar por "my browser agent"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}

site = requests.get(URL, headers = headers)

soup = BeautifulSoup(site.content, 'html.parser')
title = soup.find('h1', class_ = "fbits-produto-nome prodTitle title").get_text()
price = soup.find('div', class_ = "precoPor").get_text().strip()
num_price = price[3:9]
num_price = num_price.replace(',', '.')
num_price = float(num_price)
#print(soup.prettify())
print(type(title))
print(title)
print(price)
print(num_price)
print(type(num_price))

