from bs4 import BeautifulSoup
import requests 

class coinData:
    no = ''
    name = ''
    price = ''
    change1h = ''
    change24h = ''
    change7d = ''
    link = ''


if __name__ == "__main__":
    
    page = requests.get("https://coinmarketcap.com/all/views/all/")

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
        item.no = no
        item.name = name
        item.price = price
        item.change1h = change1h
        item.change24h = change24h
        item.change7d = change7d
        item.link = link
        data.append(item)

    for item in data:
        print(item.name)