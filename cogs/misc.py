import time
from discord.ext import commands

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # feedback command
    @commands.command()
    async def feed(ctx, *args):
        with open('suggestions.txt', 'a') as f:
            f.write(" ".join(args[:]) + '\n')
        await ctx.send('Thank you for your feedback! Please let me know if you have anymore.', delete_after = 3)
        time.sleep(2)
        await ctx.message.delete()

    # clear command
    @commands.command(name = 'clear')
    async def clear(ctx, amount = 50):
        await ctx.channel.purge(limit = amount)
        
def setup(bot):
    bot.add_cog(Misc(bot))