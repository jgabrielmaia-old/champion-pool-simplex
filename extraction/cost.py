# Data Extraction packages
import requests
from bs4 import BeautifulSoup
import os.path

# Extracts the cost of buying for each champion
# Costs: Blue Essence, Riot Points

def extract_costs():
  filename = "data/costs.txt"
  if os.path.isfile(filename):
    return

  cost_url = 'https://leagueoflegends.fandom.com/wiki/List_of_champions'
  cost_response = requests.get(cost_url)
  cost_response_soup = BeautifulSoup(cost_response.text, 'html.parser')
  cost_rows = cost_response_soup.find('table', {'class', 'sortable'}).find("tbody").find_all("tr")[1:]

  print(f"costs: {len(cost_rows)} champions found.")

  def extract_cost(cost_row):
    cost_champion = cost_row.find_all("td")
    cost_info = [cost_champion[attribute].replace('\'','').text.strip() for attribute in [4,5]]
    cost_info.insert(0,cost_champion[0]["data-sort-value"])
    return ','.join(cost_info) + "\n"

  costs = [extract_cost(cost_row) for cost_row in cost_rows]
  costs.sort()
  costs_file_content = ''.join(costs)

  outfile = open(filename, "w")
  outfile.write(costs_file_content)
  outfile.close()