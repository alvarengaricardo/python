from bs4 import BeautifulSoup
import requests

# no google pesquisar por "my browser agent"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}


def polipet():
    total = 0
    url = [
        'https://www.polipet.com.br/produto/racao-golden-formula-racas-pequenas-cachorros-adultos-frango-e-arroz-mini-bits-15-0kg-94862',
        'https://www.polipet.com.br/produto/racao-premier-ambientes-internos-senior-racas-pequenas-cachorros-7-frango-e-salmao-12-0kg-92057',
        'https://www.polipet.com.br/produto/racao-golden-formula-cachorros-filhotes-racas-pequenas-frango-e-arroz-mini-bits-10-1kg-94869'
    ]
    for URL in url:
        site = requests.get(URL, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        title = soup.find('h1', class_="fbits-produto-nome prodTitle title").get_text().strip()
        price = soup.find('div', class_="precoPor").get_text().strip()
        num_price = price[3:9]
        num_price = num_price.replace(',', '.')
        num_price = float(num_price)
        # print(soup.prettify())
        # print(type(title))
        print(title)
        print(price)
        # print(num_price)
        # print(type(num_price))
        total += num_price
    print(f'*****\nCompra total em Polipet: R$ {total:.2f}\n*****\n')


def cobasi():
    total = 0
    url = [
        'https://www.cobasi.com.br/racao-golden-formula-caes-adultos-racas-pequenas-frango-arroz-mini-bits-3626279/p?idsku=626279',
        'https://www.cobasi.com.br/racao-premier-ambientes-internos-racas-pequenas-senior-3663697/p?idsku=663700',
        'https://www.cobasi.com.br/racao-golden-filhotes-frango-mini-bits-3607967/p?idsku=324760'
    ]
    for URL in url:
        site = requests.get(URL, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        title = soup.find('h1', class_="styles__TitleProduct-sc-aqapmp-0 eubnFv").get_text().strip()
        price = soup.find('span', class_="card-price").get_text().strip()
        num_price = price[3:9]
        num_price = num_price.replace(',', '.')
        num_price = float(num_price)
        # print(soup.prettify())
        # print(type(title))
        print(title)
        print(price)
        # print(num_price)
        # print(type(num_price))
        total += num_price
    print(f'*****\nCompra total em Cobasi: R$ {total:.2f}\n*****\n')


def tudodebicho():
    total = 0
    url = [
        'https://www.tudodebicho.com.br/racao-premier-golden-formula-mini-bits-para-caes-adultos-frango-e-arroz/p?skuId=674',
     #   'https://www.tudodebicho.com.br/racao-premier-ambientes-internos-caes-adultos-senior--7-racas-pequenas-frango-e-salmao/p?skuId=81'
        'https://www.tudodebicho.com.br/racao-premier-golden-formula--mini-bits-caes-filhotes-frango-e-arroz/p?skuId=713'

    ]
    for URL in url:
        site = requests.get(URL, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        title = soup.find('h1', class_="vtex-store-components-3-x-productNameContainer mv0 t-heading-4").get_text().strip()
        price = soup.find('span', class_="vtex-product-price-1-x-sellingPrice").get_text().strip()
        num_price = price[3:9]
        #print(num_price)
        num_price = num_price.replace(',', '.')
        num_price = float(num_price)
        # print(soup.prettify())
        # print(type(title))
        print(title)
        print(price)
        # print(num_price)
        # print(type(num_price))
        total += num_price
    print(f'*****\nCompra total em Tudo de Bicho: R$ {total:.2f}\n*****\n')


def main():
    polipet()
    cobasi()
    tudodebicho()


if __name__ == '__main__':
    main()
