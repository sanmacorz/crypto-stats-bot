#!/usr/bin/env python3
import discord
from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt
import functions

token = functions.load_token('token.key')
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$price'):
        cg = CoinGeckoAPI()
        query = cg.get_price(ids='ethereum', vs_currencies='usd', include_24hr_vol=True, include_24hr_change=True)
        await message.channel.send(query)
    elif message.content.startswith('$list'):
        cg = CoinGeckoAPI()
        query = cg.get_coins_list()
        await message.channel.send(query)
    elif message.content.startswith('$ping'):
        cg = CoinGeckoAPI()
        query = cg.ping()
        await message.channel.send(query)

client.run(token)
