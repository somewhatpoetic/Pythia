import os
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

# loading all extensions
for fname in os.listdir('./cogs'):
    if fname.endswith('.py'):
        bot.load_extension(f'cogs.{fname[:-3]}')

# on ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready!')

bot.run(TOKEN)
