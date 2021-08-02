import discord
from discord.ext import Cog


class Assign(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_member_join(member):
        default_role = discord.utils.get(member.guild.roles, id=853705439338168430)
        await member.add_roles(default_role)


def setup(bot):
    bot.add_cog(Assign(bot))
