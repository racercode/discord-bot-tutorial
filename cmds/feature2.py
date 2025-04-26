from discord.ext import commands
from core import Cog_Extension

class Feature2(Cog_Extension):
        
    @commands.command()
    async def Hi(self, ctx):
        await ctx.send("Hi, Sprout")
    
    '''
    TODO
    新增你的自訂功能。
    '''

async def setup(bot):
    await bot.add_cog(Feature2(bot))