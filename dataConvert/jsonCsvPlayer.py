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
  'player_id': [], 'position': [], 'birthday': [], 'country': [], 'weight': [], 
  'height': [], 'foot': [], 'sta_Num_leagues': [], 'sta_Num_team': []
}

data_file = open(os.getcwd() + '\\csvData\\player\\player.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(data_file)


file_paths = []
file_paths = glob.glob(os.getcwd() + '\\data\\player\\' + "**/*.json", recursive=True)

# for f in file_paths:
#     print(f)

count = 0
for file_path in file_paths:
    player_id = file_path.split('\\')[-1].split('_')[1].split('.')[0]
    # player_id = file_path.split('\\')[-1].split('_')[-2].split('.')[0]
    # print(player_id)

    # team_name = file_path.split('\\')[-1].split('_')[-1].split('.')[0]
    # leagueName = leaguesNameDic[custLeagueName]
    with open(file_path, encoding='utf-8') as json_file:
    	data = json.load(json_file)
    
    if 'data' in data:
          
          player = data['data']
          # print(file_path)

          rowData['player_id'].append(player_id)
          rowData['position'].append(player['position']) if player['position'] != None else rowData['position'].append('NaN')
          rowData['birthday'].append(player['birthday']) if player['birthday'] != None else rowData['birthday'].append('NaN')
          rowData['country'].append(player['country']['name']) if player['country']['name'] != None else rowData['country'].append('NaN')
          rowData['weight'].append(player['weight']) if player['weight'] != None else rowData['weight'].append('NaN')
          rowData['height'].append(player['height']) if player['height'] != None else rowData['height'].append('NaN')
          rowData['foot'].append(player['foot']) if player['foot'] != None else rowData['foot'].append('NaN')

          if 'leagues' in player:
            rowData['sta_Num_leagues'].append(len(player['leagues'])) if player['leagues'] != None else rowData['sta_Num_leagues'].append('NaN')
          else:
            rowData['sta_Num_leagues'].append('NaN')

          if 'roles' in player:
            rowData['sta_Num_team'].append(len(player['roles'])) if player['roles'] != None else rowData['sta_Num_team'].append('NaN')
          else:
            rowData['sta_Num_team'].append('NaN')

# insert header
row = []   
for header, data in rowData.items():
    row.append(header)
csv_writer.writerow(row)

# insert data
for i in range(len(rowData['player_id'])):
      row = []
      for header, data in rowData.items():
            row.append(rowData[header][i])
      csv_writer.writerow(row)

print('done')


