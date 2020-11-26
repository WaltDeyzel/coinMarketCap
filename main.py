from bs4 import BeautifulSoup
import requests 
import webbrowser
import operator
from constants import htmlStrings as html

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

    fmt = '{:<2} {:<3} {:<20} {:<10} {:<10} {:<15} {:<15}'
    for section in bestPerforming:
        print()
        heading = fmt.format(' ','NO','COIN', 'PRICE', 'CHANGE', 'MARKETCAP', 'ROI')
        stripes = '----------------------------------------------------------------------------------'
        print(heading, ' ', heading)
        print(stripes, stripes)
        
        lhs = section[0] # DATA DISPLAYED ON THE LEFT
        rhs = section[1] # DATA DISPLAYED ON THE RIGHT

        for i in range(10):
            #MARK DATA THAT IS ALSO IN THE WATCHLIST WITH A *
            starL = " "
            starR = " "
            changeL = lhs[i].change24h #DEFAULT 24H
            changeR = rhs[i].change24h #DEFAULT 24H

            lhs_name = lhs[i].name
            rhs_name = rhs[i].name
            if(len(lhs_name)>15):
                lhs_name = lhs[i].tag
            if(len(rhs_name)>15):
                lhs_name = rhs[i].tag

            if(section == bestPerforming[0]):
                changeL = lhs[i].change1h
                changeR = rhs[i].change1h
          
            #DO NOT NEED TO CHECH FOR SECTION == BESTPERFORMING[1] BECAUSE IT IS THE DEFAULT
                
            if(section == bestPerforming[2]):
                changeL = lhs[i].change7d
                changeR = rhs[i].change7d
            
            if lhs[i].tag in wallet:
                starL = "*"
                
            if rhs[i].tag in wallet:
                starR = "*"
           
            displayL = fmt.format(starL, lhs[i].no, lhs_name, lhs[i].price, changeL, lhs[i].marketcap, lhs[i].roi)
            displayR = fmt.format(starR, rhs[i].no, rhs_name, rhs[i].price, changeR, rhs[i].marketcap, rhs[i].roi)
            print(displayL,'|', displayR,'|')
        print(stripes, stripes)
    
    watchlist = sorted(watchlist, key=operator.attrgetter('change7d'))
    watchlist.reverse()
    
    print(stripes, stripes)
    print()
    print('___________________________________WATCHLIST___________________________________')
    print(fmt.format('#','NO','COIN', 'PRICE', 'CHANGE', 'MARKETCAP', 'ROI'))
    print(stripes, stripes)

    for coin in watchlist:
        print(fmt.format(' ',coin.no, coin.name, coin.price, str(coin.change7d)+' %', str(coin.change24h)+' %', coin.marketcap, coin.roi)) 
    
    print()
    pairs = []
    n = 30
    for coin in weekly:

        if(coin.no <= n):
            if(coin.change7d < 0):
                pairs.append(coin)

    print('Worst performing coin past week in top' , n)
    for coin in pairs:
        print(fmt.format(' ',coin.no, coin.name, coin.price, str(coin.change7d)+' %', coin.marketcap, coin.roi)) 
