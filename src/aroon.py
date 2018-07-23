import sys


'''

Aroon up = ((25 - days since last 25 day high)/25) * 100
Aroon down = ((25 - days since last 25 day low)/25) * 100

'''
def aroonUp(candleList):
    current=0

    terms=25
    count=0
    high=0
    daysSince=0
    toReturn=[]
    for i in candleList:
        if (i.high > high):
            high = i.high

