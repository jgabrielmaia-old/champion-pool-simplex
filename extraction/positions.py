# Data Extraction packages
import requests
from bs4 import BeautifulSoup
import os

# Extracts the positions available for each champion
# Positions: Top, Jungle, Middle, Bottom, Support, Unplayed

def extract_positions():
  filename = "data/positions.txt"
  if os.path.isfile(filename):
    return

  draft_position_url = 'https://leagueoflegends.fandom.com/wiki/List_of_champions_by_draft_position'
  draft_position_response = requests.get(draft_position_url)
  draft_position_response_soup = BeautifulSoup(draft_position_response.text, 'html.parser')
  draft_position_rows = draft_position_response_soup.find('table', {'class', 'article-table'}).find_all('tr')

  print(f"positions: {len(draft_position_rows[1:])} champions found.")
  champion_positions = ''
  
  def is_position(pos):
    if pos == "True":
      return "1"
    return "0"

  def extract_position(row):
    champion_draft = row.find_all('td')
    champion_draft_name = champion_draft[0].text.replace('\'','')
    champion_row = [position.has_attr('data-sort-value') for position in champion_draft[1:]]
    champion_attributes = ','.join(is_position(str(c)) for c in champion_row)
    return f"{champion_draft_name.strip()},{champion_attributes}\n"

  champion_positions = [extract_position(row) for row in draft_position_rows[1:]]
  champion_positions.sort()
  positions_file_content = ''.join(champion_positions)

  outfile = open(filename, "w")
  outfile.write(positions_file_content)
  outfile.close()