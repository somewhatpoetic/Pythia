import os
import time
import discord
from discord import message
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix = 'D ')

# Commands -----------------------------------
# feedback command
@bot.command(name = 'feed')
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

# run a poll command
@bot.command(name = 'poll', pass_context = True)
async def poll(ctx, question, *options: str):
    if len(options) <= 1:
        await ctx.send('You need more than one option to make a poll!')
        return
    if len(options) > 10:
        await ctx.send('You cannot make a poll for more than 10 things!')
        return

    if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
        reactions = ['✅', '❌']
    else:
        reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

    description = []
    for x, option in enumerate(options):
        description += '\n {} {}'.format(reactions[x], option)
    msg = discord.Embed(title = question, description = ''.join(description))
    react_message = await ctx.send(embed=msg)
    for i in range(len(options)):
        await react_message.add_reaction(reactions[i])
    msg.set_footer(text='Poll ID: {}'.format(react_message.id))
    await bot.edit_message(react_message, embed=msg)


# Events -------------------------------------
# on ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready!')

bot.run(TOKEN)
