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
    'league': [], 'match_id': [],
    'team_id': [], 'type': [], 'player_id': [], 'player_name': [], 'related_player_id': [], 'related_player_name': [],
    'minute': [], 'extra_minute': [], 'injuried': [], 'own_goal': [], 
    'penalty': [], 'result': []
}

data_file = open(os.getcwd() + '\\csvData\\match\\matchEvents.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(data_file)


# file_paths = []
# for league, seasons in leaguesFileDic.items():
#     path = os.getcwd() + '\\data\\teams\\' + league 
#     for f in glob.glob(path + "**/*.json", recursive=True):
#         file_paths.append(f)

file_paths = []
for league, seasons in leaguesFileDic.items():
    for season in seasons:
        path = os.getcwd() + '\\data\\matchEvents\\' + league + '\\' + season
        for f in glob.glob(path + "**/*.json", recursive=True):
            file_paths.append(f)

# for f in file_paths:
#     print(f)

count = 0
for file_path in file_paths:
    custLeagueName = file_path.split('\\')[-1].split('_')[1]
    match_id = file_path.split('\\')[-1].split('_')[-1].split('.')[0]
    # print(custLeagueName, match_id)

    with open(file_path, encoding='utf-8') as json_file:
    	data = json.load(json_file)
    
    if 'data' in data:
        data = data['data']

        for event in data:
            rowData['league'].append(custLeagueName)
            rowData['match_id'].append(match_id)
            rowData['team_id'].append(event['team_id']) if event['team_id'] != None else rowData['team_id'].append('NaN')
            rowData['type'].append(event['type']) if event['type'] != None else rowData['type'].append('NaN')
            rowData['player_id'].append(event['player_id']) if event['player_id'] != None else rowData['player_id'].append('NaN')
            rowData['player_name'].append(event['player_name']) if event['player_name'] != None else rowData['player_name'].append('NaN')
            rowData['related_player_id'].append(event['related_player_id']) if event['related_player_id'] != None else rowData['related_player_id'].append('NaN')
            rowData['related_player_name'].append(event['related_player_name']) if event['related_player_name'] != None else rowData['related_player_name'].append('NaN')
            rowData['minute'].append(event['minute']) if event['minute'] != None else rowData['minute'].append('NaN')
            rowData['extra_minute'].append(event['extra_minute']) if event['extra_minute'] != None else rowData['extra_minute'].append('NaN')
            # rowData['reason'].append(event['reason']) if event['reason'] != None else rowData['reason'].append('NaN')
            rowData['injuried'].append(event['injuried']) if event['injuried'] != None else rowData['injuried'].append('NaN')
            rowData['own_goal'].append(event['own_goal']) if event['own_goal'] != None else rowData['own_goal'].append('NaN')
            rowData['penalty'].append(event['penalty']) if event['penalty'] != None else rowData['penalty'].append('NaN')
            rowData['result'].append(event['result']) if event['result'] != None else rowData['result'].append('NaN')

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


