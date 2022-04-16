import discord
from discord.ext import commands
import youtube_dl
import random

class music(commands.Cog):
    def __init__(self, client):
      self.client = client 

    @commands.command()
    async def join(self,ctx):
       if ctx.author.voice is None:
           await ctx.send("Voice Channel toh join kar lawdeee!!")
       voice_channel = ctx.author.voice.channel           
       if ctx.voice_client is None:
          await voice_channel.connect()
          await ctx.send("Rom Rom bhoi !!")
       else:
          await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self,ctx,url):
        
        if ctx.author.voice is None:
            await ctx.send("Voice Channel toh join kar lawdeee!!")
        voice_channel = ctx.author.voice.channel           
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

        ctx.voice_client.stop()
        await ctx.send(f"Now playing >> {url} ")
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        vc = ctx.voice_client
        
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)

    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send("Paused=>")

    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send("resume>||") 

    @commands.command()
    async def vibecheck(self,ctx):
        num=random.randint(0,100)
        if num%2==0:
            await ctx.send(f"Vibe Check Failed! :(")   
        else:
            await ctx.send(f"Vibe Check Passed! :)")
def setup(client):
    client.add_cog(music(client))