import discord
from discord.ext.commands import command
from discord.ext.commands import Cog


class Assign(Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Assign(bot))
