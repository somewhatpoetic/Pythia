import os

import discord
import random
import time

from dotenv import load_dotenv
from discord import message
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix = 'D ')

@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready!')

@bot.command(name = 'feed')
async def sugg(ctx, *args):
    with open('suggestions.txt', 'a') as f:
        f.write(" ".join(args[:]) + '\n')
    
    await ctx.send('Thank you for your feedback! Please let me know if you have anymore.', delete_after = 3)
    time.sleep(2)
    await ctx.message.delete()

@bot.command(name = 'clear')
async def clear(ctx, amount = 10):
    await ctx.channel.purge(limit = amount)

bot.run(TOKEN)
