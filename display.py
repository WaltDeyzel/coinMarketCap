import operator
class DisplayData:
    fmt = '{:<2} {:<3} {:<20} {:<10} {:<10} {:<15} {:<15}'
    stripes = '----------------------------------------------------------------------------------'

    def displayData(self, bestPerforming, wallet):
        
        for section in bestPerforming:
            print()
            heading = self.fmt.format(' ','NO','COIN', 'PRICE', 'CHANGE', 'MARKETCAP', 'ROI')
            print(heading, ' ', heading)
            print(self.stripes, self.stripes)
            
            lhs = section[0] # DATA DISPLAYED ON THE LEFT
            rhs = section[1] # DATA DISPLAYED ON THE RIGHT

            for i in range(10):
                #MARK DATA THAT IS ALSO IN THE WATCHLIST WITH A *
                starL = " "
                starR = " "
                changeL = lhs[i].change24h #DEFAULT 24H
                changeR = rhs[i].change24h #DEFAULT 24H

                lhs_name = lhs[i].name
                rhs_name = rhs[i].name
                if(len(lhs_name)>15):
                    lhs_name = lhs[i].tag
                if(len(rhs_name)>15):
                    lhs_name = rhs[i].tag

                if(section == bestPerforming[0]):
                    changeL = lhs[i].change1h
                    changeR = rhs[i].change1h
            
                #DO NOT NEED TO CHECH FOR SECTION == BESTPERFORMING[1] BECAUSE IT IS THE DEFAULT
                    
                if(section == bestPerforming[2]):
                    changeL = lhs[i].change7d
                    changeR = rhs[i].change7d
                
                if lhs[i].tag in wallet:
                    starL = "*"
                    
                if rhs[i].tag in wallet:
                    starR = "*"
            
                displayL = self.fmt.format(starL, lhs[i].no, lhs_name, lhs[i].price, changeL, lhs[i].marketcap, lhs[i].roi)
                displayR = self.fmt.format(starR, rhs[i].no, rhs_name, rhs[i].price, changeR, rhs[i].marketcap, rhs[i].roi)
                print(displayL,'|', displayR,'|')
            print(self.stripes, self.stripes)
    
    def displayWatchlist(self, watchlist):
        watchlist = sorted(watchlist, key=operator.attrgetter('change7d'))
        watchlist.reverse()
       
        print(self.stripes, self.stripes)
        print()
        print('___________________________________WATCHLIST___________________________________')
        print(self.fmt.format('#','NO','COIN', 'PRICE', 'CHANGE', 'MARKETCAP', 'ROI'))
        print(self.stripes, self.stripes)

        for coin in watchlist:
            print(self.fmt.format(' ',coin.no, coin.name, coin.price, str(coin.change7d)+' %', str(coin.change24h)+' %', coin.marketcap, coin.roi)) 

    def displayWorstPerforming(self, weekly):
        print()
        pairs = []
        n = 30
        for coin in weekly:

            if(coin.no <= n):
                if(coin.change7d < 0):
                    pairs.append(coin)

        print('Worst performing coin past week in top' , n)
        for coin in pairs:
            print(self.fmt.format(' ',coin.no, coin.name, coin.price, str(coin.change7d)+' %', coin.marketcap, coin.roi))