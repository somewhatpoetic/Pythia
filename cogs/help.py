from typing import Optional

from discord import Embed
from discord.utils import get
from discord.ext.commands import Cog
from discord.ext.commands import command


def syntax(command):
    cmd_and_aliases = "|".join([str(command), *command.aliases])
    params = []

    for key, value in command.params.items():
        if key not in ("self", "ctx"):
            params.append(
                f"[{key}]" if "NoneType" in str(value) else f'<{key}>'
            )
    params = " ".join(params)

    return f"```{cmd_and_aliases} {params}```"


class Help(Cog):

    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('help')

    @Cog.listener()
    async def on_ready(self):
        print('Help menu is ready.')

    def cmd_help(self, ctx, command):
        embed = Embed(
            title='{command}',
            description=syntax(command),
            color=ctx.author.color
        )
        embed.add_field(name="Command Description", value=command.help)

    @command(
        aliases=[
            "Help",
            "Assistance",
            "assistance",
            "assist"
            ]
    )
    async def help(self, ctx, cmd: Optional[str]):
        if cmd is None:
            pass
        else:
            if (cmd := get(self.bot.commands, name=cmd)):
                await self.cmd_help(ctx, command)

            else:
                await ctx.send("That command does not exist, yet.")


def setup(bot):
    bot.add_cog(Help(bot))
