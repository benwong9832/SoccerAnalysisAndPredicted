import json
import csv
import os
import glob
import requests
from urllib import request, parse
import dataDictionary
import sys
import common

# TODO: venue, referee

# define 
leaguesFileDic = dataDictionary.leaguesFileDic
leaguesDic = dataDictionary.leaguesDic
seasonsDic = dataDictionary.seasonsDic
leagueIdContinentDic = dataDictionary.leagueIdContinentDic
leagueIdCountryDic = dataDictionary.leagueIdCountryDic
leaguesNameDic = dataDictionary.leaguesNameDic
leaguesNameToId = dataDictionary.leaguesNameToId

# 'continent'
rowData = {
    'league': [], 'season': [], 'match_id': [], 'status': [], 'round_name': [],
    'referee_id': [], 'venue_id': [], #'pitch_id': [],
    'stage_name': [], 'group_name': [], 'week': [], 'deleted': [], 
    'datetime': [], 
    'home_tean_id': [],'home_form': [], 'home_coach_id': [], 'away_tean_id': [],'away_form': [], 'away_coach_id': [], 
    'home_score': [], 'away_score': [], 'ht_score': [], 'ft_score': [], #'et_score': [], 'ps_score': [], 
    'home_standings_position': [], 'away_standings_position': [],
    'weather_desc': [], 'fahrenheit': [], 'wind_kmph': [], 'wind_miles': [], 'wind_direction': [], 'humidity_percent': [], 'pressure': [],
    'result': []
}

