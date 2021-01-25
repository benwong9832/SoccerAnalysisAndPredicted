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
    'league': [], 'season': [], 'season_id': [], 'number_of_teams': [], 'number_of_matches': [], 
    'team_id_most_scored': [], 'team_most_scored_total_goals': [], 
    'player_id_most_scored': [], 'player_most_scored_total_goals': [], 
    'substituted_in_total': [], 'substituted_avg_per_match': [], 'substituted_avg_every_minutes': [], 
    'assists_total': [], 'assists_avg_per_match': [], 'assists_avg_every_minutes': [], 

    'cards_total': [], 'cards_avg_per_match': [], 'cards_avg_every_minutes': [], 
    'yellow_cards_total': [], 'yellow_cards_avg_per_match': [], 'yellow_cards_avg_every_minutes': [], 
    'yellowred_cards_total': [], 'yellowred_cards_avg_per_match': [], 'yellowred_cards_avg_every_minutes': [], 
    'red_cards_total': [], 'red_cards_avg_per_match': [], 'red_cards_avg_every_minutes': [], 

    'goals_total': [], 'goals_percentage_total_goals': [], 'goals_avg_per_match': [], 'goals_avg_every_minutes': [], 
    'home_goals_total': [], 'home_goals_percentage_total_goals': [], 'home_goals_avg_per_match': [], 'home_goals_avg_every_minutes': [], 
    'away_goals_total': [], 'away_goals_percentage_total_goals': [], 'away_goals_avg_per_match': [], 'away_goals_avg_every_minutes': [], 
    
    'clean_sheets_total': [], 'clean_sheets_avg_per_match': [], 
    'home_clean_sheets_total': [], 'home_clean_sheets_avg_per_match': [], 
    'away_clean_sheets_total': [], 'away_clean_sheets_avg_per_match': [], 

    'goals_scored_range_total_0To15': [], 'goals_scored_range_percentage_total_goals_0To15': [], 
    'goals_scored_range_total_15To30': [], 'goals_scored_range_percentage_total_goals_15To30': [], 
    'goals_scored_range_total_30To45': [], 'goals_scored_range_percentage_total_goals_30To45': [], 
    'goals_scored_range_total_45To60': [], 'goals_scored_range_percentage_total_goals_45To60': [], 
    'goals_scored_range_total_60To75': [], 'goals_scored_range_percentage_total_goals_60To75': [], 
    'goals_scored_range_total_75To90': [], 'goals_scored_range_percentage_total_goals_75To90': [], 
    'goals_scored_range_total_90To120': [], 'goals_scored_range_percentage_total_goals_90To120': [], 

    'goal_line_total_over_0p5': [], 'goal_line_percentage_total_matches_over_0p5': [], 
    'goal_line_total_over_1p5': [], 'goal_line_percentage_total_matches_over_1p5': [], 
    'goal_line_total_over_2p5': [], 'goal_line_percentage_total_matches_over_2p5': [], 
    'goal_line_total_over_3p5': [], 'goal_line_percentage_total_matches_over_3p5': [], 
    'goal_line_total_over_4p5': [], 'goal_line_percentage_total_matches_over_4p5': [], 
    'goal_line_total_over_5p5': [], 'goal_line_percentage_total_matches_over_5p5': [], 

    'goal_line_total_under_0p5': [], 'goal_line_percentage_total_matches_under_0p5': [], 
    'goal_line_total_under_1p5': [], 'goal_line_percentage_total_matches_under_1p5': [], 
    'goal_line_total_under_2p5': [], 'goal_line_percentage_total_matches_under_2p5': [], 
    'goal_line_total_under_3p5': [], 'goal_line_percentage_total_matches_under_3p5': [], 
    'goal_line_total_under_4p5': [], 'goal_line_percentage_total_matches_under_4p5': [], 
    'goal_line_total_under_5p5': [], 'goal_line_percentage_total_matches_under_5p5': [], 
}

