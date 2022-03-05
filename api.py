import requests
url = 'https://data.messari.io/api/v1/assets/btc/metrics'
response = requests.request('GET', url)
print(response.text)