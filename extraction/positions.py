# Data Extraction packages
import requests
from bs4 import BeautifulSoup

# Extracts the positions available for each champion
# Positions: Top, Jungle, Middle, Bottom, Support, Unplayed

draft_position_url = 'https://leagueoflegends.fandom.com/wiki/List_of_champions_by_draft_position'
draft_position_response = requests.get(draft_position_url)
draft_position_response_soup = BeautifulSoup(draft_position_response.text, 'html.parser')
draft_position_rows = draft_position_response_soup.find('table', {'class', 'article-table'}).find_all('tr')

print(f"{len(draft_position_rows[1:])} champions found.")
positions = "Champion," + ",".join([d["data-tip"] for d in draft_position_rows[0].find_all("span")])

print(positions)
P = [[0]*5 for i in range(156)]
r = 0
for row in draft_position_rows[1:]:
  champion_draft = row.find_all('td')
  champion_draft_name = champion_draft[0].text
  champion_positions = [position.has_attr('data-sort-value') for position in champion_draft[1:]]
  P[r][0] = int(champion_positions[0] == True)
  P[r][1] = int(champion_positions[1] == True)
  P[r][2] = int(champion_positions[2] == True)
  P[r][3] = int(champion_positions[3] == True)
  P[r][4] = int(champion_positions[4] == True)
  r+=1
  champion_positions.insert(0, champion_draft_name.strip())
  print(champion_positions)