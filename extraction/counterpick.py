# Data Extraction packages
import os
import requests
from bs4 import BeautifulSoup
import time

# Extracts the top 6 counterpicks for each champion
# Champion, Counters 1..6

def extract_counterpick(champion):
  formatted_champion = champion.lower().replace('\'','').replace(' ', '').replace('&willump', '').replace('.','')
  counterpick_url = f"https://www.championcounter.com.br/{formatted_champion}"
  counterpick_response = requests.get(counterpick_url)
  counterpick_response_soup = BeautifulSoup(counterpick_response.text, 'html.parser')
  
  counterpick_element = counterpick_response_soup.find('div', {'id': 'weakAgainst'})

  if counterpick_element is None:
    print(f"Didn't found counterpicks for {champion}")
    return []

  counterpicks = [counterpick.text for counterpick in counterpick_element.find_all('h4')]
  counterpicks.insert(0,champion)

  print(f"Found {champion} counterpicks.")

  time.sleep(10)

  return counterpicks

def counterpicks():
  filename = "data/counterpicks.txt"
  if os.path.isfile(filename):
    return

  with open("data/positions.txt") as f:
    champion_names = [line.split(',')[0] for line in f.readlines()]
    print(f"counterpicks: {len(champion_names)} champions found.")

    counterpicks = [extract_counterpick(name) for name in champion_names]
    counterpicks.sort()

    counterpicks_content = [','.join(counterpick) + '\n' for counterpick in counterpicks]
    counterpicks_file_content = ''.join(counterpicks_content)

    outfile = open(filename, "w")
    outfile.write(counterpicks_file_content)
    outfile.close()  