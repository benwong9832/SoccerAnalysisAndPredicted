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
  'match_id': [], 
  # 'date': [], 
  'team_id': [], 
#   'passes_total': [], 'passes_accurate': [], 'passes_percentage': [], 
  'fouls': [], 'injuries': [], 'corners': [], 'offsides': [], 'shots_total': [], 
  'shots_on_target': [], 'shots_off_target': [], 'shots_blocked': [],# 'possessiontime': [], 
  'possessionpercent': [], 
  'yellowcards': [], 'yellowredcards': [], 'redcards': [], 'substitutions': [], 'goal_kick': [], 
  'goal_attempts': [], 'free_kick': [], 'throw_in': [], 'ball_safe': [], 'goals': [], 
  'penalties': [], 'attacks': [], 'dangerous_attacks': []
}

data_file = open(os.getcwd() + '\\csvData\\stats\\matchStats.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(data_file)


# file_paths = []
# for league, seasons in leaguesFileDic.items():
#     path = os.getcwd() + '\\data\\teams\\' + league 
#     for f in glob.glob(path + "**/*.json", recursive=True):
#         file_paths.append(f)

file_paths = []
for league, seasons in leaguesFileDic.items():
    for season in seasons:
        path = os.getcwd() + '\\data\\matchStats\\' + league + '\\' + season
        for f in glob.glob(path + "**/*.json", recursive=True):
            file_paths.append(f)

# for f in file_paths:
#     print(f)


count = 0
for file_path in file_paths:
    custLeagueName = file_path.split('\\')[-1].split('_')[1]
    date = file_path.split('\\')[-1].split('_')[-2].split('.')[0]
    match_id = file_path.split('\\')[-1].split('_')[-1].split('.')[0]
    # leagueName = leaguesNameDic[custLeagueName]
    # print(custLeagueName, date, match_id)

    with open(file_path, encoding='utf-8') as json_file:
    	data = json.load(json_file)
    
    if 'data' in data:
        data = data['data']

        for team in data:
            rowData['match_id'].append(match_id)
            # rowData['date'].append(date)
            rowData['team_id'].append(team['team_id']) if team['team_id'] != None else rowData['team_id'].append('NaN')

            # rowData['passes_total'].append(team['passes']['total']) if team['passes']['total'] != None else rowData['passes_total'].append('NaN')
            # rowData['passes_accurate'].append(team['passes']['accurate']) if team['passes']['accurate'] != None else rowData['passes_accurate'].append('NaN')
            # rowData['passes_percentage'].append(team['passes']['percentage']) if team['passes']['percentage'] != None else rowData['passes_percentage'].append('NaN')

            rowData['fouls'].append(int(team['fouls'])) if team['fouls'] != None else rowData['fouls'].append('NaN')
            rowData['injuries'].append(team['injuries']) if team['injuries'] != None else rowData['injuries'].append('NaN')
            # rowData['injuries'].append(team['injuries']) if team['injuries'] != None else rowData['injuries'].append(0)
            
            rowData['corners'].append(int(team['corners'])) if team['corners'] != None else rowData['corners'].append('NaN')
            rowData['offsides'].append(team['offsides']) if team['offsides'] != None else rowData['offsides'].append('NaN')
            rowData['shots_total'].append(team['shots_total']) if team['shots_total'] != None else rowData['shots_total'].append('NaN')
            rowData['shots_on_target'].append(int(team['shots_on_target'])) if team['shots_on_target'] != None else rowData['shots_on_target'].append('NaN')
            rowData['shots_off_target'].append(int(team['shots_off_target'])) if team['shots_off_target'] != None else rowData['shots_off_target'].append('NaN')
            rowData['shots_blocked'].append(int(team['shots_blocked'])) if team['shots_blocked'] != None else rowData['shots_blocked'].append('NaN')
            # rowData['possessiontime'].append(team['possessiontime']) if team['possessiontime'] != None else rowData['possessiontime'].append('NaN')
            rowData['possessionpercent'].append(team['possessionpercent']) if team['possessionpercent'] != None else rowData['possessionpercent'].append('NaN')
            rowData['yellowcards'].append(team['yellowcards']) if team['yellowcards'] != None else rowData['yellowcards'].append('NaN')
            rowData['yellowredcards'].append(team['yellowredcards']) if team['yellowredcards'] != None else rowData['yellowredcards'].append('NaN')
            rowData['redcards'].append(team['redcards']) if team['redcards'] != None else rowData['redcards'].append('NaN')
            rowData['substitutions'].append(team['substitutions']) if team['substitutions'] != None else rowData['substitutions'].append('NaN')
            rowData['goal_kick'].append(team['goal_kick']) if team['goal_kick'] != None else rowData['goal_kick'].append('NaN')
            rowData['goal_attempts'].append(team['goal_attempts']) if team['goal_attempts'] != None else rowData['goal_attempts'].append('NaN')
            rowData['free_kick'].append(team['free_kick']) if team['free_kick'] != None else rowData['free_kick'].append('NaN')
            rowData['throw_in'].append(team['throw_in']) if team['throw_in'] != None else rowData['throw_in'].append('NaN')
            rowData['ball_safe'].append(team['ball_safe']) if team['ball_safe'] != None else rowData['ball_safe'].append('NaN')
            rowData['goals'].append(team['goals']) if team['goals'] != None else rowData['goals'].append('NaN')
            rowData['penalties'].append(team['penalties']) if team['penalties'] != None else rowData['penalties'].append('NaN')
            rowData['attacks'].append(team['attacks']) if team['attacks'] != None else rowData['attacks'].append('NaN')
            rowData['dangerous_attacks'].append(team['dangerous_attacks']) if team['dangerous_attacks'] != None else rowData['dangerous_attacks'].append('NaN')

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


