import time
from typing import List

from discord.ext.commands import Cog, command


def removeSpace(lst: List[str]) -> List[str]:
    newList = [i for i in lst if i != ' ']
    return newList


def getSpaceIndex(lst: List[str]) -> List[int]:
    spaces = [i for i, letter in enumerate(lst) if letter == ' ']
    return spaces


def addSpacesBack(lst: List[str], spaces: List[int]) -> List[str]:
    for i in range(0, len(lst) + len(spaces)):
        if i in spaces:
            lst.insert(i, ' ')
    return lst


def camelify(lst: List[str]) -> List[str]:
    for i in range(0, len(lst)):
        if i % 2 == 0:
            lst[i] = lst[i].upper()
    return lst


class SpongebobText(Cog):

    def __init__(self, bot):
        self.bot = bot

    @command(
        help='Outputs text in the Spongebob meme format',
        brief='Output text in the Spongebob meme format'
    )
    async def sbt(self, ctx):
        def get_sbt_text(message: str) -> str:
            lower = message.lower()
            letters = list(lower)

            spaces = getSpaceIndex(letters)
            spacesRemovedLetters = removeSpace(letters)
            camelifiedLetters = camelify(spacesRemovedLetters)
            lettersHalf = addSpacesBack(camelifiedLetters, spaces)
            return ''.join(lettersHalf)

        async def sbt_message_reply() -> str:
            message_obj: discord.Message = await ctx.fetch_message(ctx.message.reference.message_id)
            return get_sbt_text(message_obj.content)

        async def sbt_text_argument() -> str:
            rawMessage: str = ctx.message.content
            message: str = rawMessage.replace('.sbt ', '')
            return get_sbt_text(message)

        sbText: str = ''

        # If message is a reply, then sbt-ify the replied-to message
        if ctx.message.reference is not None:
            sbText = await sbt_message_reply()
        else: # sbt-ify the text in the message
            sbText = await sbt_text_argument()

        await ctx.send(sbText)

        time.sleep(3)
        await ctx.message.delete()

    @Cog.listener()
    async def on_ready(self):
        print('Spongebob Text Generator is ready.')


def setup(bot):
    bot.add_cog(SpongebobText(bot))
