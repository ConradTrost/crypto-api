import requests
from constants import API_KEY

BASE_URL = 'https://api.nomics.com/v1'

EX_ENDPT = '&ids=BTC,ETH,XRP&interval=1d,30d&convert=EUR&platform-currency=ETH&per-page=100&page=1'

REQ_URL = f'{BASE_URL}/currencies/ticker?key={API_KEY}&ids=BTC&interval=1d'

print(REQ_URL)

response = requests.get(REQ_URL)
print(response.json())