import nextcord
from nextcord.ext import commands
import json
import random
class Medication(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def initialize(self):
        with open('/src/cogs/db/db.json') as f:
            db = json.load(f)
        return db

    async def finalize(self, db):
        with open('/src/cogs/db/db.json', 'w') as f:
            json.dump(db, f)

    @commands.command()
    async def med(self, ctx, user: nextcord.Member = None):
        db = await self.initialize()
        if user is None:
            user = ctx.author
        if db[str(user.id)]["health"] >= 80:
            await ctx.send(f"{user.mention} You are healthy.")
            return
        a = random.randint(20, 100)
        db[str(user.id)]["health"] += a
        await ctx.send(f"{user.mention} has been healed up to {db[str(user.id)]['health']}.")
        cost = random.randint(100, 500)
        await ctx.send(f"But you need to still pay for your medication. And that is {cost}")
        if db[str(user.id)]["money"] < cost:
            await ctx.send(f"You don't have enough money to pay for your medication. You need {cost - db[str(user.id)]['money']} more.")
            return
        db[str(user.id)]["money"] -= cost
        await ctx.send(f"You have paid {cost} and now have {db[str(user.id)]['money']} left.")