from bs4 import BeautifulSoup
import requests

print('Escolhe o jogador')
homem = input('>')

html_text = requests.get('https://www.zerozero.pt/equipa.php?id=811&edicao_id=132894').text
soup = BeautifulSoup(html_text, 'lxml')
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

        print(f'''
        Nome: {player_name}
        Posição: {player_position}
        Idade: {player_age}
        Equipa: {player_team}
        ''')