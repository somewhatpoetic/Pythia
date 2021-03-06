import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# declaring intents
intents = discord.Intents().all()

bot = commands.Bot(command_prefix=['.'], intents=intents)

# load extension
def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


# loading all extensions
for fname in os.listdir('./cogs'):
    if fname.endswith('.py'):
        bot.load_extension(f'cogs.{fname[:-3]}')


# on ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready!')
    presence = discord.Game(name='.help', type=3)
    await bot.change_presence(status=discord.Status.online, activity=presence)


bot.run(TOKEN)
