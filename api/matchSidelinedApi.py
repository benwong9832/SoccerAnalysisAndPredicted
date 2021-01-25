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
		file_path = path.replace('\\', '/') + '/data/fixtures/' + league_name + '/fixtures_{}_{}.json'.format(league_name, season_name)
		json_file = open(file_path, 'r')
		data = json.load(json_file)
		
		for fixture in data['data']:
			fixture_id = fixture['id']
			fixture_datatime = fixture['time']['date'][0:4] + fixture['time']['date'][5:7] + fixture['time']['date'][8:10]
			
			url = config.endpoint + 'fixtures/?' + 'user={}&token={}'.format(config.user, config.token)\
			      + '&t={}'.format('match_sidelined')\
			      + '&id={}'.format(fixture_id)

			payload = {}
			headers = {}
			response = requests.request("GET", url, headers = headers, data = payload)
			
			print(' 22235 / ' + str(count) + '  ' + url)
			print(response.text.encode('utf8'))
			
			responseData = json.loads(response.text)
			if responseData['meta']['requests_left'] < 6:
				time.sleep(600)
			
			count += 1
			print('3000 / ' + str(responseData['meta']['requests_left']))

			check_path = path + '/data/matchSidelined/' + league_name
			if not os.path.exists(check_path):
				os.mkdir(check_path)
			
			check_path = check_path + '/' + season_name
			if not os.path.exists(check_path):
				os.mkdir(check_path)
			
			file_name = check_path + "/matchSidelined_{}_{}_{}.json".format(league_name, fixture_datatime, fixture_id)
			f = codecs.open(file_name, "w+", 'utf-8')
			f.write(response.text)
			f.close()

