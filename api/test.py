import api.config as cf
import requests

config = cf.config()


url = config.endpoint + 'continents/?' + 'user={}&token={}'.format(config.user, config.token)\
      + '&t={}'.format('list')

payload = {}
headers = {}
response = requests.request("GET", url, headers = headers, data = payload)

print(url)
print(response.text.encode('utf8'))
file_name = f"team_statistics_test_id.json"
# print(url)

f = open(file_name, "w+")
f.write(response.text)
f.close()
