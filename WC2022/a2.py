from bs4 import BeautifulSoup
import requests
import pandas as pd

html_text = requests.get('https://www.playmakerstats.com/equipa.php?id=830&edicao_id=132894').text
soup = BeautifulSoup(html_text, 'lxml')
header = soup.find('h1')
pais = header.find('span', class_='name').text
squad = soup.find('div', id = 'team_squad')
body = squad.find('tbody')
players = body.find_all('tr')
names_list = []
positions_list = []
ages_list = []
teams_list = []
leagues_list = []

for jogador in players:
    player_td = jogador.find_all('td')
    player_list = player_td[1]
    player_name = player_list.find('div', class_ = 'text').text
    player_position = jogador.find('td', style = 'text-align:left;').text
    player_age = player_td[3].text
    player_sheet = player_td[4]
    player_team = player_sheet.find('div', class_ = 'text').text
    player_teamimage = player_sheet.find('div', class_='micrologo_and_text')
    player_league = player_teamimage.find('div', class_='image').img['title']
    names_list.append(player_name)
    positions_list.append(player_position)
    ages_list.append(player_age)
    teams_list.append(player_team)
    leagues_list.append(player_league)

data = {
    'Name': names_list,
    'Position': positions_list,
    'Age': ages_list,
    'Team': teams_list,
    'League': leagues_list
}

df = pd.DataFrame(data)

df.to_csv('Morocco.csv', index=False)

print(df)
