#!/usr/bin/env python3
import discord
from discord.ext import commands
import asyncio
from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt
import functions

# Set initial values
token = functions.load_token('token.key')
prefix = "$"
bot = commands.Bot(command_prefix=prefix)
cg = CoinGeckoAPI()

# Display the name of the specified coin 
@bot.command()
async def price(ctx, arg):
    request = cg.get_coins_list()
    search = str(arg)
    print(arg)
    for data in request:
        if (data["id"] == search):
            await ctx.send(data)

# Initialize the bot by giving it the token
bot.run(token)
