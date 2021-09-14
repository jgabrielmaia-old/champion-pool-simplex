# Data Extraction packages
import requests
from bs4 import BeautifulSoup

# Extracts the cost of buying for each champion
# Costs: Blue Essence, Riot Points

def costs():
  cost_url = 'https://leagueoflegends.fandom.com/wiki/List_of_champions'
  cost_response = requests.get(cost_url)
  cost_response_soup = BeautifulSoup(cost_response.text, 'html.parser')
  cost_rows = cost_response_soup.find('table', {'class', 'sortable'}).find("tbody").find_all("tr")[1:]

  print(f"costs: {len(cost_rows[1:])} champions found.")

  def extract_cost(cost_row):
    cost_champion = cost_row.find_all("td")
    cost_info = [cost_champion[attribute].text.strip() for attribute in [4,5]]
    cost_info.insert(0,cost_champion[0]["data-sort-value"])
    return ','.join(cost_info) + "\n"

  costs = [extract_cost(cost_row) for cost_row in cost_rows]

  costs = ''.join(costs)

  outfile =  open("data/costs.txt", "w")
  outfile.write(costs)
  outfile.close()