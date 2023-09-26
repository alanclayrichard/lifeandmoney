# python 
# 09/26/23

# The class to represent a market in the simulation that has the following attributes:
# rate: the rate of return for the market
# maket cap: the market cap of the market

class Market:
    # init method
    def __init__(self, rate, market_cap):
        self.rate = rate
        self.market_cap = market_cap
        