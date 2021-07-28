# from inspect import getmembers
# from discord import client
# from discord.ext.commands.converter import GuildConverter
# from typing import List
# from discord.channel import VoiceChannel
# from discord.ext.commands import Cog, cog, command
# import discord
# import discord.utils
# import os
# from dotenv import load_dotenv

# load_dotenv()
# GUILD = os.getenv('DISCORD_GUILD')

# class WatchParty(Cog):

#     def __init__(self, bot):
#         self.bot = bot

#     @Cog.listener()
#     async def on_ready(self):
        
#     # @Cog.listener()
#     # async def (self):
#     #     #chan: VoiceChannel = discord.utils.get(ctx.guild.voice_channels, id=853735209144811590)
#     #     print(discord.Guild.id)
        
#         #vc = ctx.guild.get_channel(853735209144811590)
        
#         # vc = discord.utils.get(ctx.message.server.channels, id=853735209144811590)

#         # for x in vc.members:
#         #     print(x)
#         # for x in chan.members:
#         #     print(x)

#         # x =chan.members[1].voice.self_stream
#         # print(x)



# def setup(bot):
#     bot.add_cog(WatchParty(bot))