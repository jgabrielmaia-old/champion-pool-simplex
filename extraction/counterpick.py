# Data Extraction packages
import requests
from bs4 import BeautifulSoup
import time

# Extracts the top 6 counterpicks for each champion
# Champion, Counters 1..6

for champion in counterpick_champions:
  formatted_champion = champion.lower().replace('\'','').replace(' ', '').replace)('&willamp', '')
  print(formatted_champion)
  counterpick_url = f"https://www.championcounter.com.br/{formatted_champion}"
  counterpick_response = requests.get(counterpick_url)
  counterpick_response_soup = BeautifulSoup(counterpick_response.text, 'html.parser')
  counterpick_rows = [counterpick.text for counterpick in counterpick_response_soup.find('div', {'id': 'weakAgainst'}).find_all('h4')]
  counterpick_rows.insert(0,champion)
  print(counterpick_rows)
  time.sleep(3)
  