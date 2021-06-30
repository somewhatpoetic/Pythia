from discord.ext import commands


class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        help='General information about Pythia',
        brief='General information about Pythia'
    )
    async def Pythia(self, ctx):
        await ctx.send('I am Pythia. A bot of many abilities.')


def setup(bot):
    bot.add_cog(Info(bot))
