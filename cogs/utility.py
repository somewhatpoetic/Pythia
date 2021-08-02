import time
from discord.ext import commands

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # clear command
    @commands.command(
        help='This command clears messages',
        brief='Clear messages'
    )
    async def clear(self, ctx, amt):
        if amt.lower() == 'all':
            await ctx.channel.purge(limit=10000)
        elif amt.isnumeric() is True:
            await ctx.channel.purge(limit=int(amt) + 1)
        elif amt.isnumeric() is False:
            await ctx.send("""Invalid syntax.

Please use numbers to specify how many messages to delete.
Alternatively, you could use the clear all option, as such: `.clear all`.""")


def setup(bot):
    bot.add_cog(Misc(bot))
