import asyncio
import json

import nextcord
from nextcord.ext import commands


class Inventory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.emojis = {
            "stone": "931381079489806356",
            "rickroll": "931382810751664158",
            "sword": "931382894239293540",
            "iron": "931383376210964480",
            "diamond": "931384417702772736",
            "gold": "931385164758655007",
            "wood": "931385961605111838",
            "leather": "931386657322700850",
            "bone": "931387021073719316",
        }

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
        """
        I N V E N T O R Y
        self-explanatory
        """
        db = await self.initialize()
        b = nextcord.Embed(title="Your Inventory", color=0xFFAA00)
        for x in db[str(ctx.author.id)]["materials"]:
            if x == "diamond":
                emoji = "<a:diamond:" + self.emojis[x] + "> "
            else:
                emoji = "<:" + x + ":" + self.emojis[x] + "> "
            b.add_field(
                name=emoji + x,
                value=db[str(ctx.author.id)]["materials"][x],
                inline=False,
            )
        await ctx.send(embed=b)
        await self.finalize(db)

    @commands.command()
    async def list_swords(self, ctx):
        """
        List all swords
        Dude: What sword should I use to kill peoples? 🤔
        """
        db = await self.initialize()
        b = nextcord.Embed(title="Swords that you have", color=0xFFAA00)
        for sword in db[str(ctx.author.id)]["swords"]:
            b.add_field(name=sword, value=".", inline=False)
        await ctx.send(embed=b)

    @commands.command()
    async def use_sword(self, ctx, *, sword_name):
        """
        Use a sword
        """
        db = await self.initialize()
        for sword in db[str(ctx.author.id)]["swords"]:
            if sword == sword_name:
                db[str(ctx.author.id)]["using"] = sword
                await ctx.send(f"You are now using {sword}.")
                await self.finalize(db)
                return
        await ctx.send(f"You don't have a {sword_name}.")


def setup(bot):
    bot.add_cog(Inventory(bot))
