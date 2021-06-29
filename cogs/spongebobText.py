import time

from discord.ext.commands import command
from discord.ext.commands import Cog


class SpongebobText(Cog):

    def __init__(self, bot):
        self.bot = bot

    @command(
        help='Outputs text in the Spongebob meme format',
        brief='Output text in the Spongebob meme format'
    )
    async def sbt(self, ctx):
        rawMessage = ctx.message.content
        message = rawMessage.replace('.sbt ', '')
        lower = message.lower()
        letters = list(lower)

        """
        letters = ['M', 'y', ' ', 'n', 'a', 'm', 'e', ' ']
        """

        offset = 0
        for i in range(0, len(letters)):
            offset += i
            if (offset % 2 == 0):
                if letters[i] == ' ':
                    letters[offset] = letters[offset].upper()
                    offset += 1
                else:
                    letters[offset] = letters[offset].upper()

        sbText = ''.join(letters)
        await ctx.send(sbText)

        time.sleep(3)
        await ctx.message.delete()

    @Cog.listener()
    async def on_ready(self):
        print('Spongebob Text Generator is ready.')


def setup(bot):
    bot.add_cog(SpongebobText(bot))
