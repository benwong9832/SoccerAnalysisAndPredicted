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
    'match_id': [], 'season': [],

    'HTF': [],
    'HP1N': [], 'HP1P': [], 'HP2N': [], 'HP2P': [], 'HP3N': [], 'HP3P': [], 'HP4N': [], 'HP4P': [], 'HP5N': [], 'HP5P': [], 'HP6N': [], 'HP6P': [],
    'HP7N': [], 'HP7P': [], 'HP8N': [], 'HP8P': [], 'HP9N': [], 'HP9P': [], 'HP10N': [], 'HP10P': [], 'HP11N': [], 'HP11P': [],

    'ATF': [],
    'AP1N': [], 'AP1P': [], 'AP2N': [], 'AP2P': [], 'AP3N': [], 'AP3P': [], 'AP4N': [], 'AP4P': [], 'AP5N': [], 'AP5P': [], 'AP6N': [], 'AP6P': [],
    'AP7N': [], 'AP7P': [], 'AP8N': [], 'AP8P': [], 'AP9N': [], 'AP9P': [], 'AP10N': [], 'AP10P': [], 'AP11N': [], 'AP11P': [],
}

# data_file = open(os.getcwd() + '\\csvData\\match\\matchLineups2.csv', 'w', newline='', encoding='utf-8')
data_file = open(os.getcwd() + '/csvData/match/matchLineups2.csv', 'w', newline='', encoding='utf-8')
print(os.getcwd() + '/csvData/match/matchLineups2.csv')
csv_writer = csv.writer(data_file)


# file_paths = []
# for league, seasons in leaguesFileDic.items():
#     path = os.getcwd() + '\\data\\teams\\' + league 
#     for f in glob.glob(path + "**/*.json", recursive=True):
#         file_paths.append(f)

file_paths = []
for league, seasons in leaguesFileDic.items():
    for season in seasons:
        # path = os.getcwd() + '\\data\\matchLineups\\' + league + '\\' + season
        path = os.getcwd() + '/data/matchLineups/' + league + '/' + season
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
        if len(data['home']['squad']) != 11 or len(data['away']['squad']) != 11:
            print(file_path)
            break

        data = data['data']

        rowData['match_id'].append(match_id)
        rowData['season'].append(season)

        rowData['HTF'].append(data['home']['formation']) if data['home']['formation'] != None else rowData['HTF'].append('NaN')

        cout = 1        
        for player in data['home']['squad']:
            if cout > 11: 
                print(file_path)
                break
            rowData['HP' + str(cout) +'N'].append(player['number']) if player['number'] != None else rowData['HP' + str(cout) +'N'].append('NaN')
            rowData['HP' + str(cout) +'P'].append(player['position']) if player['position'] != None else rowData['HP' + str(cout) +'P'].append('NaN')
            cout = cout + 1

        rowData['ATF'].append(data['home']['formation']) if data['home']['formation'] != None else rowData['ATF'].append('NaN')

        cout = 1
        for player in data['away']['squad']:
            if cout > 11: 
                print(file_path)
                break
            rowData['AP' + str(cout) +'N'].append(player['number']) if player['number'] != None else rowData['AP' + str(cout) +'N'].append('NaN')
            rowData['AP' + str(cout) +'P'].append(player['position']) if player['position'] != None else rowData['AP' + str(cout) +'P'].append('NaN')
            cout = cout + 1
            

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


