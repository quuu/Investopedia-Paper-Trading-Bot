from InvestopediaApi import ita
import bollinger as BB
import numpy
import json
import requests
import candle

def getData(index="AAPL", frequency="1y"):


    candleList=[];highList=[];lowList=[];openList=[];closeList=[];dateList=[]
    response = requests.get('https://api.iextrading.com/1.0/stock/' + index + '/chart/' + frequency)
    data = json.loads(response.text)

    for i in data:
        if(i['high']>0 and i['low']>0) and i['close']>0:
            #highList.append(i['high'])
            #lowList.append(i['low'])
            #openList.append(i['open'])
            closeList.append(i['close'])
            dateList.append(i['date'])
            candleList.append(candle.Candle(i['high'],i['open'],i['close'],i['low']))
    return closeList,candleList,dateList


# main loop
def run():
    print("running")




if __name__ == "__main__":
    closeList,candleList,dateList = getData("AAPL", "1y")
    print("asdf")
    for i in candleList:
        i.candlePrint()
