from bs4 import BeautifulSoup
import requests 
import webbrowser
import operator
from constants import htmlStrings as html
from coinData import coinData
from display import DisplayData

if __name__ == "__main__":
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
    watchlist = []

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
            watchlist.append(item)
            #webbrowser.open(item.link)

    #SORTED DATA ACCORDING TO...
    hourly = sorted(data, key=operator.attrgetter('change1h'))
    daily = sorted(data, key=operator.attrgetter('change24h'))
    weekly = sorted(data, key=operator.attrgetter('change7d'))

    #DISPLAY TOP 10
    hourly_worst = hourly[:11]
    hourly_best = hourly[-10:]
    daily_worst = daily[:11]
    daily_best = daily[-10:]
    weekly_worst = weekly[:11]
    weekly_best = weekly[-10:]

    hourly_best.reverse()
    weekly_best.reverse()
    daily_best.reverse()
    #sections hourly, daily, weekly
    bestPerforming = [[hourly_best, hourly_worst], [daily_best, daily_worst], [weekly_best, weekly_worst]]

    DisplayData.displayData(DisplayData, bestPerforming, wallet)
    DisplayData.displayWatchlist(DisplayData, watchlist)
    DisplayData.displayWorstPerforming(DisplayData, weekly)
    
    