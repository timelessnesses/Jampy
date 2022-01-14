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
        return db
    async def initialize_user(self):
        with open("src/cogs/db/db.json") as fp:
            db = json.load(fp)
        return db
    async def finalize(self,db):
        with open("src/cogs/db/blacksmith.json","w") as fp:
            json.dump(db,fp)
    async def finalize_user(self,db):
        with open("src/cogs/db/db.json","w") as fp:
            json.dump(db,fp)
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
        user = await self.initialize_user()
        if sword.lower() not in db["swords"]:
            await ctx.send("That sword doesn't exist!")
        embed = nextcord.Embed(title="You want to make a sword called: "+sword_name,description="Are you sure you want to make this sword? Please check the requirement below.")
        embed.add_field(name="Cost to make",value=db["swords"][sword_name]["cost"],inline=False)
        embed.add_field(name="Damage",value=db["swords"][sword_name]["damage"],inline=False)
        embed.add_field(name="Rareness",value=db["swords"][sword_name]["rareness"],inline=False)
        embed.add_field(name="Needed Material",value='\n'.join(db["swords"][sword_name]["material"],inline=False))
        require = await ctx.send(embed=embed)
        another = discord.Embed(title="Here's what you have.")
        another.add_field(name="Money",value=user[str(ctx.author.id)]["money"],inline=False)
        another.add_field(name="Iron",value=user[str(ctx.author.id)]["materials"]["iron"],inline=False)
        another.add_field(name="Gold",value=user[str(ctx.author.id)]["materials"]["gold"],inline=False)
        another.add_field(name="Diamond",value=user[str(ctx.author.id)]["materials"]["diamond"],inline=False)
        another.add_field(name="Stone",value=user[str(ctx.author.id)]["materials"]["stone"],inline=False)
        another.add_field(name="Wood",value=user[str(ctx.author.id)]["materials"]["wood"],inline=False)
        another.add_field(name="Leather",value=user[str(ctx.author.id)]["materials"]["leather"],inline=False)
        another.add_field(name="Bone",value=user[str(ctx.author.id)]["materials"]["bone"],inline=False)
        await ctx.send(embed=another)
        await ctx.send("Please type `yes` to confirm.")
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        try:
            msg = await self.bot.wait_for('message',check=check,timeout=30)
        except asyncio.TimeoutError:
            await ctx.send("You didn't respond in time. Cancelling.")
            return# oi
        materials = []
        if msg.content.lower() == "yes":
            if user[str(ctx.author.id)]["money"] >= db["swords"][sword_name]["cost"]:
                user[str(ctx.author.id)]["money"] -= db["swords"][sword_name]["cost"]
                for material in db["swords"][sword_name]["material"]:
                    if material == "iron":
                        if user[str(ctx.author.id)]["materials"]["iron"] >= db["swords"][sword_name]["material"][material]:
                            user[str(ctx.author.id)]["materials"]["iron"] -= db["swords"][sword_name]["material"][material]
                            materials.append(material)
                        else:
                            await ctx.send("You don't have enough iron!")
                            return
                    if material == "gold":
                        if user[str(ctx.author.id)]["materials"]["gold"] >= db["swords"][sword_name]["material"][material]:
                            user[str(ctx.author.id)]["materials"]["gold"] -= db["swords"][sword_name]["material"][material]
                            
                            materials.append(material)
                        else:
                            await ctx.send("You don't have enough gold!")
                            return
                    if material == "diamond":
                        if user[str(ctx.author.id)]["materials"]["diamond"] >= db["swords"][sword_name]["material"][material]:
                            user[str(ctx.author.id)]["materials"]["diamond"] -= db["swords"][sword_name]["material"][material]
                            
                            materials.append(material)
                        else:
                            await ctx.send("You don't have enough diamond!")
                            return
                    if material == "stone":
                        if user[str(ctx.author.id)]["materials"]["stone"] >= db["swords"][sword_name]["material"][material]:
                            user[str(ctx.author.id)]["materials"]["stone"] -= db["swords"][sword_name]["material"][material]
                            
                            materials.append(material)
                        else:
                            await ctx.send("You don't have enough stone!")
                            return
                    if material == "wood":
                        if user[str(ctx.author.id)]["materials"]["wood"] >= db["swords"][sword_name]["material"][material]:
                            user[str(ctx.author.id)]["materials"]["wood"] -= db["swords"][sword_name]["material"][material]
                            
                            materials.append(material)
                        else:
                            await ctx.send("You don't have enough wood!")
                            return
                    if material == "leather":
                        if user[str(ctx.author.id)]["materials"]["leather"] >= db["swords"][sword_name]["material"][material]:
                            user[str(ctx.author.id)]["materials"]["leather"] -= db["swords"][sword_name]["material"][material]
                            
                            materials.append(material)
                        else:
                            await ctx.send("You don't have enough leather!")
                            return
                    if material == "bone":
                        if user[str(ctx.author.id)]["materials"]["bone"] >= db["swords"][sword_name]["material"][material]:
                            user[str(ctx.author.id)]["materials"]["bone"] -= db["swords"][sword_name]["material"][material]
                            
                            materials.append(material)
                        else:
                            await ctx.send("You don't have enough bone!")
                            return
                if len(materials) == len(db["swords"][sword_name]["material"]):
                    user[str(ctx.author.id)]["swords"][sword_name] = db["swords"][sword_name]
                    await ctx.send("You have made a {}!".format(sword_name))
            else:
                await ctx.send("You don't have enough money!")
                return
                        
    
