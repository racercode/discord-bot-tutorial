from discord.ext import commands
from core import Cog_Extension
from google import genai
from google.genai import types
import os
import asyncio

# 這邊的註解是 Python 函式宣告的一部份，Google Gemini 會根據這些註解來決定如何呼叫這個函式，一定要寫 !
def get_current_temperature(location: str) -> dict:
    """Gets the current temperature for a given location.

    Args:
        location: The city name, e.g. Taipei
    Returns:
        A dictionary containing the location and the current temperature, e.g. {"location": "Taipei", "temperature": "33.5°C"}
    """
    # TODO: call a real weather API here
    return {"location": location, "temperature": "33.5°C"}

class Chat(Cog_Extension):

    @commands.command()
    async def hey(self, ctx, *args):
        if len(args) == 0:
            await ctx.send("不合法的用法: 用法: hey <prompt>")
            return

        prompt = ''.join(args)
        response = await asyncio.to_thread(
            self.chat.send_message,
            prompt
        )
        await ctx.send(response.text)

    @commands.command()
    async def clear(self, ctx):
        self._init_chat()
        await ctx.send("對話已重置")

    def _init_chat(self):
        config = types.GenerateContentConfig(tools=[get_current_temperature])
        self.chat = self.client.chats.create(model="gemini-3.1-flash-lite-preview", config=config)

    def __init__(self, *args):
        super().__init__(*args)
        self.client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
        self._init_chat()

async def setup(bot):
    await bot.add_cog(Chat(bot))
