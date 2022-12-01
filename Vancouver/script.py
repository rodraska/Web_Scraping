from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.zumper.com/apartment-buildings/p780822/burrard-place-rental-downtown-vancouver-vancouver-bc').text
soup = BeautifulSoup(html_text, 'lxml')

header_text = soup.find('h1', class_='Header_headerText__39zS4')
address = header_text.find('span', class_='Header_headerAddress__3cikR')
address.extract()
address_text = address.text
building_name = header_text.text
building_details = soup.find('section', id='building-details')
year_built = building_details.find('dd', class_='css-phcs22').text
description = soup.find('div', class_='css-voxcx').text
image_link = soup.find('img', class_='MediaItem_imageTag__3Bl2a undefined')['src']

print(image_link)