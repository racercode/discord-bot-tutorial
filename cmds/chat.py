from discord.ext import commands
from core import Cog_Extension
from google import genai
from google.genai import types
import os

class Chat(Cog_Extension):

    @commands.command()
    async def Response(self, ctx, *args):
        if len(args) == 0:
            await ctx.send("Invalid arguments: Usage: Response <prompt>")
            return 
        prompt = ''.join(args)

        '''
        TODO
        Let self.client does a single text generation.
        Send the LLM response back to Discord.
        Reference: https://ai.google.dev/gemini-api/docs/text-generation
        '''

    @commands.command()
    async def Chat(self, ctx, *args):
        if len(args) == 0:
            await ctx.send("Invalid arguments: Usage: Chat <prompt>")
            return
        if self.chat:
            await ctx.send("Please starta new chat first.")
            return
        
        prompt = ''.join(args)

        '''
        TODO
        Let self.chat do multi-turn conversation.
        Send the LLM response back to Discord.
        Reference: https://ai.google.dev/gemini-api/docs/text-generation
        '''

    @commands.command()
    async def NewChat(self, ctx, *args):
        if len(args) == 0:
            await ctx.send("Invalid arguments: Usage: NewChat <system_instruction>")
            return
        system_instruction = ''.join(args)

        '''
        TODO
        Start a new multi-turn conversation with custom system_instruction
        Send the LLM response back to Discord.
        Reference: https://ai.google.dev/gemini-api/docs/text-generation
        '''

    def __init__(self, *args):
        super().__init__(*args)
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.chat = None

async def setup(bot):
    await bot.add_cog(Chat(bot))