from discord.ext import commands


class UrduTTS(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener
    async def on_ready(self):
        print('UrduTTS is ready.')

def setup(bot):
    bot.add_cog(UrduTTS(bot))
