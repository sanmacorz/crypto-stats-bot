#!/usr/bin/env python3
import nextcord
from nextcord.ext import commands
import asyncio
from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt
import functions

# Set initial values
token = functions.load_token("token.key")
prefix = "$"
bot = commands.Bot(command_prefix=prefix)
cg = CoinGeckoAPI()

# Display the name of the specified coin
@bot.command()
async def price(ctx, arg1, arg2):
    request = cg.get_coins_list()
    search = str(arg1)
    for data in request:
        if data["id"] == search.lower():
            arg1 = data["id"]
            arg2 = arg2.lower()
            request = cg.get_price(ids=arg1, vs_currencies=arg2)
            await ctx.send(request)
        elif data["symbol"] == search.lower():
            arg1 = data["id"]
            arg2 = arg2.lower()
            request = cg.get_price(ids=arg1, vs_currencies=arg2)
            elements = []
            [elements.extend([key, value]) for key, value in request.items()]
            [elements.extend([key, value]) for key, value in elements[1].items()]
            del elements[1]
            request = elements[0].capitalize() + elements[1].upper() + str(elements[2])
            await ctx.send(request)
        elif data["name"] == search.capitalize():
            arg1 = data["id"]
            arg2 = arg2.lower()
            request = cg.get_price(ids=arg1, vs_currencies=arg2)
            await ctx.send(request)


# Initialize the bot by giving it the token
bot.run(token)

# TO DO:
# Prettify the price output
# Implement error messages for the user
# Move commands to a single file
# Implement Embed messages for configuration