data_file = open(os.getcwd() + '\\csvData\\stats\\seasonStats.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(data_file)


# file_paths = []
# for league, seasons in leaguesFileDic.items():
#     path = os.getcwd() + '\\data\\teams\\' + league 
#     for f in glob.glob(path + "**/*.json", recursive=True):
#         file_paths.append(f)

file_paths = []
for league, seasons in leaguesFileDic.items():
    for season in seasons:
        path = os.getcwd() + '\\data\\seasonStats\\' + league #+ '\\' + season
        for f in glob.glob(path + "**/*.json", recursive=True):
            file_paths.append(f)

# for f in file_paths:
#     print(f)


count = 0
for file_path in file_paths:
    custLeagueName = file_path.split('\\')[-1].split('_')[1]
    date = file_path.split('\\')[-1].split('_')[-2].split('.')[0]
    season = file_path.split('\\')[-1].split('_')[-1].split('.')[0]
    # leagueName = leaguesNameDic[custLeagueName]
    # print(custLeagueName, date, season)

    with open(file_path, encoding='utf-8') as json_file:
    	data = json.load(json_file)
    
    if 'data' in data:
        data = data['data']

        rowData['league'].append(custLeagueName)
        rowData['season'].append(season)
        rowData['season_id'].append(data['season_id']) if data['season_id'] != None else rowData['season_id'].append('NaN')
        rowData['number_of_teams'].append(data['number_of_teams']) if data['number_of_teams'] != None else rowData['number_of_teams'].append('NaN')
        rowData['number_of_matches'].append(data['number_of_matches']) if data['number_of_matches'] != None else rowData['number_of_matches'].append('NaN')
        
        rowData['team_id_most_scored'].append(data['team_most_scored']['id']) if data['team_most_scored']['id'] != None else rowData['team_id_most_scored'].append('NaN')
        rowData['team_most_scored_total_goals'].append(data['team_most_scored']['total_goals']) if data['team_most_scored']['total_goals'] != None else rowData['team_most_scored_total_goals'].append('NaN')

        rowData['player_id_most_scored'].append(data['player_most_scored']['id']) if data['player_most_scored']['id'] != None else rowData['player_id_most_scored'].append('NaN')
        rowData['player_most_scored_total_goals'].append(data['player_most_scored']['total_goals']) if data['player_most_scored']['total_goals'] != None else rowData['player_most_scored_total_goals'].append('NaN')

        rowData['substituted_in_total'].append(data['substituted_in']['total']) if data['substituted_in']['total'] != None else rowData['substituted_in_total'].append('NaN')
        rowData['substituted_avg_per_match'].append(data['substituted_in']['avg_per_match']) if data['substituted_in']['avg_per_match'] != None else rowData['substituted_avg_per_match'].append('NaN')
        rowData['substituted_avg_every_minutes'].append(data['substituted_in']['avg_every_minutes']) if data['substituted_in']['avg_every_minutes'] != None else rowData['substituted_avg_every_minutes'].append('NaN')

        rowData['assists_total'].append(data['assists']['total']) if data['assists']['total'] != None else rowData['assists_total'].append('NaN')
        rowData['assists_avg_per_match'].append(data['assists']['avg_per_match']) if data['assists']['avg_per_match'] != None else rowData['assists_avg_per_match'].append('NaN')
        rowData['assists_avg_every_minutes'].append(data['assists']['avg_every_minutes']) if data['assists']['avg_every_minutes'] != None else rowData['assists_avg_every_minutes'].append('NaN')


        rowData['cards_total'].append(data['cards']['total']['total']) if data['cards']['total']['total'] != None else rowData['cards_total'].append('NaN')
        rowData['cards_avg_per_match'].append(data['cards']['total']['avg_per_match']) if data['cards']['total']['avg_per_match'] != None else rowData['cards_avg_per_match'].append('NaN')
        rowData['cards_avg_every_minutes'].append(data['cards']['total']['avg_every_minutes']) if data['cards']['total']['avg_every_minutes'] != None else rowData['cards_avg_every_minutes'].append('NaN')

        rowData['yellow_cards_total'].append(data['cards']['yellow']['total']) if data['cards']['yellow']['total'] != None else rowData['yellow_cards_total'].append('NaN')
        rowData['yellow_cards_avg_per_match'].append(data['cards']['yellow']['avg_per_match']) if data['cards']['yellow']['avg_per_match'] != None else rowData['yellow_cards_avg_per_match'].append('NaN')
        rowData['yellow_cards_avg_every_minutes'].append(data['cards']['yellow']['avg_every_minutes']) if data['cards']['yellow']['avg_every_minutes'] != None else rowData['yellow_cards_avg_every_minutes'].append('NaN')

        rowData['yellowred_cards_total'].append(data['cards']['yellowred']['total']) if data['cards']['yellowred']['total'] != None else rowData['yellowred_cards_total'].append('NaN')
        rowData['yellowred_cards_avg_per_match'].append(data['cards']['yellowred']['avg_per_match']) if data['cards']['yellowred']['avg_per_match'] != None else rowData['yellowred_cards_avg_per_match'].append('NaN')
        rowData['yellowred_cards_avg_every_minutes'].append(data['cards']['yellowred']['avg_every_minutes']) if data['cards']['yellowred']['avg_every_minutes'] != None else rowData['yellowred_cards_avg_every_minutes'].append('NaN')

        rowData['red_cards_total'].append(data['cards']['red']['total']) if data['cards']['red']['total'] != None else rowData['red_cards_total'].append('NaN')
        rowData['red_cards_avg_per_match'].append(data['cards']['red']['avg_per_match']) if data['cards']['red']['avg_per_match'] != None else rowData['red_cards_avg_per_match'].append('NaN')
        rowData['red_cards_avg_every_minutes'].append(data['cards']['red']['avg_every_minutes']) if data['cards']['red']['avg_every_minutes'] != None else rowData['red_cards_avg_every_minutes'].append('NaN')


        rowData['goals_total'].append(data['goals']['overall']['total']) if data['goals']['overall']['total'] != None else rowData['goals_total'].append('NaN')
        rowData['goals_percentage_total_goals'].append(data['goals']['overall']['avg_per_match']) if data['goals']['overall']['avg_per_match'] != None else rowData['goals_percentage_total_goals'].append('NaN')
        rowData['goals_avg_per_match'].append(data['goals']['overall']['avg_every_minutes']) if data['goals']['overall']['avg_every_minutes'] != None else rowData['goals_avg_per_match'].append('NaN')
        rowData['goals_avg_every_minutes'].append(data['goals']['overall']['avg_every_minutes']) if data['goals']['overall']['avg_every_minutes'] != None else rowData['goals_avg_every_minutes'].append('NaN')

        rowData['home_goals_total'].append(data['goals']['home']['total']) if data['goals']['home']['total'] != None else rowData['home_goals_total'].append('NaN')
        rowData['home_goals_percentage_total_goals'].append(data['goals']['home']['avg_per_match']) if data['goals']['home']['avg_per_match'] != None else rowData['home_goals_percentage_total_goals'].append('NaN')
        rowData['home_goals_avg_per_match'].append(data['goals']['home']['avg_every_minutes']) if data['goals']['home']['avg_every_minutes'] != None else rowData['home_goals_avg_per_match'].append('NaN')
        rowData['home_goals_avg_every_minutes'].append(data['goals']['home']['avg_every_minutes']) if data['goals']['home']['avg_every_minutes'] != None else rowData['home_goals_avg_every_minutes'].append('NaN')

        rowData['away_goals_total'].append(data['goals']['away']['total']) if data['goals']['away']['total'] != None else rowData['away_goals_total'].append('NaN')
        rowData['away_goals_percentage_total_goals'].append(data['goals']['away']['avg_per_match']) if data['goals']['away']['avg_per_match'] != None else rowData['away_goals_percentage_total_goals'].append('NaN')
        rowData['away_goals_avg_per_match'].append(data['goals']['away']['avg_every_minutes']) if data['goals']['away']['avg_every_minutes'] != None else rowData['away_goals_avg_per_match'].append('NaN')
        rowData['away_goals_avg_every_minutes'].append(data['goals']['away']['avg_every_minutes']) if data['goals']['away']['avg_every_minutes'] != None else rowData['away_goals_avg_every_minutes'].append('NaN')

        rowData['clean_sheets_total'].append(data['clean_sheets']['overall']['total']) if data['clean_sheets']['overall']['total'] != None else rowData['clean_sheets_total'].append('NaN')
        rowData['clean_sheets_avg_per_match'].append(data['clean_sheets']['overall']['avg_per_match']) if data['clean_sheets']['overall']['avg_per_match'] != None else rowData['clean_sheets_avg_per_match'].append('NaN')

        rowData['home_clean_sheets_total'].append(data['clean_sheets']['home']['total']) if data['clean_sheets']['home']['total'] != None else rowData['home_clean_sheets_total'].append('NaN')
        rowData['home_clean_sheets_avg_per_match'].append(data['clean_sheets']['home']['avg_per_match']) if data['clean_sheets']['home']['avg_per_match'] != None else rowData['home_clean_sheets_avg_per_match'].append('NaN')

        rowData['away_clean_sheets_total'].append(data['clean_sheets']['away']['total']) if data['clean_sheets']['away']['total'] != None else rowData['away_clean_sheets_total'].append('NaN')
        rowData['away_clean_sheets_avg_per_match'].append(data['clean_sheets']['away']['avg_per_match']) if data['clean_sheets']['away']['avg_per_match'] != None else rowData['away_clean_sheets_avg_per_match'].append('NaN')


        rowData['goals_scored_range_total_0To15'].append(data['goals_scored_range']['0-15']['total']) if data['goals_scored_range']['0-15']['total'] != None else rowData['goals_scored_range_total_0To15'].append('NaN')
        rowData['goals_scored_range_percentage_total_goals_0To15'].append(data['goals_scored_range']['0-15']['percentage_total_goals']) if data['goals_scored_range']['0-15']['percentage_total_goals'] != None else rowData['goals_scored_range_percentage_total_goals_0To15'].append('NaN')
        
        rowData['goals_scored_range_total_15To30'].append(data['goals_scored_range']['15-30']['total']) if data['goals_scored_range']['15-30']['total'] != None else rowData['goals_scored_range_total_15To30'].append('NaN')
        rowData['goals_scored_range_percentage_total_goals_15To30'].append(data['goals_scored_range']['15-30']['percentage_total_goals']) if data['goals_scored_range']['15-30']['percentage_total_goals'] != None else rowData['goals_scored_range_percentage_total_goals_15To30'].append('NaN')
        
        rowData['goals_scored_range_total_30To45'].append(data['goals_scored_range']['30-45']['total']) if data['goals_scored_range']['30-45']['total'] != None else rowData['goals_scored_range_total_30To45'].append('NaN')
        rowData['goals_scored_range_percentage_total_goals_30To45'].append(data['goals_scored_range']['30-45']['percentage_total_goals']) if data['goals_scored_range']['30-45']['percentage_total_goals'] != None else rowData['goals_scored_range_percentage_total_goals_30To45'].append('NaN')
        
        rowData['goals_scored_range_total_45To60'].append(data['goals_scored_range']['45-60']['total']) if data['goals_scored_range']['45-60']['total'] != None else rowData['goals_scored_range_total_45To60'].append('NaN')
        rowData['goals_scored_range_percentage_total_goals_45To60'].append(data['goals_scored_range']['45-60']['percentage_total_goals']) if data['goals_scored_range']['45-60']['percentage_total_goals'] != None else rowData['goals_scored_range_percentage_total_goals_45To60'].append('NaN')
        
        rowData['goals_scored_range_total_60To75'].append(data['goals_scored_range']['60-75']['total']) if data['goals_scored_range']['60-75']['total'] != None else rowData['goals_scored_range_total_60To75'].append('NaN')
        rowData['goals_scored_range_percentage_total_goals_60To75'].append(data['goals_scored_range']['60-75']['percentage_total_goals']) if data['goals_scored_range']['60-75']['percentage_total_goals'] != None else rowData['goals_scored_range_percentage_total_goals_60To75'].append('NaN')
        
        rowData['goals_scored_range_total_75To90'].append(data['goals_scored_range']['75-90']['total']) if data['goals_scored_range']['75-90']['total'] != None else rowData['goals_scored_range_total_75To90'].append('NaN')
        rowData['goals_scored_range_percentage_total_goals_75To90'].append(data['goals_scored_range']['75-90']['percentage_total_goals']) if data['goals_scored_range']['75-90']['percentage_total_goals'] != None else rowData['goals_scored_range_percentage_total_goals_75To90'].append('NaN')
        
        rowData['goals_scored_range_total_90To120'].append(data['goals_scored_range']['90-120']['total']) if data['goals_scored_range']['90-120']['total'] != None else rowData['goals_scored_range_total_90To120'].append('NaN')
        rowData['goals_scored_range_percentage_total_goals_90To120'].append(data['goals_scored_range']['90-120']['percentage_total_goals']) if data['goals_scored_range']['90-120']['percentage_total_goals'] != None else rowData['goals_scored_range_percentage_total_goals_90To120'].append('NaN')

        
        rowData['goal_line_total_over_0p5'].append(data['goal_line']['over']['0.5']['total']) if data['goal_line']['over']['0.5']['total'] != None else rowData['goal_line_total_over_0p5'].append('NaN')
        rowData['goal_line_percentage_total_matches_over_0p5'].append(data['goal_line']['over']['0.5']['percentage_total_matches']) if data['goal_line']['over']['0.5']['percentage_total_matches'] != None else rowData['goal_line_percentage_total_matches_over_0p5'].append('NaN')
        
        rowData['goal_line_total_over_1p5'].append(data['goal_line']['over']['1.5']['total']) if data['goal_line']['over']['1.5']['total'] != None else rowData['goal_line_total_over_1p5'].append('NaN')
        rowData['goal_line_percentage_total_matches_over_1p5'].append(data['goal_line']['over']['1.5']['percentage_total_matches']) if data['goal_line']['over']['1.5']['percentage_total_matches'] != None else rowData['goal_line_percentage_total_matches_over_1p5'].append('NaN')

        rowData['goal_line_total_over_2p5'].append(data['goal_line']['over']['2.5']['total']) if data['goal_line']['over']['2.5']['total'] != None else rowData['goal_line_total_over_2p5'].append('NaN')
        rowData['goal_line_percentage_total_matches_over_2p5'].append(data['goal_line']['over']['2.5']['percentage_total_matches']) if data['goal_line']['over']['2.5']['percentage_total_matches'] != None else rowData['goal_line_percentage_total_matches_over_2p5'].append('NaN')

        rowData['goal_line_total_over_3p5'].append(data['goal_line']['over']['3.5']['total']) if data['goal_line']['over']['3.5']['total'] != None else rowData['goal_line_total_over_3p5'].append('NaN')
        rowData['goal_line_percentage_total_matches_over_3p5'].append(data['goal_line']['over']['3.5']['percentage_total_matches']) if data['goal_line']['over']['3.5']['percentage_total_matches'] != None else rowData['goal_line_percentage_total_matches_over_3p5'].append('NaN')

        rowData['goal_line_total_over_4p5'].append(data['goal_line']['over']['4.5']['total']) if data['goal_line']['over']['4.5']['total'] != None else rowData['goal_line_total_over_4p5'].append('NaN')
        rowData['goal_line_percentage_total_matches_over_4p5'].append(data['goal_line']['over']['4.5']['percentage_total_matches']) if data['goal_line']['over']['4.5']['percentage_total_matches'] != None else rowData['goal_line_percentage_total_matches_over_4p5'].append('NaN')

        rowData['goal_line_total_over_5p5'].append(data['goal_line']['over']['5.5']['total']) if data['goal_line']['over']['5.5']['total'] != None else rowData['goal_line_total_over_5p5'].append('NaN')
        rowData['goal_line_percentage_total_matches_over_5p5'].append(data['goal_line']['over']['5.5']['percentage_total_matches']) if data['goal_line']['over']['5.5']['percentage_total_matches'] != None else rowData['goal_line_percentage_total_matches_over_5p5'].append('NaN')

        
        rowData['goal_line_total_under_0p5'].append(data['goal_line']['under']['0.5']['total']) if data['goal_line']['under']['0.5']['total'] != None else rowData['goal_line_total_under_0p5'].append('NaN')
        rowData['goal_line_percentage_total_matches_under_0p5'].append(data['goal_line']['under']['0.5']['percentage_total_matches']) if data['goal_line']['under']['0.5']['percentage_total_matches'] != None else rowData['goal_line_percentage_total_matches_under_0p5'].append('NaN')
        
        rowData['goal_line_total_under_1p5'].append(data['goal_line']['under']['1.5']['total']) if data['goal_line']['under']['1.5']['total'] != None else rowData['goal_line_total_under_1p5'].append('NaN')
        rowData['goal_line_percentage_total_matches_under_1p5'].append(data['goal_line']['under']['1.5']['percentage_total_matches']) if data['goal_line']['under']['1.5']['percentage_total_matches'] != None else rowData['goal_line_percentage_total_matches_under_1p5'].append('NaN')

        rowData['goal_line_total_under_2p5'].append(data['goal_line']['under']['2.5']['total']) if data['goal_line']['under']['2.5']['total'] != None else rowData['goal_line_total_under_2p5'].append('NaN')
        rowData['goal_line_percentage_total_matches_under_2p5'].append(data['goal_line']['under']['2.5']['percentage_total_matches']) if data['goal_line']['under']['2.5']['percentage_total_matches'] != None else rowData['goal_line_percentage_total_matches_under_2p5'].append('NaN')

        rowData['goal_line_total_under_3p5'].append(data['goal_line']['under']['3.5']['total']) if data['goal_line']['under']['3.5']['total'] != None else rowData['goal_line_total_under_3p5'].append('NaN')
        rowData['goal_line_percentage_total_matches_under_3p5'].append(data['goal_line']['under']['3.5']['percentage_total_matches']) if data['goal_line']['under']['3.5']['percentage_total_matches'] != None else rowData['goal_line_percentage_total_matches_under_3p5'].append('NaN')

        rowData['goal_line_total_under_4p5'].append(data['goal_line']['under']['4.5']['total']) if data['goal_line']['under']['4.5']['total'] != None else rowData['goal_line_total_under_4p5'].append('NaN')
        rowData['goal_line_percentage_total_matches_under_4p5'].append(data['goal_line']['under']['4.5']['percentage_total_matches']) if data['goal_line']['under']['4.5']['percentage_total_matches'] != None else rowData['goal_line_percentage_total_matches_under_4p5'].append('NaN')

        rowData['goal_line_total_under_5p5'].append(data['goal_line']['under']['5.5']['total']) if data['goal_line']['under']['5.5']['total'] != None else rowData['goal_line_total_under_5p5'].append('NaN')
        rowData['goal_line_percentage_total_matches_under_5p5'].append(data['goal_line']['under']['5.5']['percentage_total_matches']) if data['goal_line']['under']['5.5']['percentage_total_matches'] != None else rowData['goal_line_percentage_total_matches_under_5p5'].append('NaN')


# insert header
row = []
for header, data in rowData.items():
    row.append(header)
csv_writer.writerow(row)

# insert data
for i in range(len(rowData['season_id'])):
      row = []
      for header, data in rowData.items():
            row.append(rowData[header][i])
      csv_writer.writerow(row)
      
print('done')


