# Data Extraction packages
import os
import requests
from bs4 import BeautifulSoup

# Extracts the similar attributes for each champion
# Attributes: Primary role, Secondary role, Damage, Toughness, Control, Mobility, Utility, Style (NULL), Damage Type, Difficulty 

def extract_similarity():
  filename = "data/similarity.txt"
  if os.path.isfile(filename):
    return

  similarity_url = 'https://leagueoflegends.fandom.com/wiki/List_of_champions/Ratings'
  similarity_response = requests.get(similarity_url)
  similarity_response_soup = BeautifulSoup(similarity_response.text, 'html.parser')
  similarity_rows = similarity_response_soup.find('table', {'class', 'sortable'}).find("tbody").find_all("tr")[1:]

  print(f"similarity: {len(similarity_rows)} champions found.")
  
  def extract_similarity(row):
    similarity_champion = row.find_all("td")
    similarity_attributes = [similarity_champion[attribute].text.replace('\'','') for attribute in (0,3,4,5,6,7,10)]
    return ','.join(similarity_attributes).strip() + '\n'
    
  similarity_champions = [extract_similarity(row) for row in similarity_rows]
  similarity_champions.sort()
  similarity_file_content = ''.join(similarity_champions)

  outfile = open(filename, "w")
  outfile.write(similarity_file_content)
  outfile.close()