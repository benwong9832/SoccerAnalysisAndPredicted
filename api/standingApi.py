import api.config as cf
import requests
import os

config = cf.config()

seasons = config.seasons
leagues = config.leagues

path = '\\'.join(os.getcwd().split('\\')[:-1])

for league_id, league_name in leagues.items():
	league_seasons = seasons[league_id]

	for season_id, season_name in league_seasons.items():
		url = config.endpoint + 'leagues/?' + 'user={}&token={}'.format(config.user, config.token)\
		      + '&t={}'.format('standings')\
		      + '&season_id={}'.format(season_id)

		payload = {}
		headers = {}
		response = requests.request("GET", url, headers = headers, data = payload)

		print(url)
		print(response.text.encode('utf8'))
		
		check_path = path + '/data/standings/' + league_name
		if not os.path.exists(check_path):
			os.mkdir(check_path)
		
		file_name = check_path + "/standing_{}_{}.json".format(league_name, season_name)
		f = open(file_name, "w+")
		f.write(response.text)
		f.close()

