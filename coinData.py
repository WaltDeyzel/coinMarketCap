class coinData:
    no = 0
    star = ' '
    name = ''
    tag = ''
    price = 0.0
    change1h = 0.0
    change24h = 0.0
    change7d = 0.0
    link = ''
    roi = ''
    marketcap = ''
    fmt = '{:<2} {:<3} {:<20} {:<10} {:<10} {:<15} {:<15}'

    def displayWeekly(self): #default weekly
        return(self.fmt.format(self.star,self.no, self.name, self.price, str(self.change7d)+' %', self.marketcap, self.roi)) 
    
    def displayDaily(self): #default daily
        return(self.fmt.format(self.star,self.no, self.name, self.price, str(self.change24h)+' %', self.marketcap, self.roi)) 
    
    def displayHourly(self): #default hourly
        return(self.fmt.format(self.star,self.no, self.name, self.price, str(self.change1h)+' %', self.marketcap, self.roi)) 

