import nextcord
from nextcord.ext import commands
import dta
import json

class BlackSmith(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    async def initialize(self):
        with open("src/cogs/db/blacksmith.json") as fp:
            db = json.load(fp)
    @commands.command()
    async def swords(self,ctx):
        db = await self.initialize()
        embed = nextcord.Embed(title="Here's the list of the swords!")
        for sword in db["swords"]:
            embed.add_field(name="Sword Name",value=sword["name"],inline=False)
            embed.add_field(name="Cost to make",value=sword["cost"]+"$",inline=False)
            embed.add_field(name="Damage",value=sword["damage"],inline=False)
            embed.add_field(name="Rareness",value=sword["rareness"],inline=False)
            embed.add_field(name="Needed Material",value='\n'.join(sword["material"],inline=False))
        embed.add_field(name="To make a sword, use the command:",value="`!make <sword name>`",inline=False)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def make(self,ctx,*,sword_name):
        db = await self.initialize()
        if sword.lower() not in db["swords"]:
            await ctx.send("That sword doesn't exist!")
        embed = nextcord.Embed(title="You want to make a sword called: "+sword_name,description="Are you sure you want to make this sword? Please check the requirement below.")
        embed.add_field(name="Cost to make",value=db["swords"][sword_name]["cost"],inline=False)
        embed.add_field(name="Damage",value=db["swords"][sword_name]["damage"],inline=False)
        embed.add_field(name="Rareness",value=db["swords"][sword_name]["rareness"],inline=False)
        embed.add_field(name="Needed Material",value='\n'.join(db["swords"][sword_name]["material"],inline=False))
        await 