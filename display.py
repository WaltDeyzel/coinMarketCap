import operator
class DisplayData:
    fmt = '{:<2} {:<3} {:<20} {:<10} {:<10} {:<15} {:<15}'
    stripes = '----------------------------------------------------------------------------------'

    def displayData(self, hourly, daily, weekly):
        #DISPLAY DATA SET
        #DISPLAY TOP 10
        hourly_worst = hourly[:11]
        hourly_best = hourly[-10:]
        daily_worst = daily[:11]
        daily_best = daily[-10:]
        weekly_worst = weekly[:11]
        weekly_best = weekly[-10:]

        hourly_best.reverse()
        weekly_best.reverse()
        daily_best.reverse()
        #----------------------------------------------------------------------------------------------
        #sections hourly, daily, weekly
        bestPerforming = [[hourly_best, hourly_worst], [daily_best, daily_worst], [weekly_best, weekly_worst]]

        for section in bestPerforming:
            print()
            heading = self.fmt.format(' ','NO','COIN', 'PRICE', 'CHANGE', 'MARKETCAP', 'ROI')
            print(heading, ' ', heading)
            print(self.stripes, self.stripes)
            
            lhs = section[0] # DATA DISPLAYED ON THE LEFT
            rhs = section[1] # DATA DISPLAYED ON THE RIGHT

            for i in range(10):
                displayL = lhs[i].displayDaily()
                displayR = rhs[i].displayDaily()

                if(section == bestPerforming[0]):
                    displayL = lhs[i].displayHourly()
                    displayR = rhs[i].displayHourly()
            
                #DO NOT NEED TO CHECH FOR SECTION == BESTPERFORMING[1] BECAUSE IT IS THE DEFAULT
                    
                if(section == bestPerforming[2]):
                    displayL = lhs[i].displayWeekly()
                    displayR = rhs[i].displayWeekly()
                
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
            print(coin.displayWeekly())

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
            print(coin.displayWeekly())