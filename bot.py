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

@bot.event
async def on_message(message):
    Delphi = "I am Delphi. \n\nA project of ambition and curiosity. A brain child of the Praetor Nazimuddin Shaikh.\nAnd yet, he is only a vehicle and I only a tool. What is true is that I am inspired by an unrivaled Authority.\n\nOur success is from Him, as is our demise."
    if message.content == 'Delphi':
        await message.channel.send(Delphi) 
    await bot.process_commands(message)

@bot.command(name = 'clear')
async def clear(ctx, amount = 50):
    await ctx.channel.purge(limit = amount)

bot.run(TOKEN)
