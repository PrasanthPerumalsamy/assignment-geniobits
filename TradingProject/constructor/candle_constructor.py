class Candle:
    def __init__(self,id,open,high,low,close,date,volume):
        self.id = id
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.date = date
        self.volume = volume

    def __repr__(self):
        return f"Candle(id={self.id}, open={self.open}, high={self.high}, low={self.low}, close={self.close}, date={self.date}, volume={self.volume})"

class SingleCandle:
    def __init__(self,open,high,low,close,volume):
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def __repr__(self):
        return f"Candle(open={self.open}, high={self.high}, low={self.low}, close={self.close}, volume={self.volume})"

