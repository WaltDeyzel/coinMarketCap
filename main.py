from bs4 import BeautifulSoup
import requests 
import webbrowser
import operator

class coinData:
    no = 0
    name = ''
    price = 0.0
    change1h = 0.0
    change24h = 0.0
    change7d = 0.0
    link = ''
    roi = ''
    marketcap = ''

if __name__ == "__main__":
    site = "https://coinmarketcap.com/"
    addon = 'all/views/all/'
    page = requests.get(site+addon)

    soup = BeautifulSoup(page.content, 'html.parser')
    body = soup.find('tbody')
    row = body.find_all('tr', {'class': 'cmc-table-row'})

    data = []

    for coin in row:
        item = coinData()
        no = coin.find('td', {'class':"cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__rank"}).find('div').text
        nameLink = coin.find('td', {'class':"cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name"}).find('div').find('a')
        name = nameLink.text
        link = nameLink.get('href')
        price = coin.find('td', {'class':"cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price"}).find('a').text
        marketcap = coin.find('td', {'class': "cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap"}).text
        change1h = coin.find('td', {'class':"cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-1-h"}).find('div').text
        change24h = coin.find('td', {'class':"cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-24-h"}).find('div').text
        change7d = coin.find('td', {'class':"cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-7-d"}).find('div').text
        
        item.no = int(no)
        item.name = str(name)
        item.price = float(price[1:].replace(',','')) # removing comma and dollar sign
        item.marketcap = marketcap
        item.change1h = float(change1h.replace('%', ''))
        item.change24h= float(change24h.replace('%', ''))
        item.change7d = float(change7d.replace('%', ''))
        item.link = site + link[1:]
        data.append(item)

    # for item in data:
    #     print(item.roi)
    #     if(item.change1h > 30.0):
    #         print(item.name)
    #         webbrowser.open(item.link)

    #SORTED DATA ACCORDING TO...
    hourly = sorted(data, key=operator.attrgetter('change1h'))
    daily = sorted(data, key=operator.attrgetter('change24h'))
    weekly = sorted(data, key=operator.attrgetter('change7d'))

    hourly_worst = hourly[:11]
    hourly_best = hourly[-10:]
    daily_worst = daily[:11]
    daily_best = daily[-10:]
    weekly_worst = weekly[:11]
    weekly_best = weekly[-10:]
 
    bestPerforming = [hourly_best, hourly_worst, daily_best, daily_worst, weekly_best, weekly_worst]

    for interval in bestPerforming:
        fmt = '{:<3} {:<20} {:<10} {:<10} {:<15} {:<15}'
        print(fmt.format('NO','COIN', 'PRICE', 'CHANGE', 'MARKETCAP', 'ROI'))
        print('-------------------------------------------------------------------')
        for coin in interval:
            # #coin = interval[i]
            # page2 = requests.get(coin.link)
            # soup2 = BeautifulSoup(page2.content, 'html.parser')
            # #print(page2)
            # body2 = soup2.find('tbody', {'class': "cmc-details-panel-about__table"})
            # try:
            #     marketcap = body2.find_all('td')
            #     coin.marketcap = (marketcap[3].text).replace(',',' ').replace('USD','')
            # except:
            #     pass
            # try:
            #     coin.roi = (body2.find('span', {'class': "cmc--change-positive"}).text).replace('USD','')
            # except:
            #     pass
             
            
            if(bestPerforming[0] == interval or bestPerforming[1] == interval):
                
                print(fmt.format(coin.no, coin.name, coin.price, coin.change1h, coin.marketcap, coin.roi))
            if(bestPerforming[2] == interval or bestPerforming[3] == interval):
                
                print(fmt.format(coin.no, coin.name, coin.price, coin.change24h, coin.marketcap, coin.roi))
            if(bestPerforming[4] == interval or bestPerforming[5] == interval):

                print(fmt.format(coin.no, coin.name, coin.price, coin.change7d, coin.marketcap, coin.roi))
        print()