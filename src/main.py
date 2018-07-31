from InvestopediaApi import ita
import aroon
import time
import bollinger as BB
import numpy
import json
import requests
import candle

def getData(index="AAPL", frequency="1y"):


    candleList=[];
    response = requests.get('https://api.iextrading.com/1.0/stock/' + index + '/chart/' + frequency)
    data = json.loads(response.text)

    for i in data:
        if(i['high']>0 and i['low']>0) and i['close']>0:
            candleList.append(candle.Candle(i['high'],i['open'],i['close'],i['low']))
    return candleList


# main loop
def run():
    print("running")

    while(1):
        print("wow")
        time.sleep(1)



if __name__ == "__main__":
    candleList= getData("AAPL", "1y")
    print("asdf")
    aroonU= aroon.aroonUp(candleList)
    aroonD = aroon.aroonDown(candleList)
   # for i in candleList:
        #i.candlePrint()
    for i,j in zip(aroonU,aroonD):
        print(i," <----> ", j)
    run()
