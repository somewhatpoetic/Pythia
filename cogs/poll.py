import discord
import random
from discord import emoji
from discord.ext import commands
from discord.ext.commands.bot import Bot

class Poll(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.emojiList = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Poll feature is ready.')

    # Commands
    @commands.command()
    async def poll(self, ctx):
        # Extracting question from message
        rawMessage = ctx.message.content
        message = rawMessage.replace("D poll ", "")
        splitMessage = list(message.split("/"))
        question = splitMessage[0]
        splitMessage.pop(0)

        # Assigning emojis to each option
        optionsList = []
        for x in range(len(splitMessage)):
            optionsList += '\n {}   {}'.format(self.emojiList[x], splitMessage[x])

        # Creating embedded message
        pollEmbed = discord.Embed(title = question, description = ''.join(optionsList), color = 0x83bae3)
        e = await ctx.send(embed = pollEmbed)

        # Adding reactions to embed
        for i in range(len(splitMessage)):
            await e.add_reaction(self.emojiList[i])

        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Poll(bot))