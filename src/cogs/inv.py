import asyncio
import json

import nextcord
from nextcord.ext import commands


class Inventory(commands.Cog):
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

    @commands.command(aliases=["inv"])
    async def inventory(self, ctx):
        db = await self.initialize()
        b = nextcord.Embed(title="Your Inventory", color=0xFFAA00)
        for x in db[str(ctx.author.id)]["materials"]:
            b.add_field(
                name=x, value=db[str(ctx.author.id)]["materials"][x], inline=False
            )
        await ctx.send(embed=b)
        await self.finalize(db)


def setup(bot):
    bot.add_cog(Inventory(bot))
