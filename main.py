from bs4 import BeautifulSoup
import requests 
import webbrowser

class coinData:
    no = 0
    name = ''
    price = 0.0
    change1h = 0.0
    change24h = 0.0
    change7d = 0.0
    link = ''


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
        data.append(item)

    for item in data:
        
        if(item.name == 'Bitcoin'):
            print(item.link)
            webbrowser.open(item.link)