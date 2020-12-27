import os
import sys
from time import sleep
from api import CryptoData

if __name__ == "__main__":
    data = CryptoData.getData(CryptoData)
    if(len(sys.argv) > 1):
        if(sys.argv[1] == 'time'):
            for i in range(12):
                CryptoData.show(CryptoData,data)
                sleep(600) # 10 min 12 times = 2 hours
                os.system('cmd /c "cls"')
                data = CryptoData.getData(CryptoData)
        else:
            try:
                site = CryptoData.findCoin(CryptoData, data, sys.argv[1]).launch()
            except:
                print('FAIL')
    else:
        CryptoData.show(CryptoData,data)
    