import api.config as cf
import requests
import json
import os
from datetime import datetime
import codecs
import time

# f = open("C:/Users/kenpe/PycharmProjects/soccersApi/data/teams/primite_leayg/teams_primite_leayg_2013.json", "r")
# print(f.read())

config = cf.config()

seasons = config.seasons
leagues = config.leagues

path = '\\'.join(os.getcwd().split('\\')[:-1])

count = 0
for league_id, league_name in leagues.items():
	league_seasons = seasons[league_id]

	for season_id, season_name in league_seasons.items():
		
		url = config.endpoint + 'leaders/?' + 'user={}&token={}'.format(config.user, config.token)\
		      + '&t={}'.format('topassists')\
		      + '&season_id={}'.format(season_id)
		
		payload = {}
		headers = {}
		response = requests.request("GET", url, headers = headers, data = payload)
		
		check_path = path + '/data/topAssists/' + league_name
		if not os.path.exists(check_path):
			os.mkdir(check_path)
			
		responseData = json.loads(response.text)
		print(url)
		print(responseData)
		if responseData['meta']['requests_left'] < 6:
			time.sleep(600)
		
		count += 1
		print('3000 / ' + str(responseData['meta']['requests_left']))
		
		
		file_name = check_path + "/topAssists_{}_{}.json".format(league_name, season_name)
		f = codecs.open(file_name, "w+", 'utf-8')
		f.write(response.text)
		f.close()
		


