from bs4 import BeautifulSoup
import requests

print('Escolhe a marca')
marca = input('>')

f = open("potatoes.txt", 'w')
html_text = requests.get('https://www.continente.pt/pesquisa/?q=batata&start=0&srule=Continente&pmin=0.01').text
soup = BeautifulSoup(html_text, 'lxml')
potatoes = soup.find_all('div', class_ = 'col-12 col-sm-3 col-lg-2 productTile')
for batata in potatoes:
    batata_marca = batata.find('p', class_ = 'ct-tile--brand').text
    if marca in batata_marca:
        batata_name = batata.find('a', class_ = 'ct-tile--description').text
        batata_price = batata.find('span', class_= 'ct-price-value').text.replace('\n','')
        f.write(f"Nome : {batata_name}\n")
        f.write(f"Preço: {batata_price}/Kg\n\n")
