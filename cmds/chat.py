from discord.ext import commands
from core import Cog_Extension
from google import genai
from google.genai import types
import os

class Chat(Cog_Extension):

    @commands.command()
    async def Response(self, ctx, *args):
        if len(args) == 0:
            await ctx.send("不合法的用法: 用法: Response <prompt>")
            return 
        prompt = ''.join(args)

        '''
        TODO
        讓 self.client 完成單次的對話。
        讓 Bot 回傳本次 Gemini 的回應。
        Reference: https://ai.google.dev/gemini-api/docs/text-generation
        '''

    @commands.command()
    async def Chat(self, ctx, *args):
        if len(args) == 0:
            await ctx.send("不合法的用法: 用法: Chat <prompt>")
            return
        if self.chat:
            await ctx.send("請先初始化對話")
            return
        
        prompt = ''.join(args)

        '''
        TODO
        讓 self.client 完成來回多次的對話。( 一次 Chat 代表多次對話的其中一次對話 )
        讓 Bot 回傳本次 Gemini 的回應。
        Reference: https://ai.google.dev/gemini-api/docs/text-generation
        '''

    @commands.command()
    async def NewChat(self, ctx, *args):
        if len(args) == 0:
            await ctx.send("不合法的用法: 用法: NewChat <system_instruction>")
            return
        system_instruction = ''.join(args)

        '''
        TODO
        開始一個多次的對話，並設定 system_instruction 提供 Gemini 背景知識。
        Reference: https://ai.google.dev/gemini-api/docs/text-generation
        '''

    def __init__(self, *args):
        super().__init__(*args)
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.chat = None

async def setup(bot):
    await bot.add_cog(Chat(bot))