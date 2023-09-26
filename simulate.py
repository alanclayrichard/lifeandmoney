# python 

from man import Man
from market import Market
# from year import Year
import numpy as np
import names

N = 100


# simulate the man in the market
if __name__ == "__main__":

    men = []

    # make 100 men with random ages, assets, and health
    for i in range(N):
        men.append(Man(names.get_full_name(), np.random.randint(18, 100), np.random.randint(10000, 1000000), np.random.randint(0, 100)))
    
    for man in men: 
        print(man)

    # make a market with a random rate and 40 trillion market cap
    market = Market(np.random.randint(5, 15), 40000000000000)

    # describe the population
    


