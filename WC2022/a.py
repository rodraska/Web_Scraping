from bs4 import BeautifulSoup
import requests
import pandas as pd

print('Pick a Player')
homem = input('>')

html_text = requests.get('https://www.playmakerstats.com/equipa.php?id=811&edicao_id=132894').text
soup = BeautifulSoup(html_text, 'lxml')
header = soup.find('h1')
pais = header.find('span', class_='name').text
squad = soup.find('div', id = 'team_squad')
body = squad.find('tbody')
players = body.find_all('tr')

for jogador in players:
    player_td = jogador.find_all('td')
    player_list = player_td[1]
    player_name = player_list.find('div', class_ = 'text').text
    if homem in player_name:
        player_position = jogador.find('td', style = 'text-align:left;').text
        player_age = player_td[3].text
        player_sheet = player_td[4]
        player_team = player_sheet.find('div', class_ = 'text').text
        player_teamimage = player_sheet.find('div', class_='micrologo_and_text')
        player_league = player_teamimage.find('div', class_='image').img['title']

        print(f'''
        Name: {player_name}
        Position: {player_position}
        Age: {player_age}
        Country: {pais}
        Club: {player_team}
        League: {player_league}
        ''')