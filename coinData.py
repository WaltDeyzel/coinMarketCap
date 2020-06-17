class coinData:
    def data(self, no, name, price, c1h, c24h, c7d):
        self.name = name
        self.no = no
        self.price = price
        self.c1h = c1h
        self.c24h = c24h
        self.c7d = c7d
        print(self.name)