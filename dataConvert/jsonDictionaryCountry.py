import json
import csv
import os
import glob
import requests
from urllib import request, parse
import dataDictionary

file_path = 'C:\\Users\\kenpe\\PycharmProjects\\soccersApi\\data\\countrys.json'
with open(file_path) as json_file:
    data = json.load(json_file)
        
data = data['data']

dic = {}

for country in data:
    dic[int(country['id'])] = {}
    dic[int(country['id'])]['name'] = country['name']
    dic[int(country['id'])]['continent'] = country['continent']
    dic[int(country['id'])]['sub_region'] = country['sub_region']
    dic[int(country['id'])]['code'] = country['code']

# print(dic)
print('done')
