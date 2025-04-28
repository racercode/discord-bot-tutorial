import discord
from discord.ext import commands
import os
from core import Cog_Extension

class Music(Cog_Extension):
        
    @commands.command()
    async def play(self, ctx, *args):
        if len(args) != 1:
            await ctx.send("不合法的用法: 用法: play <連結>")
            return
        
        url = args[0]
        song_exist = os.path.isfile("song.mp3")
        try:
            if song_exist:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("請等待目前歌曲結束，或者使用 'stop' 指令")
            return
        
        '''
        TODO (bonus)
        讓使用者能夠查詢歌曲
        (可以使用爬蟲，或者參考 yt-dlp 的更多功能)
        Reference : https://www.mankier.com/1/yt-dlp
        '''

        os.system(f"yt-dlp.exe --extract-audio --audio-format mp3 --audio-quality 0 {url}")
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        if voice is None:
            voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
            await voiceChannel.connect(timeout=600.0)
            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
    
        voice.play(discord.FFmpegPCMAudio(executable='ffmpeg.exe', source="song.mp3"))

    '''
    TODO (bonus)
    讓使用者管理待播放清單，包含加入歌曲、插歌...
    '''
    
    @commands.command()
    async def leave(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        try:
            await voice.disconnect()
        except:
            await ctx.send("機器人沒有連接到語音頻道")


    @commands.command()
    async def pause(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        try: 
            if voice.is_playing():
                voice.pause()
            else:
                await ctx.send("目前沒有歌曲播放")
        except:
            await ctx.send("機器人沒有連接到語音頻道")


    @commands.command()
    async def resume(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        try:
            if voice.is_paused():
                voice.resume()
            else:
                await ctx.send("目前歌曲正在播放")
        except:
            await ctx.send("機器人沒有連接到語音頻道")

    @commands.command()
    async def stop(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        try:
            voice.stop()
        except:
            await ctx.send("機器人沒有連接到語音頻道")
    
async def setup(bot):
    await bot.add_cog(Music(bot))