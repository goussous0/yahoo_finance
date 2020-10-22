import yfinance as yf
import threading
import os
import  pandas as pd
from pandas_datareader import data as pdr
from clint.textui import puts ,colored, indent

portfolio = ["GC=F","AAPL","NVDA","RUB=X"]

thread_lst = []
def intro(item):

    msft = yf.Ticker(item)
    data = yf.download(item, start="1995-01-01", end="2020-03-15")
    print(len(data))

    hist = msft.history(period="max")
    msft.info

    tmp_info = ["priceToSalesTrailing12Months","startDate","averageVolume","dayHigh","toCurrency","maxAge",
                "lastMarket","exDividendDate","totalAssets","open","ytdReturn","market","exchangeTimezoneName",
                "headSymbol","gmtOffSetMilliseconds","regularMarketVolume","averageVolume10days","isEsgPopulated",
                "regularMarketPrice","fiftyDayAverage","regularMarketDayLow","fiftyTwoWeekLow","bid","quoteType",
                "volume","strikePrice","expireDate","averageDailyVolume10Day","twoHundredDayAverage","yield",
                "fiftyTwoWeekHigh","regularMarketOpen","fiveYearAvgDividendYield","volume24Hr","dividendRate",
                "payoutRatio","volumeAllCurrencies","priceHint","forwardPE","previousClose","currency","maxSupply",
                "navPrice","askSize","exchangeTimezoneShortName","openInterest","logo_url","tradeable",
                "regularMarketDayHigh","exchange","underlyingSymbol","symbol","dividendYield","beta",
                "trailingAnnualDividendRate","fromCurrency","ask","bidSize","shortName",
                "regularMarketPreviousClose","circulatingSupply","algorithm","dayLow",
                "trailingAnnualDividendYield","marketCap","underlyingExchangeSymbol"]

    option_lst = ["dayHigh","market","dayLow","open","currency","ask","exchange","averageVolume","bid","symbol"]

    for item in msft.info:
        if item == "symbol":
            path = os.getcwd() +"/"+str(msft.info[item]+".csv")

           # print (path)
        if [ option for option in option_lst if option == item in option_lst]:

        #puts(colored.cyan(str(item)+"              "+str(msft.info[item])))
            puts(colored.cyan(str(item)+"<>                 <>"+str(msft.info[item])))
    #puts(colored.yellow(option_lst[0]+" "+str(msft.info[option_lst[0]])))

    ## the important user options are done

    #print (type(pd.DataFrame(data)))


    data.to_csv(path , index=True , header=True)
    print ((pd.DataFrame(data)))






# get histo
# rical market data






if __name__ == "__main__":
    print (" welcome sir !!!")
    for item in portfolio:
        intro(item)
