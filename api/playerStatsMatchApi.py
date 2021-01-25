import api.config as cf
import requests
import json
import os
from datetime import datetime
import codecs
import time
import glob


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
		# print(path)
		#
		# file_path = path.replace('\\', '/') + '/data/matchLineups/' + league_name + '/matchLineups_{}_{}.json'.format(
		# 	league_name, season_name)
		# json_file = open(file_path, 'r')
		# data = json.load(json_file)
		
		match_file_paths = [f for f in glob.glob(path + "\\data\\matchLineups\\{}\\{}\\".format(league_name, season_name) + "**/*.json", recursive = True)]
		
		# print(path + "\\{}\\{}\\".format(league_name, season_name))
		# print(match_file_paths)
		
		for match_file_path in match_file_paths:
			# f = open(WAVE_FILE, "r", encoding = "utf-8")
			json_file = open(match_file_path, 'r',  encoding = "utf-8")
			data = json.load(json_file)
			
			if 'data' in data:
				
				# print(match_file_path)
				match_id = match_file_path.split('\\')[-1:][0].split('_')[-1:][0].replace('.json', '')
				
				home_squad = data['data']['home']['squad']
				away_squad = data['data']['away']['squad']
				
				# print(match_id)
				
				
				for player in home_squad:
					player_id = player['player']['id']
					
					url = config.endpoint + 'stats/?' + 'user={}&token={}'.format(config.user, config.token)\
					     + '&t={}'.format('player')\
					     + '&player_id={}'.format(player_id)\
					     + '&match_id={}'.format(match_id)
					
					print(url)
					
					check_path = path + '/data/playerStatsMatch/' + league_name
					if not os.path.exists(check_path):
						os.mkdir(check_path)
	
					check_path = check_path + '/' + season_name
					if not os.path.exists(check_path):
						os.mkdir(check_path)
					
					payload = {}
					headers = {}
					response = requests.request("GET", url, headers = headers, data = payload)
					
					count += 1
					print(str(count) + '  ' + url)
					print(response.text.encode('utf8'))

					responseData = json.loads(response.text)
					if responseData['meta']['requests_left'] < 6:
						time.sleep(600)
					
					file_name = check_path + "/playerStatsMatch_{}_{}_home_{}.json".format(league_name, match_id, player_id)
					f = codecs.open(file_name, "w+", 'utf-8')
					f.write(response.text)
					f.close()
				
				for player in away_squad:
					player_id = player['player']['id']
					
					url = config.endpoint + 'stats/?' + 'user={}&token={}'.format(config.user, config.token)\
					      + '&t={}'.format('player')\
					      + '&player_id={}'.format(player_id)\
					      + '&match_id={}'.format(match_id)
					
					print(url)
					
					check_path = path + '/data/playerStatsMatch/' + league_name
					if not os.path.exists(check_path):
						os.mkdir(check_path)
					
					check_path = check_path + '/' + season_name
					if not os.path.exists(check_path):
						os.mkdir(check_path)
					
					payload = {}
					headers = {}
					response = requests.request("GET", url, headers = headers, data = payload)
					
					count += 1
					print(str(count) + '  ' + url)
					print(response.text.encode('utf8'))
					
					responseData = json.loads(response.text)
					if responseData['meta']['requests_left'] < 6:
						time.sleep(600)
					
					file_name = check_path + "/playerStatsMatch_{}_{}_away_{}.json".format(league_name, match_id,
						player_id)
					f = codecs.open(file_name, "w+", 'utf-8')
					f.write(response.text)
					f.close()
		# url = config.endpoint + 'fixtures/?' + 'user={}&token={}'.format(config.user, config.token)\
		#       + '&t={}'.format('match_trends')\
		#       + '&id={}'.format(fixture_id)
		#
		# for fixture in data['data']:
		# 	fixture_id = fixture['id']
		# 	fixture_datatime = fixture['time']['date'][0:4] + fixture['time']['date'][5:7] + fixture['time'][
		# 		'date'][8:10]
		#
		# 	url = config.endpoint + 'fixtures/?' + 'user={}&token={}'.format(config.user, config.token)\
		# 	      + '&t={}'.format('match_trends')\
		# 	      + '&id={}'.format(fixture_id)
		#
		# 	payload = {}
		# 	headers = {}
		# 	response = requests.request("GET", url, headers = headers, data = payload)
		#
		# 	print(' 22235 / ' + str(count) + '  ' + url)
		# 	print(response.text.encode('utf8'))
		#
		# 	responseData = json.loads(response.text)
		# 	if responseData['meta']['requests_left'] < 6:
		# 		time.sleep(600)
		#
		# 	count += 1
		# 	print('3000 / ' + str(responseData['meta']['requests_left']))
		#
		# 	check_path = path + '/data/matchTrends/' + league_name
		# 	if not os.path.exists(check_path):
		# 		os.mkdir(check_path)
		#
		# 	check_path = check_path + '/' + season_name
		# 	if not os.path.exists(check_path):
		# 		os.mkdir(check_path)
		#
		# 	file_name = check_path + "/matchTrends_{}_{}_{}.json".format(league_name, fixture_datatime,
		# 		fixture_id)
		# 	f = codecs.open(file_name, "w+", 'utf-8')
		# 	f.write(response.text)
		# 	f.close()


