import api.config as cf
import requests
import json
import os
from datetime import datetime
import codecs
import time
import glob
import csv


def checkExistValInFile(file_path, value):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if value in row:
                file.close()
                return True
        file.close()
        return False


def appendValInFile(file_path, value):
    with open(file_path,'a+', newline='') as fd:
        csv_writer = csv.writer(fd)
        csv_writer.writerow([value])
	    
# f = open("C:/Users/kenpe/PycharmProjects/soccersApi/data/teams/primite_leayg/teams_primite_leayg_2013.json", "r")
# print(f.read())

config = cf.config()

seasons = config.seasons
leagues = config.leagues

path = '\\'.join(os.getcwd().split('\\')[:-1])

callPlayer_id = []
count = 0
for league_id, league_name in leagues.items():
	league_seasons = seasons[league_id]
	
	for season_id, season_name in league_seasons.items():
		

		# file_path = path.replace('\\', '/') + '/data/teamsSquad/' + league_name + '/' + season_name + '/teamsSquad_{}_{}.json'.format(
		# 	league_name, season_name)
		# json_file = open(file_path, 'r')
		# data = json.load(json_file)
		
		
		
		match_file_paths = [f for f in glob.glob(path + "\\data\\teamsSquad\\{}\\{}\\".format(league_name, season_name) + "**/*.json", recursive = True)]
		# print(match_file_paths)
		# print(path + "\\{}\\{}\\".format(league_name, season_name))
		# print(match_file_paths)
		
		for match_file_path in match_file_paths:
			json_file = open(match_file_path, 'r',  encoding = "utf-8")
			data = json.load(json_file)

			if 'data' in data:
				teamSquad = data['data']['squad']
			
				for player in teamSquad:
					player_id = player['player']['id']
					
					url = config.endpoint + 'players/?' + 'user={}&token={}'.format(config.user, config.token)\
							+ '&t={}'.format('info')\
							+ '&id={}'.format(player_id)
					
					check_path = path + '/data/player'
					
					
					# if not os.path.exists(check_path):
					# 	os.mkdir(check_path)
						
					# check_path = check_path + '/' + season_name
					# if not os.path.exists(check_path):
					# 	os.mkdir(check_path)
					
					checked_player = checkExistValInFile("C:\\Users\\kenpe\\PycharmProjects\\soccersApi\\data\\player\\checkedPlayerId.csv", str(player_id))
					
					if not checked_player:
						payload = {}
						headers = {}
						response = requests.request("GET", url, headers = headers, data = payload)
						appendValInFile("C:\\Users\\kenpe\\PycharmProjects\\soccersApi\\data\\player\\checkedPlayerId.csv", str(player_id))

						# callPlayer_id.append(player_id)
						
						count += 1
						print(str(count) + '  ' + url)
						print(league_name + '  ' + season_name)
						print(response.text.encode('utf8'))
						
						responseData = json.loads(response.text)
						if responseData['meta']['requests_left'] < 6:
							time.sleep(600)
						
						
						file_name = check_path + "/player_{}.json".format(player_id)
						f = codecs.open(file_name, "w+", 'utf-8')
						f.write(response.text)
						f.close()
