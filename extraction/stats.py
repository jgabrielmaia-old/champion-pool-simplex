# Data Extraction packages
import os
import requests
from bs4 import BeautifulSoup

# stats per champion
def stats():
  filename = "data/stats.txt"
  if os.path.isfile(filename):
    return
  
  stats_per_champion_url = 'https://www.op.gg/statistics/ajax2/champion/'
  stats_response = requests.post(stats_per_champion_url, data = {'type': 'win','league':'', 'period': 'month','mapId': 1, 'queue': 'ranked'})
  stats_per_champion_soup = BeautifulSoup(stats_response.text, 'html.parser')
  stats_rows = stats_per_champion_soup.find_all('tr', {'class':'Row'})

  print(f"stats: {len(stats_rows[1:])} champions found.")

  def extract_stats(row):
    name = row.find('td', {'class', 'ChampionName'}).text.strip()
    victory_rate = row.find('span', {'class', 'Value'}).text.strip()
    games = row.find_all('td', {'class', 'Cell'})[4].text.replace(',','').strip()
    kda = row.find('td', {'class', 'KDARatio'}).text.split(":")[0].strip()
    cs = row.find('span', {'class', 'Value Green'}).text.strip()
    gold = row.find('span', {'class', 'Value Orange'}).text.replace(',','.').strip()
    stats_attributes = [name,victory_rate,games,kda,cs,gold]
    return ','.join(stats_attributes) + "\n"

  champions_stats = [extract_stats(row) for row in stats_rows[1:]]
  champions_stats.sort()
  stats_file_content = ''.join(champions_stats)

  outfile = open(filename, "w")
  outfile.write(stats_file_content)
  outfile.close()

