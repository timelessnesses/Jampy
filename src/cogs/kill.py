import asyncio
import json
import random

import nextcord
from nextcord.ext import commands


class Kill(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def initialize(self):
        await asyncio.sleep(1)
        with open("src/cogs/db/db.json") as fp:
            db = json.load(fp)
        return db

    async def initialize_sword(self):
        await asyncio.sleep(1)
        with open("src/cogs/db/blacksmith.json") as fp:
            db = json.load(fp)
        return db

    async def finalize(self, db):
        with open("src/cogs/db/db.json", "w") as fp:
            json.dump(db, fp, indent=4)

    async def finalize_sword(self, db):
        with open("src/cogs/db/blacksmith.json", "w") as fp:
            json.dump(db, fp, indent=4)

    @commands.command()
    async def kill(self, ctx, *, user: nextcord.User):
        """
        K I L L
        self-explanatory
        """
        db = await self.initialize()
        swords = await self.initialize_sword()
        if str(user.id) in db:
            if db[str(ctx.author.id)]["using"] == "":
                await ctx.send("You don't have a sword equipped.")
                return
            for sword in swords["swords"]:
                if sword["name"] == db[str(ctx.author.id)]["using"]:
                    chance = random.randint(1, 100)
                    if chance <= 50:
                        db[str(user.id)]["health"] -= sword["damage"]
                        if db[str(user.id)]["health"] <= 0:
                            db[str(user.id)]["health"] = 0
                            await ctx.send(f"You killed {user.mention}.")
                            del db[str(user.id)]
                            await self.finalize(db)
                            return
                        else:
                            await ctx.send(
                                f"You don't really {user.mention} but you injure them. You can attack again."
                            )
                            await self.finalize(db)
                            return
                    else:
                        await ctx.send(
                            f"You miss {user.mention} but you can attack again."
                        )
                        await self.finalize(db)
                        return
        else:
            await ctx.send(
                f"What the actual hell? {user.name} is just a new guy! Leave him alone!"
            )


def setup(bot):
    bot.add_cog(Kill(bot))
