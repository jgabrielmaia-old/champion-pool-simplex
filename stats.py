# Data Extraction packages
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

# stats per champion
stats_per_champion_url = 'https://www.op.gg/statistics/ajax2/champion/'
stats_response = requests.post(stats_per_champion_url, data = {'type': 'win','league':'', 'period': 'month','mapId': 1, 'queue': 'ranked'})
stats_per_champion_soup = BeautifulSoup(stats_response.text, 'html.parser')
stats_rows = stats_per_champion_soup.find_all('tr', {'class':'Row'})

print("champion_name,champion_victory_rate,champion_games,champion_kda,champion_cs,champion_gold")
for s in stats_rows[1:]:
  champion_name = s.find('td', {'class', 'ChampionName'}).text.strip()
  champion_victory_rate = s.find('span', {'class', 'Value'}).text.strip()
  champion_games = s.find_all('td', {'class', 'Cell'})[4].text.replace(',','').strip()
  champion_kda = s.find('td', {'class', 'KDARatio'}).text.split(":")[0].strip()
  champion_cs = s.find('span', {'class', 'Value Green'}).text.strip()
  champion_gold = s.find('span', {'class', 'Value Orange'}).text.replace(',','.').strip()

  print([champion_name,champion_victory_rate,champion_games,champion_kda,champion_cs,champion_gold])