data_file = open(os.getcwd() + '\\csvData\\fixtures\\fixtures.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(data_file)


# file_paths = []
# for league, seasons in leaguesFileDic.items():
#     path = os.getcwd() + '\\data\\teams\\' + league 
#     for f in glob.glob(path + "**/*.json", recursive=True):
#         file_paths.append(f)

file_paths = []
for league, seasons in leaguesFileDic.items():
    # for season in seasons:
    path = os.getcwd() + '\\data\\fixtures\\' + league
    for f in glob.glob(path + "**/*.json", recursive=True):
        file_paths.append(f)

# for f in file_paths:
#     print(f)


count = 0
for file_path in file_paths:
    custLeagueName = file_path.split('\\')[-1].split('_')[1]
    season = file_path.split('\\')[-1].split('_')[-1].split('.')[0]
    custLeagueName = leaguesNameDic[custLeagueName]
    # print(custLeagueName, season)

    with open(file_path, encoding='utf-8') as json_file:
    	json_datas = json.load(json_file)
    
    if 'data' in json_datas:
        datas = json_datas['data']

        for data in datas:
            # print(data)
            rowData['league'].append(custLeagueName)
            rowData['season'].append(season)
            rowData['match_id'].append(data['id'])
            rowData['status'].append(data['status_name']) if data['status_name'] != None else rowData['status'].append('NaN')
            #rowData['status_period'].append(data['status_period']) if data['status_period'] != None else rowData['status_period'].append('NaN')
            #rowData['pitch'].append(data['pitch']) if data['pitch'] != None else rowData['pitch'].append('NaN')
            rowData['venue_id'].append(data['venue_id']) if data['venue_id'] != None else rowData['venue_id'].append('NaN')
            rowData['referee_id'].append(data['referee_id']) if data['referee_id'] != None else rowData['referee_id'].append('NaN')
            if 'round_name' in data:
                rowData['round_name'].append(data['round_name']) if data['round_name'] != None else rowData['round_name'].append('NaN')
            else:
                rowData['round_name'].append('NaN')
            
            rowData['stage_name'].append(data['stage_name']) if data['stage_name'] != None else rowData['stage_name'].append('NaN')
            rowData['group_name'].append(data['group_name']) if data['group_name'] != None else rowData['group_name'].append('NaN')
            #rowData['aggregate_id'].append(data['aggregate_id']) if data['aggregate_id'] != None else rowData['aggregate_id'].append('NaN')
            #rowData['leg'].append(data['leg']) if data['leg'] != None else rowData['leg'].append('NaN')
            if 'week' in data:
                rowData['week'].append(int(data['week'])) if data['week'] != None else rowData['week'].append('NaN')
            else:
                rowData['week'].append('NaN')
            rowData['deleted'].append(data['deleted']) if data['deleted'] != None else rowData['deleted'].append('NaN')

            rowData['datetime'].append(data['time']['datetime']) if data['time']['datetime'] != None else rowData['datetime'].append('NaN')
            
            rowData['home_tean_id'].append(data['teams']['home']['id']) if data['teams']['home']['id'] != None else rowData['home_tean_id'].append('NaN')
            rowData['home_form'].append(data['teams']['home']['form']) if data['teams']['home']['form'] != None else rowData['home_form'].append('NaN')
            rowData['home_coach_id'].append(data['teams']['home']['coach_id']) if data['teams']['home']['coach_id'] != None else rowData['home_coach_id'].append('NaN')
            
            rowData['away_tean_id'].append(data['teams']['away']['id']) if data['teams']['away']['id'] != None else rowData['away_tean_id'].append('NaN')
            rowData['away_form'].append(data['teams']['away']['form']) if data['teams']['away']['form'] != None else rowData['away_form'].append('NaN')
            rowData['away_coach_id'].append(data['teams']['away']['coach_id']) if data['teams']['away']['coach_id'] != None else rowData['away_coach_id'].append('NaN')

            rowData['home_score'].append(data['scores']['home_score']) if data['scores']['home_score'] != None else rowData['home_score'].append('NaN')
            rowData['away_score'].append(data['scores']['away_score']) if data['scores']['away_score'] != None else rowData['away_score'].append('NaN')
            rowData['ht_score'].append(data['scores']['ht_score']) if data['scores']['ht_score'] != None else rowData['ht_score'].append('NaN')
            rowData['ft_score'].append(data['scores']['ft_score']) if data['scores']['ft_score'] != None else rowData['ft_score'].append('NaN')
            # rowData['et_score'].append(data['scores']['et_score']) if data['scores']['et_score'] != None else rowData['et_score'].append('NaN')
            # rowData['ps_score'].append(data['scores']['ps_score']) if data['scores']['ps_score'] != None else rowData['ps_score'].append('NaN')
            
            if data['scores']['ft_score'] != None:
                result = data['scores']['ft_score'].split('-')
                if result[0] != '' and result[1] != '':
                    if int(result[0]) == int(result[1]):
                        rowData['result'].append("draw")
                    elif int(result[0]) > int(result[1]):
                        rowData['result'].append("home")
                    else:
                        rowData['result'].append("away")
                else:
                    rowData['result'].append("NaN")
            else:
                rowData['result'].append("NaN")
            
            rowData['home_standings_position'].append(data['standings']['home_position']) if data['standings']['home_position'] != None else rowData['home_standings_position'].append('NaN')
            rowData['away_standings_position'].append(data['standings']['away_position']) if data['standings']['away_position'] != None else rowData['away_standings_position'].append('NaN')

            if data['weather_report'] != None and data['weather_report'] != False:
                rowData['weather_desc'].append(data['weather_report']['desc']) if data['weather_report']['desc'] != None else rowData['weather_desc'].append('NaN')
                rowData['fahrenheit'].append(data['weather_report']['temp']['fahrenheit']) if data['weather_report']['temp']['fahrenheit'] != None else rowData['fahrenheit'].append('NaN')
                rowData['wind_kmph'].append(data['weather_report']['wind']['kmph']) if data['weather_report']['wind']['kmph'] != None else rowData['wind_kmph'].append('NaN')
                rowData['wind_miles'].append(data['weather_report']['wind']['miles']) if data['weather_report']['wind']['miles'] != None else rowData['wind_miles'].append('NaN')
                rowData['wind_direction'].append(data['weather_report']['wind']['direction']) if data['weather_report']['wind']['direction'] != None else rowData['wind_direction'].append('NaN')
                rowData['humidity_percent'].append(data['weather_report']['humidity_percent']) if data['weather_report']['humidity_percent'] != None else rowData['humidity_percent'].append('NaN')
                rowData['pressure'].append(data['weather_report']['pressure']) if data['weather_report']['pressure'] != None else rowData['pressure'].append('NaN')
            else:
                rowData['weather_desc'].append('NaN')
                rowData['fahrenheit'].append('NaN')
                rowData['wind_kmph'].append('NaN')
                rowData['wind_miles'].append('NaN')
                rowData['wind_direction'].append('NaN')
                rowData['humidity_percent'].append('NaN')
                rowData['pressure'].append('NaN')
                


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


