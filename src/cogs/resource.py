import asyncio
import json
import random

import nextcord
from nextcord.ext import commands


class Resources(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def initialize(self):
        await asyncio.sleep(1)
        with open("src/cogs/db/db.json") as f:
            db = json.load(f)
        return db

    async def finalize(self, db):
        with open("src/cogs/db/db.json", "w") as f:
            json.dump(db, f, indent=4)

    @commands.command()
    async def mine(self, ctx):
        """
                Minin' away
        I don't know what to mine
        I'll mine this anyway
        In this Minecraft day"""
        ores = ["Iron", "Diamond", "Gold", "Stone", "Bone"]
        db = await self.initialize()
        a = await ctx.send(embed=nextcord.Embed(title="Mining...", color=0xFFAA00))
        await asyncio.sleep(5)
        b = nextcord.Embed(
            title="After 5 hours non-stop mining. Here's what you got!", color=0xFFAA00
        )
        cache = ""
        for x in range(random.randint(1, 5)):
            az = random.choice(ores)
            if az == cache:
                az = random.choice(ores)
            else:
                cache = az
            v = random.randint(1, 20)
            b.add_field(name=az, value=v, inline=False)
            db[str(ctx.author.id)]["materials"][az.lower()] += v
        await a.edit(embed=b)
        await self.finalize(db)

    @commands.command()
    async def cut_wood(self, ctx):
        """
        Pop quiz: Will Mr.Beast hunt your ass down because of you cutting the tree?
        """
        db = await self.initialize()
        a = await ctx.send(
            embed=nextcord.Embed(
                title="Destroying Nature Enviroment...", color=0xFFAA00
            )
        )
        await asyncio.sleep(5)
        b = nextcord.Embed(
            title="After 5 hours non-stop of cutting trees. Here's what you got!",
            color=0xFFAA00,
        )
        v = random.randint(1, 20)
        db[str(ctx.author.id)]["materials"]["wood"] += v
        b.add_field(name="Wood", value=v, inline=False)
        b.set_footer(text="Mr. Beast will now hunt your ass.")
        await a.edit(embed=b)
        await self.finalize(db)

    @commands.command()
    async def hunt_leather(self, ctx):
        db = await self.initialize()
        a = await ctx.send(embed=nextcord.Embed(title="Hunting...", color=0xFFAA00))
        await asyncio.sleep(5)
        b = nextcord.Embed(
            title="After 5 hours non-stop hunting. Here's what you got!", color=0xFFAA00
        )
        v = random.randint(1, 20)
        db[str(ctx.author.id)]["materials"]["leather"] += v
        b.add_field(name="Leather", value=v, inline=False)
        await a.edit(embed=b)
        await self.finalize(db)

    @commands.command()
    async def hunt_bone(self, ctx):
        db = await self.initialize()
        a = await ctx.send(embed=nextcord.Embed(title="Hunting...", color=0xFFAA00))
        await asyncio.sleep(5)
        b = nextcord.Embed(
            title="After 5 hours non-stop hunting. Here's what you got!", color=0xFFAA00
        )
        v = random.randint(1, 20)
        db[str(ctx.author.id)]["materials"]["bone"] += v
        b.add_field(name="Bone", value=v, inline=False)
        await a.edit(embed=b)
        await self.finalize(db)


def setup(bot):
    bot.add_cog(Resources(bot))
