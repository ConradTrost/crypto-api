import requests
from constants import API_KEY

class Coin():
    def __init__(self, ticker, market):
        self.base_url = 'https://www.alphavantage.co/query'
        self.key = API_KEY
        self.market = market
        self.ticker = ticker

    def send_req(self, url):
        response = requests.get(url)
        print(response.json())

    def print_url(self, url):
        print(f'\n{url}\n')

    def build_url(self, endpoint):
        url = f'{self.base_url}?{endpoint}&apikey={self.key}'
        self.print_url(url)

    # Intervals can be 5, 10, 15, 30, 60 for intraday
    def intraday(self, interval):
        endpoint = f'function=CRYPTO_INTRADAY&symbol={self.ticker}&market={self.market}&interval={interval}min'
        self.build_url(endpoint)

    def currentExchangeRate(self):
        endpoint = f'function=CURRENCY_EXCHANGE_RATE&from_currency={self.ticker}&to_currency={self.market}'
        self.build_url(endpoint)


btc = Coin('BTC', 'USD')

print('')
btc.intraday(60)
btc.currentExchangeRate()
print('')