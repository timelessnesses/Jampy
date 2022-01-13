# How to operate with cogs
Cogs is a seperate of code living in another so code won't just stuck in same file which it make look so messy
## What's the difference of normal and cogs?
Here's the list
- `@client.event` or `@bot.event` will changed to `@commands.Cog.listener()`
- You need to add self in every function you write like
```py
@commands.command()
async def hi (self,ctx):
    await ctx.send("hi")

async def a(self):
    print("hello")

@commands.command()
async def b(self,ctx):
    await a()
```
When call a function ignore the self as argument like if function have only self argument then there's no argument needed.  
This is what will happen if you don't put self in class
```py
class a():
    def b():
        return 'hi'
```
Error:
```py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: b() takes 0 positional arguments but 1 was given
```
- Every time you want to access `client` (or `bot`) you should use `self.client` (or `self.bot`) instead
- You can still use bot as the same
- This is code template that you can use  
Normal:
```py
import nextcord
from .ext import commands

class ClassName(commands.Cog):

    def __init(self,bot): # or client
        self.bot = bot # or client
        # do stuff before bot run

    @commands.Cog.listener()
    async def on_ready(self): # you can change this to any event
        # do something
    
    @commands.command()
    async def command_name(self,ctx, args): # worth know that you can create command same as normal like you normally do
        # do something

def setup(bot): # or client
    bot.add_cog(ClassName(bot))
```
## Example
Normal Cog
```py
import nextcord
from nextcord.ext import commands

class Ping_Pong(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self,message):
        await self.bot.process_commands(message)
        if message.content == "uwu":
            await message.channel.send("owo")
    
    @commands.command()
    async def ping(self,ctx):
        await ctx.send("pong!")
    
    @commands.command()
    async def hi(self,ctx,member):
        await ctx.send(f"hi {member.mention}")
    
def setup(bot):
    bot.add_cog(Ping_Pong(bot))
```
that's it.  
DM me if there's the problem