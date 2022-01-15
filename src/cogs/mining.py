import asyncio
import random

import nextcord
from nextcord.ext import commands


class Resources(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def initialize(self):
        with open("src/cogs/db/db.json") as f:
            db = json.load(f)
        return db

    async def finalize(self, db):
        with open("src/cogs/db/db.json", "w") as f:
            json.dump(db, f, indent=4)

    @commands.command()
    async def mine(self, ctx):
        ores = ["Iron", "Diamond", "Gold", "Stone", "Bone"]
        db = await self.initialize()
        a = await ctx.send(embed=discord.Embed(title="Mining...", color=0xFFAA00))
        await asyncio.sleep(5)
        b = discord.Embed(
            title="After 5 hours non-stop mining. Here's what you got!", color=0xFFAA00
        )
        ore = {}
        for x in range(random.randint(1, 5)):
            az = random.choice(ores)
            v = random.randint(1, 20)
            b.add_field(name=az, value=v, inline=False)
            db[str(ctx.author.id)]["material"][az.lower()] += v
        await a.edit(embed=b)
        await self.finalize(db)
