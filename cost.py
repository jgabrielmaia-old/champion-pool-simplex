# Data Extraction packages
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

# Extracts the cost of buying for each champion
# Costs: Blue Essence, Riot Points

cost_url = 'https://leagueoflegends.fandom.com/wiki/List_of_champions'
cost_response = requests.get(cost_url)
cost_response_soup = BeautifulSoup(cost_response.text, 'html.parser')
cost_rows = cost_response_soup.find('table', {'class', 'sortable'}).find("tbody").find_all("tr")[1:]

print(f"{len(cost_rows[1:])} champions found.")

counterpick_champions = []
C = []
for cost_row in cost_rows:
  cost_champion = cost_row.find_all("td")
  cost_info = [cost_champion[attribute].text.strip() for attribute in [4,5]]
  C.append(float(cost_info[1]))
  cost_info.insert(0,cost_champion[0]["data-sort-value"])
  counterpick_champions.insert(0, cost_champion[0]["data-sort-value"])
  print(cost_info)
