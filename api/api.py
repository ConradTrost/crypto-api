import os
import json
import requests  
from constants import API_KEY

class Coin():
    def __init__(self, ticker, market):
        self.base_url = 'https://www.alphavantage.co/query'
        self.key = API_KEY
        self.market = market
        self.ticker = ticker

    def get_data(self, file_name, url):
        print(f'\nRequesting data from {url}..')
        response = requests.get(url)
        self.write_file(file_name, response.json())

    def url(self, endpoint):
        return f'{self.base_url}?{endpoint}&apikey={self.key}'

    def write_file(self, file_name, data):
        f = open(file_name, "w")
        f.write(json.dumps(data))
        f.close()

    def find_data(self, directory, url):
        file_name = f'{directory}/{self.ticker}.json'

        while True:
            try:
                f = open(file_name, 'r')
                print(f'\nReading data from current {file_name}...') 
                return json.load(f)
            except IOError: 
                try:
                    os.mkdir(directory)
                except OSError as error: 
                    print(error)  
                self.get_data(file_name, url)

    # Intervals can be 5, 10, 15, 30, 60 for intraday
    def intraday(self, interval):
        endpoint = f'function=CRYPTO_INTRADAY&symbol={self.ticker}&market={self.market}&interval={interval}min&outputsize=full'
        self.find_data(f'_data/intraday/{interval}/{self.market}', self.url(endpoint))


    def current_exchange_rate(self):
        endpoint = f'function=CURRENCY_EXCHANGE_RATE&from_currency={self.ticker}&to_currency={self.market}'
        print(self.url(endpoint))

    def daily(self):
        endpoint = f'function=DIGITAL_CURRENCY_DAILY&symbol={self.ticker}&market={self.market}'
        self.find_data(f'_data/daily/{self.market}', self.url(endpoint))


btc = Coin('BTC', 'USD')
eth = Coin('ETH', 'USD')

# btc.intraday(60)
# btc.daily()
# eth.daily()

# https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=ETH&market=USD&apikey=""""&datatype=csv