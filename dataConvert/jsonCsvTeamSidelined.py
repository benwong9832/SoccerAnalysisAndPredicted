import json
import csv
import os
import glob
import requests
from urllib import request, parse
import dataDictionary
import sys
import common

# define 
leaguesFileDic = dataDictionary.leaguesFileDic
leaguesDic = dataDictionary.leaguesDic
seasonsDic = dataDictionary.seasonsDic
leagueIdContinentDic = dataDictionary.leagueIdContinentDic
leagueIdCountryDic = dataDictionary.leagueIdCountryDic
leaguesNameDic = dataDictionary.leaguesNameDic
leaguesNameToId = dataDictionary.leaguesNameToId


rowData = {
  'continent': [], 'country': [], 'league': [], 'season': [], 'team_name': [],
  'type': [], 'player_id': [], 'name': [],
  'reason': [], 'since': [], 'expected_return': [], 
}

data_file = open(os.getcwd() + '\\csvData\\teams\\teamsSidelined.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(data_file)


# file_paths = []
# for league, seasons in leaguesFileDic.items():
#     path = os.getcwd() + '\\data\\teams\\' + league 
#     for f in glob.glob(path + "**/*.json", recursive=True):
#         file_paths.append(f)

file_paths = []
for league, seasons in leaguesFileDic.items():
    for season in seasons:
        path = os.getcwd() + '\\data\\teamsSidelined\\' + league + '\\' + season
        for f in glob.glob(path + "**/*.json", recursive=True):
            file_paths.append(f)

# for f in file_paths:
#     print(f)


count = 0
for file_path in file_paths:
    custLeagueName = file_path.split('\\')[-1].split('_')[1]
    season = file_path.split('\\')[-1].split('_')[-2].split('.')[0]
    team_name = file_path.split('\\')[-1].split('_')[-1].split('.')[0]
    leagueName = leaguesNameDic[custLeagueName]
    # print(custLeagueName, season, team_name, leagueName)

    with open(file_path, encoding='utf-8') as json_file:
    	data = json.load(json_file)
    
    if 'data' in data:
        data = data['data']

        types = data['types'].keys()
        for stype in types:
            for player in data['types'][stype]:
                rowData['continent'].append(leagueIdContinentDic.get(leaguesNameToId[leagueName]))
                rowData['country'].append(leagueIdCountryDic.get(leaguesNameToId[leagueName]))
                rowData['league'].append(leagueName)
                rowData['season'].append(season)
                rowData['team_name'].append(team_name)

                rowData['type'].append(stype)
                rowData['player_id'].append(player['player']['id']) if player['player']['id'] != None else rowData['player_id'].append('NaN')
                rowData['name'].append(player['player']['name']) if player['player']['name'] != None else rowData['name'].append('NaN')
                rowData['reason'].append(player['reason']) if player['reason'] != None else rowData['name'].append('NaN')
                rowData['since'].append(player['since']) if player['since'] != None else rowData['name'].append('NaN')
                rowData['expected_return'].append(player['expected_return']) if player['expected_return'] != None else rowData['name'].append('NaN')

                # print(types)


# insert header
row = []
for header, data in rowData.items():
    row.append(header)
csv_writer.writerow(row)

# insert data
for i in range(len(rowData['league'])):
      row = []
      for header, data in rowData.items():
            row.append(rowData[header][i])
      csv_writer.writerow(row)
      
print('done')


