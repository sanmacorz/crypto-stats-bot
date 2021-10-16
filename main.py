#!/usr/bin/env python3
from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt

cg = CoinGeckoAPI()
query = cg.get_price(ids='ethereum', vs_currencies='usd', include_24hr_vol=True, include_24hr_change=True)
print(query)

# plt.plot([1, 2, 3, 4], [1, 4, 9, 32])
# plt.ylabel('Ethereum price graph in USD')
# plt.show()
