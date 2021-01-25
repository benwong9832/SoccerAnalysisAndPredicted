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
  'match_id': [], 'season': [], 'team': [], 'formation': [], 
  'player_id': [], 'common_name': [], 'weight': [], 'height': [], 
  'country': [], 
  'number': [], 'position': [], 'order': []
}

data_file = open(os.getcwd() + '\\csvData\\match\\matchLineups.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(data_file)


# file_paths = []
# for league, seasons in leaguesFileDic.items():
#     path = os.getcwd() + '\\data\\teams\\' + league 
#     for f in glob.glob(path + "**/*.json", recursive=True):
#         file_paths.append(f)

file_paths = []
for league, seasons in leaguesFileDic.items():
    for season in seasons:
        path = os.getcwd() + '\\data\\matchLineups\\' + league + '\\' + season
        for f in glob.glob(path + "**/*.json", recursive=True):
            file_paths.append(f)

# for f in file_paths:
#     print(f)


count = 0
for file_path in file_paths:
    custLeagueName = file_path.split('\\')[-1].split('_')[1]
    season = file_path.split('\\')[-1].split('_')[-2].split('.')[0]
    match_id = file_path.split('\\')[-1].split('_')[-1].split('.')[0]
    # leagueName = leaguesNameDic[custLeagueName]
    # print(custLeagueName, season, match_id)

    with open(file_path, encoding='utf-8') as json_file:
    	data = json.load(json_file)
    
    if 'data' in data:
        data = data['data']

        for player in data['home']['squad']:
            rowData['match_id'].append(match_id)
            rowData['season'].append(season)
            rowData['team'].append('home')
            rowData['formation'].append(data['home']['formation']) if data['home']['formation'] != None else rowData['formation'].append('NaN')

            rowData['player_id'].append(player['player']['id']) if player['player']['id'] != None else rowData['player_id'].append('NaN')
            rowData['common_name'].append(player['player']['common_name']) if player['player']['common_name'] != None else rowData['common_name'].append('NaN')
            
            if player['player']['weight'] != None and player['player']['weight'] != 0 and player['player']['weight'] != '0':
                rowData['weight'].append(player['player']['weight'])
            else:
                rowData['weight'].append('NaN')
            # rowData['weight'].append(player['player']['weight']) if player['player']['weight'] != None else rowData['weight'].append('NaN')
            
            # if player['player']['height'] != None or player['player']['height'] != 0:
            #     rowData['height'].append(player['player']['height'])
            # else:
            #     rowData['height'].append('NaN')
            rowData['height'].append(player['player']['height']) if player['player']['height'] != None else rowData['height'].append('NaN')
            rowData['country'].append(player['player']['country']['name']) if player['player']['country']['name'] != None else rowData['country'].append('NaN')
            
            rowData['number'].append(player['number']) if player['number'] != None else rowData['number'].append('NaN')
            rowData['position'].append(player['position']) if player['position'] != None else rowData['position'].append('NaN')
            rowData['order'].append(player['order']) if player['order'] != None else rowData['order'].append('NaN')
        
        for player in data['away']['squad']:
            rowData['match_id'].append(match_id)
            rowData['season'].append(season)
            rowData['team'].append('away')
            rowData['formation'].append(data['home']['formation']) if data['home']['formation'] != None else rowData['formation'].append('NaN')

            rowData['player_id'].append(player['player']['id']) if player['player']['id'] != None else rowData['player_id'].append('NaN')
            rowData['common_name'].append(player['player']['common_name']) if player['player']['common_name'] != None else rowData['common_name'].append('NaN')
            if player['player']['weight'] != None and player['player']['weight'] != 0 and player['player']['weight'] != '0':
                rowData['weight'].append(player['player']['weight'])
            else:
                rowData['weight'].append('NaN')
            # rowData['weight'].append(player['player']['weight']) if player['player']['weight'] != None else rowData['weight'].append('NaN')
            
            # if player['player']['height'] != None or player['player']['height'] != 0:
            #     rowData['height'].append(player['player']['height'])
            # else:
            #     rowData['height'].append('NaN')
            rowData['height'].append(player['player']['height']) if player['player']['height'] != None else rowData['height'].append('NaN')
            rowData['country'].append(player['player']['country']['name']) if player['player']['country']['name'] != None else rowData['country'].append('NaN')
            
            rowData['number'].append(player['number']) if player['number'] != None else rowData['number'].append('NaN')
            rowData['position'].append(player['position']) if player['position'] != None else rowData['position'].append('NaN')
            rowData['order'].append(player['order']) if player['order'] != None else rowData['order'].append('NaN')

# insert header
row = []
for header, data in rowData.items():
    row.append(header)
csv_writer.writerow(row)

# insert data
for i in range(len(rowData['match_id'])):
      row = []
      for header, data in rowData.items():
            row.append(rowData[header][i])
      csv_writer.writerow(row)
      
print('done')


