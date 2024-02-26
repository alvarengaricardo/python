from bs4 import BeautifulSoup
import requests

# no google pesquisar por "my browser agent"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}


def linkedin():
    URL = 'https://www.linkedin.com/analytics/profile-views/'
    # Criar um objeto BeautifulSoup
    site = requests.get(URL, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    div_tag = soup.find('div', class_='display-flex align-items-center')
    print(div_tag)
    if div_tag:
        numero = div_tag.get_text(strip=True)
        print(numero)
    else:
        print("Tag não encontrada.")

def main():
    linkedin()


if __name__ == '__main__':
    main()
