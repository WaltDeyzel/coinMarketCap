class Trader:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.wallet = {}
    
    def showTrder(self):
        for coin in self.wallet:
            print(coin, self.wallet[coin])
        print('Budget', self.budget)
        print('Roi', 100*self.budget/10000)
    
    def buy(self, coin, amount):
        if(amount*coin.price < self.budget):
            if(coin.name in self.wallet):
                newAmount = self.wallet[coin.name]+amount
                self.wallet.update({coin.name: newAmount})
            else:
                self.wallet[coin.name] = amount
            self.budget = self.budget-amount*coin.price
        else:
            pass

    def sell(self, coin, amount):
        if(amount <= self.wallet[coin.name]):
            self.budget = self.budget + amount*coin.price
            newAmount = self.wallet[coin.name]-amount
            self.wallet.update({coin.name: newAmount})
        else:
            pass



class Crypto:
    def __init__(self, name, price):
        self.name = name
        self.price = price

if __name__ == "__main__":
    person = Trader('W', 10000)
    coin0 = Crypto('Bitcoin', 1000)
    coin1 = Crypto('Golem', 1)
    person.buy(coin0, 5)
    person.buy(coin1, 100)
    coin0 = Crypto('Bitcoin', 80)
    coin1 = Crypto('Golem', 3)
    person.sell(coin0, 1)
    person.sell(coin1, 100)

    person.showTrder()


    