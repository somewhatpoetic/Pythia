import time

from discord.ext.commands import command
from discord.ext.commands import Cog


def removeSpace(list):
    newList = [i for i in list if i != ' ']
    return newList


def getSpaceIndex(list):
    spaces = [i for i, letter in enumerate(list) if letter == ' ']
    return spaces


def addSpacesBack(list, spaces):
    for i in range(0, len(list) + len(spaces)):
        if i in spaces:
            list.insert(i, ' ')
    return list


def camelify(list):
    for i in range(0, len(list)):
        if i % 2 == 0:
            list[i] = list[i].upper()
    return list


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

        spaces = getSpaceIndex(letters)
        spacesRemovedLetters = removeSpace(letters)
        camelifiedLetters = camelify(spacesRemovedLetters)
        lettersHalf = addSpacesBack(camelifiedLetters, spaces)

        sbText = ''.join(lettersHalf)
        await ctx.send(sbText)

        time.sleep(3)
        await ctx.message.delete()

    @Cog.listener()
    async def on_ready(self):
        print('Spongebob Text Generator is ready.')


def setup(bot):
    bot.add_cog(SpongebobText(bot))
