#!/usr/bin/env python3
from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt

cg = CoinGeckoAPI()
query = cg.get_price(ids='ethereum', vs_currencies='usd')
ticker = cg.get_coin_ticker_by_id('bitcoin')

data = list(query.keys())
moredata = list(query.values())
dictionary = dict(moredata[0])
evenmoredata = list(dictionary.items())
fuckthis = evenmoredata[0]
data.append(fuckthis[0])
data.append(fuckthis[1])

# get some basic info
for i in data:
    print(i)

# get data parsed for plotting
print(ticker)

plt.plot([1, 2, 3, 4], [1, 4, 9, 32])
plt.ylabel('ETH IS GOING TO THE MOON')
plt.show()
