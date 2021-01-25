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
  'continent': [], 'country': [], 'league': [], 'season': [], 'team_name': [], 'formation': [],
  'player_id': [], 'name': [], 'common_name': [], 'firstname': [], 'lastname': [], 
  'weight': [], 'height': [], 'age': [], 'country': [], #, 'img': []
  'number': [], 'captain': [], 'position': [], 'order': []
#   ,
#   'total': [], 'status': [], 'result': [], 'points': [],
#   'overall_games_played': [], 'overall_won': [], 'overall_draw': [], 'overall_lost': [], 'overall_goals_diff': [], 'overall_goals_scored': [], 'overall_goals_against': [], 'overall_points': [], 'overall_position': [], 
#   'home_games_played': [], 'home_won': [], 'home_draw': [], 'home_lost': [], 'home_goals_diff': [], 'home_goals_scored': [], 'home_goals_against': [], 'home_points': [], 'home_position': [], 
#   'away_games_played': [], 'away_won': [], 'away_draw': [], 'away_lost': [], 'away_goals_diff': [], 'away_goals_scored': [], 'away_goals_against': [], 'away_points': [], 'away_position': []
}

data_file = open(os.getcwd() + '\\csvData\\teams\\teamsSquad.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(data_file)


# file_paths = []
# for league, seasons in leaguesFileDic.items():
#     path = os.getcwd() + '\\data\\teams\\' + league 
#     for f in glob.glob(path + "**/*.json", recursive=True):
#         file_paths.append(f)

file_paths = []
for league, seasons in leaguesFileDic.items():
    for season in seasons:
        path = os.getcwd() + '\\data\\teamsSquad\\' + league + '\\' + season
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

        for index, player in enumerate(data['squad']):
            for key, value in player.items(): 
        # for index, player in data['squad'].items():
                if key == 'player':
                    rowData['continent'].append(leagueIdContinentDic.get(leaguesNameToId[leagueName]))
                    rowData['country'].append(leagueIdCountryDic.get(leaguesNameToId[leagueName]))
                    rowData['league'].append(leagueName)
                    rowData['season'].append(season)
                    rowData['team_name'].append(team_name)
                    rowData['formation'].append(data['formation']) if data['formation'] != None else rowData['formation'].append('NaN')
                    
                    rowData['player_id'].append(value['id']) if value['id'] != None else rowData['player_id'].append('NaN')
                    rowData['name'].append(value['name']) if value['name'] != None else rowData['name'].append('NaN')
                    rowData['common_name'].append(value['common_name']) if value['common_name'] != None else rowData['common_name'].append('NaN')
                    rowData['firstname'].append(value['firstname']) if value['firstname'] != None else rowData['firstname'].append('NaN')
                    rowData['lastname'].append(value['lastname']) if value['lastname'] != None else rowData['lastname'].append('NaN')
                    rowData['weight'].append(value['weight']) if value['weight'] != None else rowData['weight'].append('NaN')
                    rowData['height'].append(value['height']) if value['height'] != None else rowData['height'].append('NaN')
                    # print(leagueName)
                    # print(season)
                    # print(team_name)
                    # print(value['age'])
                    
                    if 'age' in value:
                        rowData['age'].append(value['age']) if value['age'] != None else rowData['age'].append('NaN')
                    else:
                        rowData['age'].append('NaN')

                    # save img
                    if 'img' in value and value['img'] is not None:
                        checked_player = common.checkExistValInFile(os.getcwd() + "\\data\\img\\player\\checkedPlayerId.csv", str(value['id']))

                        if not checked_player:
                            response = requests.request("GET", value['img'], headers = {}, data = {})
                            common.appendValInFile(os.getcwd() + "\\data\\img\\player\\checkedPlayerId.csv", str(value['id']))
                            sys.stdout.write(str(response.status_code) + ' ' + value['img'] + ' \n')
                            sys.stdout.flush()
                            if response.status_code != 404:
                                img_url = parse.urlparse(value['img'])
                                filename, file_ext = os.path.splitext(os.path.basename(img_url.path))

                                save_img_path = os.getcwd() + "\\data\\img\\player\\" + team_name
                                if not os.path.exists(save_img_path):
                                    os.mkdir(save_img_path)

                                img_name = value['common_name'] + '_icon' + file_ext
                                
                                if not os.path.exists(save_img_path + '\\' + img_name):
                                    count += 1
                                    sys.stdout.write('saved image ' + str(count) + '\n')  # same as print
                                    sys.stdout.flush()

                                    f = open(save_img_path + '\\' + img_name, 'wb')
                                    f.write(response.content)
                                    f.close()

                    rowData['country'].append(value['country']['name']) if value['country']['name'] != None else rowData['country'].append('NaN')
                elif key == 'number':
                    rowData['number'].append(value) if value != None else rowData['number'].append('NaN')
                elif key == 'captain':
                    rowData['captain'].append(value) if value != None else rowData['captain'].append('NaN')
                elif key == 'position':
                    rowData['position'].append(value) if value != None else rowData['position'].append('NaN')
                elif key == 'order':
                    rowData['order'].append(value) if value != None else rowData['order'].append('NaN')


        # for index, team in enumerate(data):
        #     rowData['continent'].append(leagueIdContinentDic.get(leaguesNameToId[leagueName]))
        #     rowData['country'].append(leagueIdCountryDic.get(leaguesNameToId[leagueName]))
        #     rowData['league'].append(leagueName)
        #     rowData['season'].append(season)
        #     rowData['team_name'].append(team_name)
        #     if key == 'formation':
        #         rowData['formation'].append(data['formation']) if data['formation'] != None else rowData['result'].append('NaN')
        #     elif key == 'squad':
        #         for player in data
        #         rowData['team_name'].append(standing[key]) if standing[key] != None else rowData['result'].append('NaN')

            # for key, value in standing.items():
            #     if key == 'overall' or key == 'home' or key == 'away':
            #         rowData[key + '_games_played'].append(standing[key]['games_played'])
            #         rowData[key + '_won'].append(standing[key]['won'])
            #         rowData[key + '_draw'].append(standing[key]['draw'])
            #         rowData[key + '_lost'].append(standing[key]['lost'])
            #         rowData[key + '_goals_diff'].append(standing[key]['goals_diff'])
            #         rowData[key + '_goals_scored'].append(standing[key]['goals_scored'])
            #         rowData[key + '_goals_against'].append(standing[key]['goals_against'])
            #         rowData[key + '_points'].append(standing[key]['points'])
            #         rowData[key + '_position'].append(standing[key]['position'])
            #     elif key == 'team_name':
            #         rowData['team_name'].append(standing[key]) if standing[key] != None else rowData['result'].append('NaN')
            #     elif key == 'total':
            #         rowData['total'].append(standing[key]) if standing[key] != None else rowData['result'].append('NaN')
            #     elif key == 'status':
            #         rowData['status'].append(standing[key]) if standing[key] != None else rowData['result'].append('NaN')
            #     elif key == 'result':
            #         rowData['result'].append(standing[key]) if standing[key] != None else rowData['result'].append('NaN')
            #     elif key == 'points':
            #         rowData['points'].append(standing[key]) if standing[key] != None else row.append('NaN')



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


