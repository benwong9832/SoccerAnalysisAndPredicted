import api.config as cf
import requests
import json
import os

# f = open("C:/Users/kenpe/PycharmProjects/soccersApi/data/teams/primite_leayg/teams_primite_leayg_2013.json", "r")
# print(f.read())

config = cf.config()

seasons = config.seasons
leagues = config.leagues

path = '\\'.join(os.getcwd().split('\\')[:-1])

for league_id, league_name in leagues.items():
	url = config.endpoint + 'leagues/?' + 'user={}&token={}'.format(config.user, config.token)\
	      + '&t={}'.format('info')\
	      + '&id={}'.format(league_id)
	
	payload = {}
	headers = {}
	response = requests.request("GET", url, headers = headers, data = payload)
	# print(url)
	# print(response.text.encode('utf8'))
	check_path = path + '/data/leagues/'
	# if not os.path.exists(check_path):
	# 	os.mkdir(check_path)
	
	file_name = check_path + "{}.json".format(league_name)
	f = open(file_name, "w+")
	f.write(response.text)
	# f.write('{}')
	f.close()


