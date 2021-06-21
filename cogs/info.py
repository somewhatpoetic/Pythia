from discord.ext import commands

class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Delphi(self, ctx):
        await ctx.send('I am Delphi. A bot of many abilities.')

def setup(bot):
    bot.add_cog(Info(bot))