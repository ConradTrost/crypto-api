import requests
import json
from constants import API_KEY

class Coin():
    def __init__(self, ticker, market):
        self.base_url = 'https://www.alphavantage.co/query'
        self.key = API_KEY
        self.market = market
        self.ticker = ticker

    def get_data(self, fileName, url):
        response = requests.get(url)
        self.write_file(fileName, response.json())

    def url(self, endpoint):
        return f'{self.base_url}?{endpoint}&apikey={self.key}'

    def write_file(self, fileName, data):
        f = open(f'{fileName}/{self.ticker}to{self.market}.json', "w")
        f.write(json.dumps(data))
        f.close()

    def find_data(self, fileName, url):
        while True:
            try:
                f = open(f'{fileName}/{self.ticker}to{self.market}.json', 'r')
                return json.load(f)
            except IOError: 
                self.get_data(fileName, url)

    # Intervals can be 5, 10, 15, 30, 60 for intraday
    def intraday(self, interval):
        endpoint = f'function=CRYPTO_INTRADAY&symbol={self.ticker}&market={self.market}&interval={interval}min&outputsize=full'
        self.find_data(f'intraday/{interval}', self.url(endpoint))


    def currentExchangeRate(self):
        endpoint = f'function=CURRENCY_EXCHANGE_RATE&from_currency={self.ticker}&to_currency={self.market}'
        print(self.url(endpoint))

    def daily(self):
        endpoint = f'function=DIGITAL_CURRENCY_DAILY&symbol={self.ticker}'
        self.find_data(f'daily', self.url(endpoint))


btc = Coin('BTC', 'USD')

print('')
# btc.intraday(60)
# btc.currentExchangeRate()
# print('')
btc.daily()