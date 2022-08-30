import requests

x = requests.get('https://api.spacexdata.com/v3/launches')

print(x.text)
