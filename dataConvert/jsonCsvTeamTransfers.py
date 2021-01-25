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
  'transfer_type': [], 'player_id': [], 'player_name': [], 'transfer_team': [], 
  'type': [], 'date': [], 'fee': []
}

data_file = open(os.getcwd() + '\\csvData\\teams\\teamsTransfers.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(data_file)


file_paths = []
for league, seasons in leaguesFileDic.items():
    for season in seasons:
        path = os.getcwd() + '\\data\\teamsTransfers\\' + league + '\\' + season
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
    with open(file_path, encoding='utf-8') as json_file:
    	data = json.load(json_file)
    
    if 'data' in data:
        data = data['data']

        if data['arrivals'] is not None:
            for index, player in enumerate(data['arrivals']):
                for key, value in player.items(): 
                    if key == 'player':
                        rowData['continent'].append(leagueIdContinentDic.get(leaguesNameToId[leagueName]))
                        rowData['country'].append(leagueIdCountryDic.get(leaguesNameToId[leagueName]))
                        rowData['league'].append(leagueName)
                        rowData['season'].append(season)
                        rowData['team_name'].append(team_name)
                        rowData['transfer_type'].append('arrivals')
                        
                        rowData['player_id'].append(value['id']) if value['id'] != None else rowData['player_id'].append('NaN')
                        rowData['player_name'].append(value['name']) if value['name'] != None else rowData['player_id'].append('NaN')
                    elif key == 'team_left':
                        rowData['transfer_team'].append(value['name']) if value != None else rowData['transfer_team'].append('NaN')
                    elif key == 'type':
                        rowData['type'].append(value) if value != None else rowData['type'].append('NaN')
                    elif key == 'date':
                        rowData['date'].append(value) if value != None else rowData['date'].append('NaN')
                    elif key == 'fee':
                        rowData['fee'].append(value) if value != None else rowData['fee'].append('NaN')

        if data['departures'] is not None:
            for index, player in enumerate(data['departures']):
                for key, value in player.items(): 
                    if key == 'player':
                        rowData['continent'].append(leagueIdContinentDic.get(leaguesNameToId[leagueName]))
                        rowData['country'].append(leagueIdCountryDic.get(leaguesNameToId[leagueName]))
                        rowData['league'].append(leagueName)
                        rowData['season'].append(season)
                        rowData['team_name'].append(team_name)
                        rowData['transfer_type'].append('departures')
                        
                        rowData['player_id'].append(value['id']) if value['id'] != None else rowData['player_id'].append('NaN')
                        rowData['player_name'].append(value['name']) if value['name'] != None else rowData['player_id'].append('NaN')
                    elif key == 'team_join':
                        rowData['transfer_team'].append(value['name']) if value != None else rowData['transfer_team'].append('NaN')
                    elif key == 'type':
                        rowData['type'].append(value) if value != None else rowData['type'].append('NaN')
                    elif key == 'date':
                        rowData['date'].append(value) if value != None else rowData['date'].append('NaN')
                    elif key == 'fee':
                        rowData['fee'].append(value) if value != None else rowData['fee'].append('NaN')




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


