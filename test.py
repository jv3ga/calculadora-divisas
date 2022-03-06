import requests

asset = 'btc'
url = 'https://data.messari.io/api/v1/assets/{}/metrics'.format(asset)
data = requests.request('GET', url)
print(data.ok)