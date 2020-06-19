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
    c = 0
    for coin in row:
        item = coinData()
        no = coin.find('td', {'class':"cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__rank"}).find('div').text
        nameLink = coin.find('td', {'class':"cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name"}).find('div').find('a')
        name = nameLink.text
        link = nameLink.get('href')
        price = coin.find('td', {'class':"cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price"}).find('a').text
        change1h = coin.find('td', {'class':"cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-1-h"}).find('div').text
        change24h = coin.find('td', {'class':"cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-24-h"}).find('div').text
        change7d = coin.find('td', {'class':"cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-7-d"}).find('div').text
        item.no = int(no)
        item.name = str(name)
        item.price = float(price[1:].replace(',','')) # removing comma and dollar sign
        item.change1h = float(change1h.replace('%', ''))
        item.change24h= float(change24h.replace('%', ''))
        item.change7d = float(change7d.replace('%', ''))
        item.link = site + link[1:]
        if(c>0):
            page2 = requests.get(item.link)
            soup2 = BeautifulSoup(page2.content, 'html.parser')
            ##print(page2)
            body2 = soup2.find('tbody', {'class': "cmc-details-panel-about__table"})
            roi = body2.find('span', {'class': "cmc--change-positive"}).text
            #change positive somehow... very slow method. Move to class....
            item.roi = (roi.replace('%','')).replace(',','')
            c -=1
        data.append(item)

    # for item in data:
    #     print(item.roi)
    #     if(item.change1h > 30.0):
    #         print(item.name)
    #         webbrowser.open(item.link)
    hourly = sorted(data, key=operator.attrgetter('change1h'))
    daily = sorted(data, key=operator.attrgetter('change24h'))
    weekly = sorted(data, key=operator.attrgetter('change7d'))
    bestPerforming = [hourly, daily, weekly]

    for interval in bestPerforming:
        
        for i in range(10):
            coin = interval[i]
            page2 = requests.get(coin.link)
            soup2 = BeautifulSoup(page2.content, 'html.parser')
            #print(page2)
            body2 = soup2.find('tbody', {'class': "cmc-details-panel-about__table"})
            try:
                marketcap = body2.find_all('td')
                coin.marketcap = (marketcap[3].text).replace(',',' ')
            except:
                pass
            
            #print(marketcap[2])
        
            
            try:
                coin.roi = body2.find('span', {'class': "cmc--change-positive"}).text
            except:
                pass
             
            fmt = '{:<20} {:<10} {:<10} {:<10} {:<15}'
            if(bestPerforming[0] == interval):
                
                print(fmt.format(coin.name, coin.price, coin.change1h, coin.roi, coin.marketcap))
            if(bestPerforming[1] == interval):
              
                print(fmt.format(coin.name, coin.price, coin.change24h, coin.roi, coin.marketcap))
            if(bestPerforming[2] == interval):
                
                print(fmt.format(coin.name, coin.price, coin.change7d, coin.roi, coin.marketcap))
        print()


