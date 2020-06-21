from bs4 import BeautifulSoup
import requests 
import webbrowser
import operator

class coinData:
    no = 0
    name = ''
    tag = ''
    price = 0.0
    change1h = 0.0
    change24h = 0.0
    change7d = 0.0
    link = ''
    roi = ''
    marketcap = ''

if __name__ == "__main__":
    #WEBSITE
    site = "https://coinmarketcap.com/"
    addon = 'all/views/all/'
    page = requests.get(site+addon)

    soup = BeautifulSoup(page.content, 'html.parser')
    #BODY CONTAINS ALL THE DATA IN HTML.
    body = soup.find('tbody')
    row = body.find_all('tr', {'class': 'cmc-table-row'})

    #STORE ALL THE CRUPTO DATA IN DATA LIST
    data = []
    #SPESIFIC COINS 
    wallet = ['BTC', 'GNT', 'ETH', 'ADA', 'CVC', 'OMG', 'ZEC', 'XRP', 'LTC', 'LSK', 'NEO', 'XMR', 'QTUM'] 
    watchlist = []

    for coin in row:
        item = coinData()
        no = coin.find('td', {'class':"cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__rank"}).find('div').text
        nameLink = coin.find('td', {'class':"cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name"}).find('div').find('a')
        name = nameLink.text
        tag = coin.find('td', {'class': "cmc-table__cell cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__symbol"}).text
        link = nameLink.get('href')
        price = coin.find('td', {'class':"cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price"}).find('a').text
        marketcap = coin.find('td', {'class': "cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap"}).text
        change1h = coin.find('td', {'class':"cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-1-h"}).find('div').text
        change24h = coin.find('td', {'class':"cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-24-h"}).find('div').text
        change7d = coin.find('td', {'class':"cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-7-d"}).find('div').text
        
        item.no = int(no)
        item.name = str(name)
        item.price = float(price[1:].replace(',','')) # removing comma and dollar sign
        item.marketcap = marketcap.replace(',',' ')
        item.change1h = float(change1h.replace('%', ''))
        item.change24h= float(change24h.replace('%', ''))
        item.change7d = float(change7d.replace('%', ''))
        item.link = site + link[1:]
        data.append(item)

        #Add spesific coind to seprate list
        if tag in wallet:
            watchlist.append(item)
            #print(tag)
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

    fmt = '{:<3} {:<20} {:<10} {:<10} {:<15} {:<15}'
    for section in bestPerforming:
        heading = fmt.format('NO','COIN', 'PRICE', 'CHANGE', 'MARKETCAP', 'ROI')
        stripes = '-------------------------------------------------------------------------------'
        print(heading, ' ', heading)
        print(stripes, stripes)
        
        lhs = section[0]
        rhs = section[1]   
            
        for i in range(10):
            lhs_name = lhs[i].name
            rhs_name = rhs[i].name
            if(len(lhs_name)>15):
                lhs_name = lhs[i].tag
            if(len(rhs_name)>15):
                lhs_name = rhs[i].tag

            if(section == bestPerforming[0]):
                displayL = fmt.format(lhs[i].no, lhs_name, lhs[i].price, str(lhs[i].change1h)+'%', lhs[i].marketcap, lhs[i].roi)
                displayR = fmt.format(rhs[i].no, rhs_name, rhs[i].price, rhs[i].change1h, rhs[i].marketcap, rhs[i].roi)
          
            if(section == bestPerforming[1]):
                displayL = fmt.format(lhs[i].no, lhs_name, lhs[i].price, lhs[i].change24h, lhs[i].marketcap, lhs[i].roi)
                displayR = fmt.format(rhs[i].no, rhs_name, rhs[i].price, rhs[i].change24h, rhs[i].marketcap, rhs[i].roi)
                
            if(section == bestPerforming[2]):
                displayL = fmt.format(lhs[i].no, lhs_name, lhs[i].price, lhs[i].change7d, lhs[i].marketcap, lhs[i].roi)
                displayR = fmt.format(rhs[i].no, rhs_name, rhs[i].price, rhs[i].change7d, rhs[i].marketcap, rhs[i].roi)
            print(displayL,'|', displayR,'|')
        print(stripes, stripes)
    
    watchlist = sorted(watchlist, key=operator.attrgetter('no'))

    print(stripes, stripes)
    print()
    print('********************WATCHLIST********************')
    print(fmt.format('NO','COIN', 'PRICE', 'CHANGE', 'MARKETCAP', 'ROI'))
    print(stripes, stripes)

    for coin in watchlist:
        print(fmt.format(coin.no, coin.name, coin.price, str(coin.change7d)+' %', coin.marketcap, coin.roi))  
