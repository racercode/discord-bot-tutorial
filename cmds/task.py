from discord.ext import commands
from core import Cog_Extension
import datetime

class Task():
    def __init__(self, name: str, description: str, deadline: datetime.datetime):
        self.name: str = name
        self.deadline: datetime.datetime = deadline
        self.description: str = description

class Scheduler(Cog_Extension):

    @commands.command()
    async def AddTodoList(self, ctx, *args):
        try:
            name, description, date, deadline = args
        except Exception as e:
            await ctx.send("不合法的用法: 用法: AddTodoList <事項名稱> <詳細資訊> <期限>")
            return
        try:
            deadline_object = datetime.datetime.strptime(f'{date} {deadline}', "%Y-%m-%d %H:%M")
        except ValueError as e:
            await ctx.send("錯誤日期格式：範例：2025-05-18 23:59")
            return
        
        '''
        TODO
        新增一個事項到 TodoList
        如果有一個同名的已經存在，則不新增。
        '''

        

    @commands.command()
    async def RemoveTodoList(self, ctx, *args):
        if len(args) != 1:
            await ctx.send("不合法的用法: 用法: RemoveTodoList <事項名稱>")
            return
        
        task_name = args[0]

        '''
        TODO
        移除事項。如果不存在，則不刪除。
        '''

    @commands.command()
    async def ClearTodoList(self, ctx):
        '''
        TODO
        清空 TodoList。
        '''

    @commands.command()
    async def ShowTodoList(self, ctx):
        if len(self.TodoList) == 0:
            await ctx.send("TodoList 是空的.")
            return

        '''
        TODO
        列印所有事項。
        '''

    def __init__(self, *args):
        super().__init__(*args)
        
        '''
        TODO
        初始化 TodoList.
        '''

async def setup(bot):
    await bot.add_cog(Scheduler(bot))