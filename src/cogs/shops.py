import asyncio
import json

import nextcord
from nextcord.ext import commands


class BlackSmith(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def initialize(self):
        await asyncio.sleep(1)
        with open("src/cogs/db/blacksmith.json") as fp:
            db = json.load(fp)
        return db

    async def initialize_user(self):
        await asyncio.sleep(1)
        with open("src/cogs/db/db.json") as fp:
            db = json.load(fp)
        return db

    async def finalize(self, db):
        with open("src/cogs/db/blacksmith.json", "w") as fp:
            json.dump(db, fp)

    async def finalize_user(self, db):
        with open("src/cogs/db/db.json", "w") as fp:
            json.dump(db, fp)

    @commands.command()
    async def swords(self, ctx):
        """
        Shows all swords
        """
        db = await self.initialize()
        embed = nextcord.Embed(title="Here's the list of the swords!", color=0xFFAA00)
        for sword in db["swords"]:
            embed.add_field(name="Sword Name", value=sword["name"], inline=False)
            embed.add_field(
                name="Cost to make", value=int(sword["cost"]) + "$", inline=False
            )
            embed.add_field(name="Damage", value=sword["damage"], inline=False)
            embed.add_field(name="Rareness", value=sword["rareness"], inline=False)
            embed.add_field(
                name="Needed Material", value="\n".join(sword["material"]), inline=False
            )
        embed.add_field(
            name="To make a sword, use the command:",
            value="`!make <sword name>`",
            inline=False,
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def make(self, ctx, *, sword_name):
        """
        Makes a sword
        """
        db = await self.initialize()
        user = await self.initialize_user()
        for sword in db["swords"]:
            if sword["name"] == sword_name:
                break
            else:
                sword = None
        if sword is None:
            return await ctx.send("That sword doesn't exist!")
        embed = nextcord.Embed(
            title="You want to make a sword called: " + sword_name,
            description="Are you sure you want to make this sword? Please check the requirement below.",
            color=0xFFAA00,
        )
        embed.add_field(
            name="Cost to make",
            value=int(sword["cost"]),  # dms
            inline=False,
        )
        embed.add_field(name="Damage", value=sword["damage"], inline=False)
        embed.add_field(name="Rareness", value=sword["rareness"], inline=False)
        embed.add_field(
            name="Needed Material",
            value="\n".join(
                sword["material"],
            ),
            inline=False,
        )
        require = await ctx.send(embed=embed)
        another = nextcord.Embed(title="Here's what you have.", color=0xFFAA00)
        another.add_field(
            name="cash", value=user[str(ctx.author.id)]["cash"], inline=False
        )
        another.add_field(
            name="Iron",
            value=user[str(ctx.author.id)]["materials"]["iron"],
            inline=False,
        )
        another.add_field(
            name="Gold",
            value=user[str(ctx.author.id)]["materials"]["gold"],
            inline=False,
        )
        another.add_field(
            name="Diamond",
            value=user[str(ctx.author.id)]["materials"]["diamond"],
            inline=False,
        )
        another.add_field(
            name="Stone",
            value=user[str(ctx.author.id)]["materials"]["stone"],
            inline=False,
        )
        another.add_field(
            name="Wood",
            value=user[str(ctx.author.id)]["materials"]["wood"],
            inline=False,
        )
        another.add_field(
            name="Leather",
            value=user[str(ctx.author.id)]["materials"]["leather"],
            inline=False,
        )
        another.add_field(
            name="Bone",
            value=user[str(ctx.author.id)]["materials"]["bone"],
            inline=False,
        )
        await ctx.send(embed=another)
        await ctx.send("Please type `yes` to confirm.")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            msg = await self.bot.wait_for("message", check=check, timeout=30)
        except asyncio.TimeoutError:
            await ctx.send("You didn't respond in time. Cancelling.")
            return  # :)
        materials = []
        if msg.content.lower() == "yes":
            for material in sword["material"]:
                materials.append(material)
            for material in materials:
                if user[str(ctx.author.id)]["materials"][material] < 1:
                    return await ctx.send("You don't have enough materials!")
                else:
                    user[str(ctx.author.id)]["materials"][material] -= 1
            
            if user[str(ctx.author.id)]["cash"] < int(sword["cost"]):
                return await ctx.send("You don't have enough money!")
            user[str(ctx.author.id)]["cash"] -= int(sword["cost"])
            user[str(ctx.author.id)]["swords"].append(sword["name"])
            await self.finalize_user(user)
            await ctx.send("You made a " + sword["name"] + "!")


def setup(bot):
    bot.add_cog(BlackSmith(bot))
