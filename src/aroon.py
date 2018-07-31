import sys


'''

Aroon up = ((25 - days since last 25 day high)/25) * 100
Aroon down = ((25 - days since last 25 day low)/25) * 100

'''
def aroonUp(candleList):
    current=0

    terms=25
    count=0
    currenthigh=0.0
    daysSince=0
    toReturn=[]
    for i in candleList:
        if(currenthigh>i.high):
            daysSince+=1
        else:
            daysSince-=1
            currenthigh = i.high
        if(daysSince>25):
            daysSince=25
        if(daysSince<0):
            daysSince=0
        print(daysSince)
        toReturn.append(((25-daysSince)/25)*100)
    return toReturn

def aroonDown(candleList):
    current =0

    terms = 25
    count=0
    currentlow=25555
    daysSince=0
    toReturn=[]
    for i in candleList:

        if(currentlow<i.low):
            daysSince-=1
            currentlow=i.low
        else:
            daysSince+=1
        if(daysSince>25):
            daysSince=25
        if(daysSince<0):
            daysSince=0
        toReturn.append(((25-daysSince)/25)*100)
    return toReturn
