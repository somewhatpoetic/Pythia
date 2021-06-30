import discord
import youtube_dl
from discord.ext.commands import command
from discord.ext.commands import Cog


class Music(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("not in voice channel")

        voice_channel = ctx.author.voice.channel
        await voice_channel.connect()

    @command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @command()
    async def play(self, ctx, url):
        # ctx.voice_client.stop()
        FFMPEG_OPTIONS = {
            'before_options':
            '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn'
        }
        YDL_OPTIONS = {'format': 'bestaudio'}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)


def setup(bot):
    bot.add_cog(Music(bot))
