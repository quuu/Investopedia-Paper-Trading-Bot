class Candle:
    def __init__(self, h, o, c, l):
        self.high = h
        self.open = o
        self.close = c
        self.low = l
        if(self.open > self.close):
            self.rising = False
        else:
            self.rising = True

    def candlePrint(self):
        if(self.rising):
            print("Positive")
        else:
            print("Negative")
        print("High  -- " + str(self.high))
        print("Open -- " + str(self.open))
        print("Close  -- " + str(self.close))
        print("Low  -- " + str(self.low))
