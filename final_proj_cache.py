import json
import requests
import os
import json
import statsapi

open('cache.json', 'w').close()
people_2022 = statsapi.get('sports_players',{'season':2022})['people']

roster_2022 = []

for x in people_2022:
    roster_2022.append((x.get('nameFirstLast'),'2022 ' + statsapi.lookup_team(x.get('currentTeam')['id'])[0].get('name')))

with open('cache.json', 'w') as json_file:
    json.dump(roster_2022, json_file)

