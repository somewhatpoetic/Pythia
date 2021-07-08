import discord
from discord.ext import commands


class Assign(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = discord.utils.get(member.server.roles, name='Tribus')
        await self.bot.add_roles(member, role)


def setup(bot):
    bot.add_cog(Assign(bot))
