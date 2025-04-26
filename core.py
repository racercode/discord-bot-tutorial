import discord
from discord.ext import commands

class Cog_Extension(commands.Cog):
    '''
    bot: discord bot instance
    '''
    def __init__(self, bot):
        self.bot = bot