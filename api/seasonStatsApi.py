import api.config as cf
import requests
import json
import os
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
		url = config.endpoint + 'stats/?' + 'user={}&token={}'.format(config.user, config.token)\
		      + '&t={}'.format('season')\
		      + '&id={}'.format(season_id)
		
		payload = {}
		headers = {}
		response = requests.request("GET", url, headers = headers, data = payload)
		print(url)
		print(response.text.encode('utf8'))
		
		check_path = path + '/data/seasonStats/' + league_name
		if not os.path.exists(check_path):
			os.mkdir(check_path)
		
		file_name = check_path + "/seasonStats_{}_{}.json".format(league_name, season_name)
		f = codecs.open(file_name, "w+", 'utf-8')
		f.write(response.text)
		# f.write('{}')
		f.close()


