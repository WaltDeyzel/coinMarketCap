from constants import Constants as con

class coinData:
    id = 0
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
    
    num_market_pairs = 0
    date_added = ''
    circulating_supply = 0
    max_supply = 0
    total_supply = 0
    volume_24hvolume_24h = 0 

    def displayWeekly(self): #default weekly
        return(con.fmt.format(self.star,self.no, self.getName(), con.currency+str(self.price), str(self.change7d)+' %', self.marketcap, self.roi)) 
    
    def displayDaily(self): #default daily
        return(con.fmt.format(self.star,self.no, self.getName(), con.currency+str(self.price), str(self.change24h)+' %', self.marketcap, self.roi)) 
    
    def displayHourly(self): #default hourly
        return(con.fmt.format(self.star,self.no, self.getName(), con.currency+str(self.price), str(self.change1h)+' %', self.marketcap, self.roi)) 

    def getName(self):
        if(len(self.name)>10):
            return self.tag
        else:
            return self.name
