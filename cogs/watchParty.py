'''
Feature to create watch parties.
Use command .watchparty 

use .watchparty
send direct message to user
ask for:
What are you watching?
When are you hosting the watch party? (now, in x hours, at 3 pm [cst, gmt])
How early do you want to send a reminder for the watch party (15, 30, hour)
private or open?
if private - who are invited? (@username#1234)
'''

from typing import List
from discord import guild
from discord.channel import VoiceChannel
from discord.ext.commands import Cog, command
import discord
import discord.utils

class WatchParty(Cog):

    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print('Watch party feature is ready.')

    @command()
    async def watchparty(self, ctx):
        message = ctx.message.content.replace('.watchparty ', '')
        messageList: List[str] = message.split(',')
        title: str = messageList[0]
        
        category = discord.utils.get(ctx.guild.categories, id=866142892254691348)

        await ctx.guild.create_voice_channel(name=title, category=category)


def setup(bot):
    bot.add_cog(WatchParty(bot))