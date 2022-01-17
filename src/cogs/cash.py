import asyncio
import json
import time

import nextcord
from nextcord.ext import commands


def check():
    async def owner(ctx):
        return ctx.author.id in [890913140278181909, 737103938192408637]

    return commands.check(owner)


class Cash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def finalize(self, db):
        """A finalizer for the database

        Keyword arguments:
            db -- Dictionary to dump to file
        Return: None
        """
        with open("src/cogs/db/db.json", "w") as f:
            json.dump(db, f, indent=4)

    async def initialize(self):
        await asyncio.sleep(1)
        """Initializes the database

        Return: Dictionary
        """
        with open("src/cogs/db/db.json") as f:
            db = json.load(f)
        return db

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cash is loaded.")

    @commands.command(aliases=["bal"])
    async def balance(self, ctx, user: nextcord.Member = None):

        """
        Shows the balance of the user.
        If no user is specified, shows the balance of the author.
        """

        cash = await self.initialize()
        if user is None:
            user = ctx.author
        if str(user.id) not in list(cash):
            cash[str(user.id)] = {}
        try:
            bal = cash[str(user.id)]["cash"]
        except KeyError:
            pass
        await ctx.send(
            embed=nextcord.Embed(
                title=f"{user.name}'s balance",
                description=f"Wallet: {bal}$\n",
                color=0xFFAA00,
            )
        )
        await self.finalize(cash)

    @commands.command(aliases=["set"],hidden=True)
    @check()
    async def setbalance(self, ctx, amount: int):
        """
        Sets the balance of the author.
        """
        cash = await self.initialize()
        if str(ctx.author.id) not in list(cash):
            cash[str(ctx.author.id)] = {}
        try:
            cash[str(ctx.author.id)]["cash"] = amount
        except KeyError:
            cash[str(ctx.author.id)]["cash"] = amount
        await ctx.send(
            embed=nextcord.Embed(
                title=f"{ctx.author.name}'s balance",
                description=f'{cash[str(ctx.author.id)]["cash"]}',
                color=0xFFAA00,
            )
        )
        await self.finalize(cash)

    @commands.command()
    async def give(self, ctx, user: nextcord.Member, amount: int):
        """
        Gives the user the specified amount of cash.
        """
        cash = await self.initialize()
        if str(ctx.author.id) not in list(cash):
            cash[str(ctx.author.id)] = {}
        try:
            cash[str(user.id)]["cash"] += amount
            cash[str(ctx.author.id)]["cash"] -= amount
        except KeyError:
            cash[str(user.id)] = {}
            cash[str(user.id)]["cash"] = 0
            cash[str(user.id)]["cash"] += amount
            cash[str(ctx.author.id)]["cash"] -= amount
            print(cash)
        await ctx.send(
            embed=nextcord.Embed(
                title=f"{ctx.author.name}'s balance",
                description=f'{cash[str(ctx.author.id)]["cash"]}',
                color=0xFFAA00,
            )
        )
        await self.finalize(cash)

    @commands.command()
    async def daily(self, ctx):
        """
        Gives the user a daily reward.
        """
        cash = await self.initialize()
        if str(ctx.author.id) not in list(cash):
            cash[str(ctx.author.id)] = {}
        try:
            if cash[str(ctx.author.id)]["time"]["day"] + 86400 > time.time():
                return await ctx.send(
                    embed=nextcord.Embed(
                        title="Error",
                        description="You already claimed your daily.",
                        color=0xFFAA00,
                    )
                )
            cash[str(ctx.author.id)]["cash"] += 1000
            cash[str(ctx.author.id)]["time"]["day"] = time.time()
        except KeyError:
            cash[str(ctx.author.id)]["cash"] = 1000
        await ctx.send(
            embed=nextcord.Embed(
                title=f"{ctx.author.name}'s balance",
                description=f'{cash[str(ctx.author.id)]["cash"]}',
                color=0xFFAA00,
            )
        )
        await self.finalize(cash)

    @commands.command()
    async def weekly(self, ctx):
        """
        Gives the user a weekly reward.
        """
        cash = await self.initialize()
        if str(ctx.author.id) not in list(cash):
            cash[str(ctx.author.id)] = {}
        try:
            if cash[str(ctx.author.id)]["time"]["week"] + 604800 > time.time():
                return await ctx.send(
                    embed=nextcord.Embed(
                        title="Error",
                        description="You already claimed your daily.",
                        color=0xFFAA00,
                    )
                )
            cash[str(ctx.author.id)]["cash"] += 1000
            cash[str(ctx.author.id)]["time"]["week"] = time.time()
        except KeyError:
            cash[str(ctx.author.id)]["cash"] = 1000
        await ctx.send(
            embed=nextcord.Embed(
                title=f"{ctx.author.name}'s balance",
                description=f'{cash[str(ctx.author.id)]["cash"]}',
                color=0xFFAA00,
            )
        )
        await self.finalize(cash)

    @commands.command()
    async def monthly(self, ctx):
        """
        Gives the user a monthly reward.
        """

        cash = await self.initialize()
        if str(ctx.author.id) not in list(cash):
            cash[str(ctx.author.id)] = {}
        try:
            if cash[str(ctx.author.id)]["time"]["month"] + 2629743.83 > time.time():
                return await ctx.send(
                    embed=nextcord.Embed(
                        title="Error",
                        description="You already claimed your daily.",
                        color=0xFFAA00,
                    )
                )
            cash[str(ctx.author.id)]["cash"] += 1000
            cash[str(ctx.author.id)]["time"]["month"] = time.time()
        except KeyError:
            cash[str(ctx.author.id)]["cash"] = 1000
        await ctx.send(
            embed=nextcord.Embed(
                title=f"{ctx.author.name}'s balance",
                description=f'{cash[str(ctx.author.id)]["cash"]}',
                color=0xFFAA00,
            )
        )
        await self.finalize(cash)


def setup(bot):
    bot.add_cog(Cash(bot))
