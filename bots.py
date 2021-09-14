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
  champion_games = s.find_all('td', {'class', 'Cell'})[4].text.replace(',','.').strip()
  champion_kda = s.find('td', {'class', 'KDARatio'}).text.split(":")[0].strip()
  champion_cs = s.find('span', {'class', 'Value Green'}).text.strip()
  champion_gold = s.find('span', {'class', 'Value Orange'}).text.replace(',','.').strip()

  print(f"{champion_name},{champion_victory_rate},{champion_games},{champion_kda},{champion_cs},{champion_gold}")

# draft positions
draft_position_url = 'https://leagueoflegends.fandom.com/wiki/List_of_champions_by_draft_position'
draft_position_response = requests.get(draft_position_url)
draft_position_response_soup = BeautifulSoup(draft_position_response.text, 'html.parser')
draft_position_rows = draft_position_response_soup.find('table', {'class', 'article-table'}).find_all('tr')

print(f"{len(draft_position_rows[1:])} champions found.")
positions = "Champion," + ",".join([d["data-tip"] for d in draft_position_rows[0].find_all("span")])

print(positions)

for row in draft_position_rows[1:]:
  champion_draft = row.find_all('td')
  champion_draft_name = champion_draft[0].text
  champion_positions = [position.has_attr('data-sort-value') for position in champion_draft[1:]]
  champion_positions.insert(0, champion_draft_name.strip())
  print(champion_positions)

# similarities
similarity_url = 'https://leagueoflegends.fandom.com/wiki/List_of_champions/Ratings'
similarity_response = requests.get(similarity_url)
similarity_response_soup = BeautifulSoup(similarity_response.text, 'html.parser')
similarity_rows = similarity_response_soup.find('table', {'class', 'sortable'}).find("tbody").find_all("tr")[1:][0].find_all("td")

for similarity_row in similarity_response_soup.find('table', {'class', 'sortable'}).find("tbody").find_all("tr")[1:]:
  similarity_champion = similarity_row.find_all("td")

  print([similarity_champion[attribute].text for attribute in range(11)])

# costs
cost_url = 'https://leagueoflegends.fandom.com/wiki/List_of_champions'
cost_response = requests.get(cost_url)
cost_response_soup = BeautifulSoup(cost_response.text, 'html.parser')
cost_rows = cost_response_soup.find('table', {'class', 'sortable'}).find("tbody").find_all("tr")[1:]

print(f"{len(cost_rows[1:])} champions found.")

counterpick_champions = []

for cost_row in cost_rows:
  cost_champion = cost_row.find_all("td")
  cost_info = [cost_champion[attribute].text.strip() for attribute in [4,5]]
  cost_info.insert(0,cost_champion[0]["data-sort-value"])
  counterpick_champions.insert(0, cost_champion[0]["data-sort-value"])
  print(cost_info)

# counters

import time

for champion in counterpick_champions:
  print(champion)
  counterpick_url = f"https://www.championcounter.com.br/{champion.lower()}"
  counterpick_response = requests.get(counterpick_url)
  counterpick_response_soup = BeautifulSoup(counterpick_response.text, 'html.parser')
  counterpick_rows = [counterpick.text for counterpick in counterpick_response_soup.find('div', {'id': 'weakAgainst'}).find_all('h4')]

  print(counterpick_rows)
  time.sleep(3)