import json
import csv
import os
import glob
import requests
from urllib import request, parse
import dataDictionary

# define 
leaguesFileDic = dataDictionary.leaguesFileDic
leaguesDic = dataDictionary.leaguesDic
seasonsDic = dataDictionary.seasonsDic
leagueIdContinentDic = dataDictionary.leagueIdContinentDic
leagueIdCountryDic = dataDictionary.leagueIdCountryDic

file_paths = []

for league, seasons in leaguesFileDic.items():
    path = os.getcwd() + '\\data\\standings\\' + league 
    for f in glob.glob(path + "**/*.json", recursive=True):
        file_paths.append(f)

# for f in file_paths:
#     print(f)

data_file = open(os.getcwd() + '\\csvData\\standings\\standingsAll.csv', 'w', newline='')
csv_writer = csv.writer(data_file)


rowData = {
  'continent': [],
  'country': [],
  'league': [], 
  'season': [],
  'team_name': [],
  'total': [], 'status': [], 'result': [], 'points': [],
  'overall_games_played': [], 'overall_won': [], 'overall_draw': [], 'overall_lost': [], 'overall_goals_diff': [], 'overall_goals_scored': [], 'overall_goals_against': [], 'overall_points': [], 'overall_position': [], 
  'home_games_played': [], 'home_won': [], 'home_draw': [], 'home_lost': [], 'home_goals_diff': [], 'home_goals_scored': [], 'home_goals_against': [], 'home_points': [], 'home_position': [], 
  'away_games_played': [], 'away_won': [], 'away_draw': [], 'away_lost': [], 'away_goals_diff': [], 'away_goals_scored': [], 'away_goals_against': [], 'away_points': [], 'away_position': []
}

# csv_writer.writerow(hearders)

coun = 0
for file_path in file_paths:
    with open(file_path) as json_file:
    	data = json.load(json_file)
    
    if 'data' in data:
        data = data['data']

        for count, standing in enumerate(data['standings']):
            rowData['continent'].append(leagueIdContinentDic.get(int(data['league_id'])))
            rowData['country'].append(leagueIdCountryDic.get(int(data['league_id'])))
            rowData['league'].append(leaguesDic.get(int(data['league_id'])))
            rowData['season'].append(seasonsDic.get(int(data['season_id'])))
            for key, value in standing.items():
                if key == 'overall' or key == 'home' or key == 'away':
                    rowData[key + '_games_played'].append(standing[key]['games_played'])
                    rowData[key + '_won'].append(standing[key]['won'])
                    rowData[key + '_draw'].append(standing[key]['draw'])
                    rowData[key + '_lost'].append(standing[key]['lost'])
                    rowData[key + '_goals_diff'].append(standing[key]['goals_diff'])
                    rowData[key + '_goals_scored'].append(standing[key]['goals_scored'])
                    rowData[key + '_goals_against'].append(standing[key]['goals_against'])
                    rowData[key + '_points'].append(standing[key]['points'])
                    rowData[key + '_position'].append(standing[key]['position'])
                elif key == 'team_name':
                    rowData['team_name'].append(standing[key]) if standing[key] != None else rowData['result'].append('NaN')
                elif key == 'total':
                    rowData['total'].append(standing[key]) if standing[key] != None else rowData['result'].append('NaN')
                elif key == 'status':
                    rowData['status'].append(standing[key]) if standing[key] != None else rowData['result'].append('NaN')
                elif key == 'result':
                    rowData['result'].append(standing[key]) if standing[key] != None else rowData['result'].append('NaN')
                elif key == 'points':
                    rowData['points'].append(standing[key]) if standing[key] != None else row.append('NaN')

            # csv_writer.writerow(row)

# insert header
row = []
for header, data in rowData.items():
    row.append(header)
csv_writer.writerow(row)

# insert data
lenRowData = len(rowData['league'])
for i in range(len(rowData['league'])):
      row = []
      for header, data in rowData.items():
            row.append(rowData[header][i])
      csv_writer.writerow(row)
      
print('done')
