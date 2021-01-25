import json
import csv
import os
import glob
import requests
from urllib import request, parse
import numpy as np
import dataDictionary as dic

path = os.getcwd() + '\\data\\leagues'

file_paths = [f for f in glob.glob(path + "**/*.json", recursive=True)]

data_file = open(os.getcwd() + '\\csvData\\leagues\\leagues.csv', 'w', newline='')
csv_writer = csv.writer(data_file)

hearders = ['id', 'continent', 'country', 'name', 'seasons']

csv_writer.writerow(hearders)

is_headers = 0
for file_path in file_paths:
    with open(file_path) as json_file:
    	data = json.load(json_file)
    data = data['data']
    
    row = []
    for header in hearders:
        if header == 'continent': 
            row.append(data[header]['name'])
        elif header == 'country':
            row.append(data[header]['name'])
        elif header == 'id':
            row.append(data[header])
        elif header == 'name':
            row.append(dic.leaguesDic.get(int(data['id'])))
        elif header == 'seasons':
            seasons = ''
            for season in data[header]:
                if seasons != '':
                    seasons += ', '

                if season['name'] == '20/21':
                    seasons += '2020'
                elif season['name'] == '19/20':
                    seasons += '2019'
                elif season['name'] == '18/19':
                    seasons += '2020'
                else:
                    seasons += season['name']
            row.append(seasons)
        else:
            row.append(data[header]) if data[header] is not None else row.append('NaN')

    # # save img
    # if 'img' in data:
    #     response = requests.request("GET", data['img'], headers = {}, data = {})

    #     img_url = parse.urlparse(data['img'])
    #     filename, file_ext = os.path.splitext(os.path.basename(img_url.path))

    #     save_img_path = os.getcwd() + "\\data\\img\\leagues\\"
    #     img_name = data['country']['name'] + '_' + data['name'] + '_logo' + file_ext

    #     if not os.path.exists(save_img_path + img_name):
    #         f = open(save_img_path + img_name, 'wb')
    #         f.write(response.content)
    #         f.close()

    csv_writer.writerow(row)

print('done')
