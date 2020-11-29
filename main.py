from bs4 import BeautifulSoup
import requests 
import webbrowser
import operator
import sys
from constants import htmlStrings as html
from coinData import coinData
from display import DisplayData

def watchlistFilter(data):
    watchlist = []
    for coin in data:
        if(coin.star == '*'):
            watchlist.append(coin)
    return watchlist

def show(data):
    #SORTED DATA ACCORDING TO...
    hourly = sorted(data, key=operator.attrgetter('change1h'))
    daily = sorted(data, key=operator.attrgetter('change24h'))
    weekly = sorted(data, key=operator.attrgetter('change7d'))
    watchlist = watchlistFilter(data)

    DisplayData.displayData(DisplayData, hourly, daily, weekly)
    DisplayData.displayWatchlist(DisplayData, watchlist)
    DisplayData.displayWorstPerforming(DisplayData, weekly)

def getData():
    #WEBSITE
    site = "https://coinmarketcap.com/"
    addon = 'all/views/all/'
    site = site + addon
    page = requests.get(site)

    soup = BeautifulSoup(page.content, 'html.parser')
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
        link  = nameLink.get('href')
        price = coin.find('td', {'class': html.price}).find('a').text
        marketcap = coin.find('td', {'class': html.marketcap}).text
        change1h  = coin.find('td', {'class': html.change1h}).find('div').text
        change24h = coin.find('td', {'class': html.change24h}).find('div').text
        change7d  = coin.find('td', {'class':html.change7d}).find('div').text
        
        item.no = int(no)
        item.name = str(name)
        item.tag = tag
        item.price = float(price[1:].replace(',','')) # removing comma and dollar sign
        item.marketcap = marketcap.replace(',',' ')
        item.change1h = float(change1h.replace('%', ''))
        item.change24h= float(change24h.replace('%', ''))
        change7d = change7d.replace(',', '')
        item.change7d = float(change7d.replace('%', ''))
        item.link = site + link[1:]
        data.append(item)

        #Add spesific coind to seprate list
        if tag in wallet:
            item.star = '*'
            #webbrowser.open(item.link)
    return data

if __name__ == "__main__":
    data = getData()
    if(len(sys.argv) > 1):
        try:
            site = "https://coinmarketcap.com/currencies/" + sys.argv[1]
            webbrowser.open(site)
        except:
            print('FAIL')
    else:
        show(data)
    