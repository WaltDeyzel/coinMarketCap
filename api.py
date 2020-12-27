from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from coinData import coinData
import requests
import operator
from display import DisplayData
from coinData import coinData

class CryptoData:
  def getData(self):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'200',
      'convert':'ZAR'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': '96e23a7b-6435-46a1-9588-ae3dd3a1b753',
    }

    session = Session()
    session.headers.update(headers)

    #STORE ALL THE CRUPTO DATA IN DATA LIST
    data = []
    #SPESIFIC COINS 
    wallet = ['BTC', 'GNT', 'ETH', 'ADA', 'CVC', 'OMG', 'ZEC', 'XRP', 'LTC', 'LSK', 'NEO', 'XMR', 'QTUM'] 

    try:
      response = session.get(url, params=parameters)
      data1 = json.loads(response.text)
      for coin in data1['data']:
        item = coinData()

        item.no   = coin['cmc_rank']
        item.name  = coin['name'].lower()
        item.tag   = coin['symbol']
        item.price = round(coin['quote']['ZAR']['price'],2)
        item.marketcap = round(coin['quote']['ZAR']['market_cap'])
        item.change1h  = round(coin['quote']['ZAR']['percent_change_1h'],2)
        item.change24h = round(coin['quote']['ZAR']['percent_change_24h'],2)
        item.change7d  = round(coin['quote']['ZAR']['percent_change_7d'],2)

        item.id = coin['id']
        item.num_market_pairs = coin['num_market_pairs']
        item.date_added = coin['date_added']
        item.circulating_supply = coin['circulating_supply']
        item.max_supply = coin['max_supply']
        item.total_supply = coin['total_supply']
        item.volume_24h = coin['quote']['ZAR']['volume_24h']
        
        data.append(item)

        #Add spesific coins to seprate list
        if item.tag in wallet:
            item.star = '*'

      return data
        
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)

  def show(self, data):
          #SORTED DATA ACCORDING TO...
          hourly = sorted(data, key=operator.attrgetter('change1h'))
          daily = sorted(data, key=operator.attrgetter('change24h'))
          weekly = sorted(data, key=operator.attrgetter('change7d'))

          watchlist = self.getWatchlist(self.getWatchlist, data)
          worst = self.getWorstPerforming(self.getWorstPerforming, weekly, 30)

          DisplayData.displayData(DisplayData, hourly, daily, weekly)
          DisplayData.displayWatchlist(DisplayData, watchlist)
          DisplayData.displayWorstPerforming(DisplayData, worst)
      
  def findCoin(self, data, name):
      for coin in data:
          if coin.name == name:
              return coin

  def getWatchlist(self, data):
      watchlist = []
      for coin in data:
          if(coin.star == '*'):
              watchlist.append(coin)
      watchlist = sorted(watchlist, key=operator.attrgetter('change7d'))
      watchlist.reverse()
      return watchlist

  def getWorstPerforming(self, data, n):
      worst = []
      for coin in data:
          if(coin.no <= n):
              if(coin.change7d < 0):
                  worst.append(coin)
      return worst