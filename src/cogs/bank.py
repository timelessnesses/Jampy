import nextcord
from nextcord.ext import commands
import dta #upm package(dta)
import aiofiles
import json

class Bank(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(aliases=["b","balance","wallet"])
    async def bal(self,ctx,member:nextcord.Member=None):
        if member is None:
            member = ctx.author
        db = json.loads(await open("src/data/bank.json"))

        await ctx.send(embed=nextcord.Embed(title=f"{member.name}'s balance.",description=f"Wallet:  {db[str(member.id)]['money']} $"))

    @commands.command(aliases=["deposit","add","d"])
    async def dep(self,ctx,amount:str=""):
        if amount == "":
            return await ctx.send("Please specify an amount")
        db = json.loads(await open("src/data/bank.json"))
        if str(ctx.author.id) not in db:
            db[str(ctx.author.id)] = {"money":0,"bank":0,"daily":0,"weekly":0,"monthly":0}
        db[str(ctx.author.id)]["bank"] += int(amount)
        with open("src/data/bank.json","w") as fp:
            json.dump(db,fp)
        await ctx.send(f"You have deposited {amount} $")
    
    @commands.command(aliases=["withdraw","remove","r"])
    async def wd(self,ctx,amount:str=""):
        if amount == "":
            return await ctx.send("Please specify an amount")
        db = json.loads(await open("src/data/bank.json"))
        if str(ctx.author.id) not in db:
            db[str(ctx.author.id)] = {"money":0,"bank":0,"daily":0,"weekly":0,"monthly":0}
        if db[str(ctx.author.id)]["bank"] < int(amount):
            return await ctx.send("You don't have enough money")
        db[str(ctx.author.id)]["bank"] -= int(amount)
        db[str(ctx.author.id)]["money"] += int(amount)
        with open("src/data/bank.json","w") as fp:
            json.dump(db,fp)
        await ctx.send(f"You have withdrawn {amount} $")

def setup(bot):
    bot.add_cog(Bank(bot))