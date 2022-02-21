import requests
from constants import API_KEY

url = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=ETH&market=USD&apikey={API_KEY}&datatype=csv&outputsize=full'

req = requests.get(url)
url_content = req.content
csv_file = open('data/btc_price_history.csv', 'wb')

csv_file.write(url_content)
csv_file.close()