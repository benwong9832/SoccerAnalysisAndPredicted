import api.config as cf
import requests
import json
import os
import codecs

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
		file_path = path.replace('\\', '/') + '/data/teams/' + league_name + '/teams_{}_{}.json'.format(league_name, season_name)
		json_file = open(file_path, 'r')
		# print(json_file.read())
		data = json.load(json_file)

		for team in data['data']:
			team_id = team['id']
			team_name = team['name']
			
			url = config.endpoint + 'teams/?' + 'user={}&token={}'.format(config.user, config.token)\
			      + '&t={}'.format('transfers')\
			      + '&id={}'.format(team_id)\
			      + '&season_id={}'.format(season_id)

			payload = {}
			headers = {}
			response = requests.request("GET", url, headers = headers, data = payload)
			
			count += 1
			print(count)
			print(url)
			print(response.text.encode('utf8'))

			check_path = path + '/data/teamsTransfers/' + league_name
			if not os.path.exists(check_path):
				os.mkdir(check_path)
			
			check_path = check_path + '/' + season_name
			if not os.path.exists(check_path):
				os.mkdir(check_path)
			
			file_name = check_path + "/teamsTransfers_{}_{}_{}.json".format(league_name, season_name, team_name)
			# f = open(file_name, "w+")
			f = codecs.open(file_name, "w+", 'utf-8')
			f.write(response.text)
			# f.write('{}')
			f.close()


