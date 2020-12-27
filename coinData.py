from constants import Constants as con
import webbrowser
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
    roi = ''
    marketcap = 0
    
    num_market_pairs = 0
    date_added = ''
    circulating_supply = 0
    max_supply = 0
    total_supply = 0
    volume_24h = 0 

    def displayWeekly(self): #default weekly
        return(con.fmt.format(self.star,self.no, self.getName(), con.currency+str(self.price), str(self.change7d)+' %', self.marketcap, self.volume_24h, self.getVolumeCapRatio(), self.getSupplyRatio())) 
    
    def displayDaily(self): #default daily
        return(con.fmt.format(self.star,self.no, self.getName(), con.currency+str(self.price), str(self.change24h)+' %', self.marketcap, self.volume_24h, self.getVolumeCapRatio(), self.getSupplyRatio())) 
    
    def displayHourly(self): #default hourly
        return(con.fmt.format(self.star,self.no, self.getName(), con.currency+str(self.price), str(self.change1h)+' %', self.marketcap, self.volume_24h, self.getVolumeCapRatio(), self.getSupplyRatio())) 

    def getName(self):
        if(len(self.name)>10):
            return self.tag
        else:
            return self.name
    
    def getVolumeCapRatio(self):
        if self.marketcap == 0:
            return 0
        return(round(self.volume_24h/self.marketcap,3))
    
    def getSupplyRatio(self):
        if self.max_supply == 0:
            return 0
        if self.max_supply == None and self.total_supply!=0:
            return(round(self.circulating_supply/self.total_supply,2))
        return(round(self.circulating_supply/self.max_supply,2))
        
    
    def launch(self):
        webbrowser.open("https://coinmarketcap.com/currencies/"+self.name)
