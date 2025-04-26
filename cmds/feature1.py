from discord.ext import commands
from core import Cog_Extension

class Feature1(Cog_Extension):
        
    @commands.command()
    async def Hello(self, ctx):
        await ctx.send("Hello, world")
    
    '''
    TODO
    Add the necessary bot commands of your custom feature.
    '''

async def setup(bot):
    await bot.add_cog(Feature1(bot))