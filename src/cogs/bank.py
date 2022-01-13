import nextcord
from nextcord.ext import commands
import dta #upm package(dta)
import aiofiles
import json
from src.data.util import open

class Bank(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(aliases=["b","balance","wallet"])
    async def bal(self,ctx,member:nextcord.Member=None):
        if member is None:
            member = ctx.author
        db = json.loads(await open("src/data/bank.json"))

        await ctx.send(embed=nextcord.Embed(title=f"{member.name}'s balance.",description=f"Wallet:  {db[str(member.id)]['money']} $"))   

def setup(bot):
    bot.add_cog(Bank(bot))