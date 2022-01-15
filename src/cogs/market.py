import asyncio
import json

import nextcord
from nextcord.ext import commands


class Selling(commands.Cog):
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
    async def sell(self, ctx, item, amount):
        db = await self.initialize()
        if db[str(ctx.author.id)]["material"][item.lower()] >= amount:
            db[str(ctx.author.id)]["material"][item.lower()] -= amount
            db[str(ctx.author.id)]["money"] += amount
            await ctx.send(
                embed=nextcord.Embed(
                    title="Successfully sold {} {}(s)".format(amount, item),
                    color=0xFFAA00,
                )
            )
        else:
            await ctx.send(
                embed=nextcord.Embed(
                    title="You don't have enough {}(s)".format(item), color=0xFF0000
                )
            )
        await self.finalize(db)


def setup(bot):
    bot.add_cog(Selling(bot))
