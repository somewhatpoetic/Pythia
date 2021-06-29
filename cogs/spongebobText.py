from discord.ext import commands
import time


class SpongebobText(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        help='Outputs text in the Spongebob meme format',
        brief='Output text in the Spongebob meme format'
    )
    async def sbt(self, ctx):
        rawMessage = ctx.message.content
        message = rawMessage.replace('.sbt ', '')
        lower = message.lower()
        letters = list(lower)

        for i in range(0, len(letters)):
            if (i % 2 == 0):
                if letters[i] == ' ':
                    letters[i+1] = letters[i+1].upper()
                else:
                    letters[i] = letters[i].upper()

        sbText = ''.join(letters)
        await ctx.send(sbText)

        time.sleep(3)
        await ctx.message.delete()

    @commands.Cog.listener()
    async def on_ready(self):
        print('Spongebob Text Generator is ready.')


def setup(bot):
    bot.add_cog(SpongebobText(bot))
