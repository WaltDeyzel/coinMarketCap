from bs4 import BeautifulSoup
import requests
import operator
from constants import Constants as html
from display import DisplayData
from coinData import coinData

class CryptoData:
    def getData(self):
        #WEBSITE
        site = "https://coinmarketcap.com/"
        addon = 'all/views/all/'
        page = site + addon
        webpage = requests.get(page)

        soup = BeautifulSoup(webpage.content, 'html.parser')
        #BODY CONTAINS ALL THE DATA IN HTML.
        body = soup.find('tbody')
        row = body.find_all('tr', {'class': html.table})

        #STORE ALL THE CRUPTO DATA IN DATA LIST
        data = []
        #SPESIFIC COINS 
        wallet = ['BTC', 'GNT', 'ETH', 'ADA', 'CVC', 'OMG', 'ZEC', 'XRP', 'LTC', 'LSK', 'NEO', 'XMR', 'QTUM'] 

        for coin in row:
            item = coinData()
            no   = coin.find('td', {'class': html.number}).find('div').text
            nameLink = coin.find('td', {'class': html.link}).find('div').find('a')
            name  = nameLink.text
            tag   = coin.find('td', {'class': html.tag}).text
            #link  = nameLink.get('href')
            price = coin.find('td', {'class': html.price}).find('a').text
            marketcap = coin.find('td', {'class': html.marketcap}).text
            change1h  = coin.find('td', {'class': html.change1h}).find('div').text
            change24h = coin.find('td', {'class': html.change24h}).find('div').text
            change7d  = coin.find('td', {'class':html.change7d}).find('div').text
            
            item.no = int(no)
            item.name = str(name).lower()
            item.tag = tag
            item.price = float(price[1:].replace(',','')) # removing comma and dollar sign
            item.marketcap = marketcap.replace(',',' ')
            item.change1h = float(change1h.replace('%', ''))
            item.change24h= float(change24h.replace('%', ''))
            change7d = change7d.replace(',', '')
            item.change7d = float(change7d.replace('%', ''))
            item.link = site + "currencies/" + name.lower() +'/'                       #site + link[1:]
            data.append(item)

            #Add spesific coins to seprate list
            if tag in wallet:
                item.star = '*'
                #webbrowser.open(item.link)
        return data

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