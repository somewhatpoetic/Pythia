
import gtts
from discord.ext import commands
from playsound import playsound


class UrduTTS(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('UrduTTS is ready.')

    @commands.command()
    async def urduTTS(self, ctx):
        userText = ctx.message.content
        text = userText.replace('.urduTTS ', '')
        audio = gtts.gTTS(text=text, lang='ur')
        audio.save('urduTTS.mp3')

        playsound('urduTTS.mp3')


def setup(bot):
    bot.add_cog(UrduTTS(bot))
