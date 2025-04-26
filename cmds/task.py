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
            await ctx.send("Invalid number of arguments")
            return
        try:
            deadline_object = datetime.datetime.strptime(f'{date} {deadline}', "%Y-%m-%d %H:%M")
        except ValueError as e:
            await ctx.send("Invalid date format")
            return
        
        '''
        TODO
        Add the task to the TodoList.
        If a task with same name exists, do not add it.
        '''

        

    @commands.command()
    async def RemoveTodoList(self, ctx, *args):
        if len(args) != 1:
            await ctx.send("Invalid arguments: Usage: RemoveTodoList <Taskname>")
            return
        
        task_name = args[0]

        '''
        TODO
        Remove the task if it exists. Otherwise, response with not exist.
        '''

    @commands.command()
    async def ClearTodoList(self, ctx):
        '''
        TODO
        Clear the TodoList.
        '''

    @commands.command()
    async def ShowTodoList(self, ctx):
        if len(self.TodoList) == 0:
            await ctx.send("TodoList is empty.")
            return

        '''
        TODO
        Print all the tasks in the TodoList.
        '''

    def __init__(self, *args):
        super().__init__(*args)
        
        '''
        TODO
        Init the TodoList.
        '''

async def setup(bot):
    await bot.add_cog(Scheduler(bot))