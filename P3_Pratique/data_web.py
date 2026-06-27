import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
with open("/workspaces/7168871-apprenez-les-bases-du-langage-python/P3/P3C2/énoncé/index.html", "r") as file:
   soup = BeautifulSoup(file.read(), 'html.parser')

print(soup)

print(soup.title)
titre = soup.title.string

h1 = soup.find_all('h1') and soup.find(id = 'titre')
print(h1)

produits = soup.select("li.product")
print(produits)