import requests
from bs4 import BeautifulSoup

# URL do seu perfil do LinkedIn
linkedin_url = "https://www.linkedin.com/in/alvarengaricardo/"

# Fazendo uma solicitação HTTP para a página do LinkedIn
response = requests.get(linkedin_url)

# Analisando o HTML da página
soup = BeautifulSoup(response.content, "html.parser")

# Encontrando o elemento que contém a quantidade de visitas
visit_element = soup.find("span", class_="num-views")

# Extraindo o número de visitas
num_visits = visit_element.text.strip()

# Exibindo a quantidade de visitas
print("Quantidade de visitas ao perfil do LinkedIn:", num_visits)
