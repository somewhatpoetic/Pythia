import discord
from discord.channel import TextChannel
from discord.ext.commands import Cog
import json

def write_json(feedback) -> None:
    with open("feedback.json", "r+") as file:
        data = json.load(file)
        data["feedback"].append(feedback)
        file.seek(0)
        json.dump(data, file, indent=3)

class Querelis(Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @Cog.listener()
    async def on_message(self, ctx):
        chan: TextChannel = discord.utils.get(ctx.guild.channels, name="querelis")
        id = chan.id

        if (ctx.channel.id == id):
            author = ctx.author.name
            content = ctx.content
            entry = {
                "author": author,
                "feedback" : content
            }
            write_json(entry)
            

def setup(bot):
    bot.add_cog(Querelis(bot))

