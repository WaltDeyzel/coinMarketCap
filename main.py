import webbrowser
import sys
from cryptoData import CryptoData

if __name__ == "__main__":
    data = CryptoData.getData(CryptoData)
    if(len(sys.argv) > 1):
        try:
            site = CryptoData.findCoin(CryptoData, data, sys.argv[1]).link
            webbrowser.open(site)
        except:
            print('FAIL')
    else:
        CryptoData.show(CryptoData,data)
    