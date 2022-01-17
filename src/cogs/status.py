import json

import nextcord
from nextcprd.ext import commands


class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def initialize(self):
        with open("/src/cogs/db/db.json") as f:
            db = json.load(f)
        return db

    async def finalize(self, db):
        with open("/src/cogs/db/db.json", "w") as f:
            json.dump(db, f)

    @commands.command()
    async def status(self, ctx, user: nextcord.Member = None):
        db = await self.initialize()
        if user is None:
            user = ctx.author
        health = db[str(user.id)]["health"]
        if health <= 20:
            status_ = "You very injured!"
        elif health <= 50:
            status_ = "You injured!"
        elif health <= 80:
            status_ = "You are okay."
        elif health <= 100:
            status_ = "You are fine."
        else:
            status_ = "You are healthy."
        await ctx.send(
            f"{user.mention}'s status is {status_}. Your health is {health}."
        )
        await self.finalize(db)


def setup(bot):
    bot.add_cog(Status(bot))
