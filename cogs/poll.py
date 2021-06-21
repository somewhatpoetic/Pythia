import discord
import random
from emojiList import emojiList
from discord.ext import commands

class Poll(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.emojiList = emojiList

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Poll feature is ready.')

    # Commands
    @commands.command()
    async def poll(self, ctx):
        # Extracting question from message
        rawMessage = ctx.message.content
        message = rawMessage.replace(".poll ", "")
        splitMessage = list(message.split("/"))
        question = splitMessage[0]
        splitMessage.pop(0)

        # Assigning emojis to each option
        randomizedList = random.sample(self.emojiList, 20)
        optionsList = []
        for x in range(len(splitMessage)):
            optionsList += '\n {} {}'.format(randomizedList[x], splitMessage[x])

        # Creating embedded message
        pollEmbed = discord.Embed(title = question, description = ''.join(optionsList), color = 0x83bae3)
        e = await ctx.send(embed = pollEmbed)

        # Adding reactions to embed
        for i in range(len(splitMessage)):
            await e.add_reaction(randomizedList[i])

        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Poll(bot))