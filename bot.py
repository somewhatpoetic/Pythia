import os
import time
import discord
from discord import message
from discord import client
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix = ['.'])

# load extension
@bot.command(hidden = True)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

# unload extension
@bot.command(hidden = True)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

# loading all extensions
for fname in os.listdir('./cogs'):
    if fname.endswith('.py'):
        bot.load_extension(f'cogs.{fname[:-3]}')


# Commands -----------------------------------
# feedback command
@bot.command()
async def feed(ctx, *args):
    with open('suggestions.txt', 'a') as f:
        f.write(" ".join(args[:]) + '\n')
    await ctx.send('Thank you for your feedback! Please let me know if you have anymore.', delete_after = 3)
    time.sleep(2)
    await ctx.message.delete()

# clear command
@bot.command(name = 'clear')
async def clear(ctx, amount = 50):
    await ctx.channel.purge(limit = amount)

# Events -------------------------------------
# on ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready!')

bot.run(TOKEN)
