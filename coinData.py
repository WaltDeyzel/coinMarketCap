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

    def display(self):
        
        print(self.no, self.name, '$'+str(self.price))
        print(self.marketcap)
        print(self.change1h, self.change24h, self.change7d)
