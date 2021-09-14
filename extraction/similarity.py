# Data Extraction packages
import requests
from bs4 import BeautifulSoup

# Extracts the similar attributes for each champion
# Attributes: Primary role, Secondary role, Damage, Toughness, Control, Mobility, Utility, Style (NULL), Damage Type, Difficulty 

similarity_url = 'https://leagueoflegends.fandom.com/wiki/List_of_champions/Ratings'
similarity_response = requests.get(similarity_url)
similarity_response_soup = BeautifulSoup(similarity_response.text, 'html.parser')
similarity_rows = similarity_response_soup.find('table', {'class', 'sortable'}).find("tbody").find_all("tr")[1:]

print(f"{len(similarity_rows[1:])} champions found.")
D = []
for similarity_row in similarity_rows:
  similarity_champion = similarity_row.find_all("td")
  D.append(float(similarity_champion[10].text.strip()))
  print([similarity_champion[attribute].text.strip() for attribute in range(11)])
