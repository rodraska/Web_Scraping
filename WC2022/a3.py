from bs4 import BeautifulSoup
import requests
import pandas as pd

links_list=[
    'https://www.playmakerstats.com/equipa.php?id=825&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=938&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=979&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=881&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=826&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=874&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=934&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=833&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=835&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=814&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=876&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=831&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=824&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=889&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=819&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=988&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=822&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=875&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=906&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=812&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=818&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=830&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=815&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=904&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=816&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=1018&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=947&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=1016&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=811&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=961&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=861&edicao_id=132894',
    'https://www.playmakerstats.com/equipa.php?id=940&edicao_id=132894',
]

countries_list=[]
names_list = []
positions_list = []
ages_list = []
teams_list = []
leagues_list =[]

i=0
while (i < 32):

    html_text = requests.get(links_list[i]).text
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
        player_position = jogador.find('td', style = 'text-align:left;').text
        player_age = player_td[3].text
        player_sheet = player_td[4]
        player_team = player_sheet.find('div', class_ = 'text').text
        player_teamimage = player_sheet.find('div', class_='micrologo_and_text')
        player_league = player_teamimage.find('div', class_='image').img['title']
        countries_list.append(pais)
        names_list.append(player_name)
        positions_list.append(player_position)
        ages_list.append(player_age)
        teams_list.append(player_team)
        leagues_list.append(player_league)
    i += 1

data = {
    'Country': countries_list,
    'Name': names_list,
    'Position': positions_list,
    'Age': ages_list,
    'Team': teams_list,
    'League': leagues_list
}

df = pd.DataFrame(data)

df.to_csv('All.csv', index=False)

print(df)