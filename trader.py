from api import CryptoData
from time import sleep
import random
class Trader:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.wallet = []
        self.mode = True
    
    def showTraderInfo(self):
        fmt = '{:<22} {:<13} {:<10}'
        for crypto in self.wallet:
            print(fmt.format(crypto.name, round(crypto.price,2), round(crypto.amount,2)))
        print('BUDGET',self.budget)
        print()
    
    def buy(self, coin, cost):
        if(cost <= self.budget):
            self.budget -= cost
            index = Trader.findInWallet(self, coin)
            amount = cost/coin.price #amount of coins
            if( index == -1):
                crypto = Crypto(coin.name, cost, amount)
                self.wallet.append(crypto)
            else:
                self.wallet[index].price += cost
                self.wallet[index].amount += amount
        else:
            print('Not enough money')
    
    def sell(self, coin):
        index = Trader.findInWallet(self, coin)
        if(index != -1):
            value = self.wallet[index].amount*coin.price
            self.budget += value
            self.wallet.remove(self.wallet[index])
            
        
    def findInWallet(self, coin):
        for crypto in self.wallet:
            if(crypto.name == coin.name):
                return(self.wallet.index(crypto))
        return(-1)

    def stategy1(self, data, hourly):
        if(self.budget == 10000):
            self.fillWallet(hourly, 10)
            self.showTraderInfo()
            self.mode = False
        else:
            if(self.mode == True and self.budget>=1000):
                n = 10-len(self.wallet)
                for i in range(n):
                    ran = random.randint(0, 100)
                    self.buy(data[ran], 1000)
                print('BUY')
                self.mode = False
            else:
                for thing in p.wallet:
                    for coin in data:
                        if(thing.name == coin.name):
                            change = 100*(coin.price-thing.pricePerCoin())/thing.pricePerCoin()
                            if(change > 5.0):
                                self.sell(coin)
                                self.mode = True
                            break
                print('SELL')
            self.showTraderInfo()

    #FILL WALLET WITH N COINS
    def fillWallet(self, hourly, n):
        for a in range(n):
            coin = hourly[a]
            if(coin.price < 0.0001):
                coin = hourly[a+random.randint(11,100)]
            self.buy(coin, 1000)
                

class Crypto:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
    
    def pricePerCoin(self):
        return(self.price/self.amount)

if __name__ == "__main__":
    p = Trader('w', 10000)

    for i in range(100):
        data = CryptoData.getData(CryptoData)
        hourly = CryptoData.filter(CryptoData, data, 'change1h')
        
        p.stategy1(data, hourly)

        sleep(600) # 10 min 12 times = 2 hours