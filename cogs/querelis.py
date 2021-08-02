from discord.ext.commands import Cog


class Querelis(Cog):

    def __init__(self, bot) -> None:
        self.bot = bot


def setup(bot):
    bot.add_cog(Querelis(bot))

