from constants import Constants as con
import webbrowser
class CoinData:
    def __init__(self, id, no, star, name, tag, price, change1h, change24h, change7d, roi, marketcap, num_market_pairs, date_added, circulating_supply, max_supply, total_supply, volume_24h):
        self.id = id
        self.no = no
        self.star = star
        self.name = name
        self.tag = tag
        self.price = price
        self.change1h = change1h
        self.change24h = change24h
        self.change7d = change7d
        self.roi = roi
        self.marketcap = marketcap
        self.num_market_pairs = num_market_pairs
        self.date_added = date_added
        self.circulating_supply = circulating_supply
        self.max_supply = max_supply
        self.total_supply = total_supply
        self.volume_24h = volume_24h

    def displayWeekly(self): #default weekly
        return(CoinData.display(self, self.change7d))
    
    def displayDaily(self): #default daily
        return(CoinData.display(self, self.change24h))
    
    def displayHourly(self): #default hourly
        return(CoinData.display(self, self.change1h))

    def display(self, change):
        return(con.fmt.format(self.star,self.no, self.getName(), con.currency+str(self.price), str(change)+' %', self.marketcap, self.volume_24h, self.getVolumeCapRatio(), self.getSupplyRatio())) 
        
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
