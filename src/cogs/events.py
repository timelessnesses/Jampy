import nextcord
from nextcord.ext import commands

class EventListener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("EventListener is loaded.")
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send(embed=nextcord.Embed(title='Error', description='Missing required argument.', color=nextcord.Color.red()))
        elif isinstance(error, commands.BadArgument):
            return await ctx.send(embed=nextcord.Embed(title='Error', description='Bad argument.', color=nextcord.Color.red()))
        elif isinstance(error, commands.CheckFailure):
            return await ctx.send(embed=nextcord.Embed(title='Error', description='You do not have permission to do this.', color=nextcord.Color.red()))
        elif isinstance(error, commands.CommandOnCooldown):
            return await ctx.send(embed=nextcord.Embed(title='Error', description='You are on cooldown.', color=nextcord.Color.red()))
        elif isinstance(error, commands.CommandInvokeError):
            return await ctx.send(embed=nextcord.Embed(title='Error', description='An error occured.', color=nextcord.Color.red()))
        elif isinstance(error, ValueError):
            return await ctx.send(embed=nextcord.Embed(title='Error', description='The ', color=nextcord.Color.red()))
        else:
            return await ctx.send(embed=nextcord.Embed(title='Error', description=f'{type(error).__name__} - {error}', color=nextcord.Color.red()))
