import os

import nextcord
from nextcord.ext import commands


def check():
    async def owner(ctx):
        return ctx.author.id in [890913140278181909, 737103938192408637]

    return commands.check(owner)


class CogsManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("CogsManagement is loaded.")

    @commands.command(hidden=True)
    @check()
    async def load(self, ctx, *, cog: str):
        """
        Loads a cog.
        """
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")
        else:
            await ctx.send(f"**`SUCCESS`**")

    @commands.command(hidden=True)
    @check()
    async def unload(self, ctx, *, cog: str):
        """
        Unloads a cog.
        """
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")
        else:
            await ctx.send(f"**`SUCCESS`**")

    @commands.command(hidden=True)
    @check()
    async def reload(self, ctx, *, cog: str):
        """
        Reloads a cog.
        """
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")
        else:
            await ctx.send(f"**`SUCCESS`**")

    @commands.command(hidden=True)
    @check()
    async def reloadall(self, ctx):
        """
        Reloads all cogs.
        """
        for cog in os.listdir("./src/cogs"):
            if cog == "cogs_management.py":
                continue
            if ".py" not in cog:
                continue
            try:
                self.bot.unload_extension("src.cogs." + cog[:-3])
                self.bot.load_extension("src.cogs." + cog[:-3])
            except Exception as e:
                await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")
            else:
                await ctx.send(f"**`SUCCESS`**")
    
    @commands.command(hidden=True)
    @check()
    async def emojis(self,ctx):
        embed = nextcord.Embed(title="Here's the list of emojis")
        for emoji in ctx.guild.emojis:
            embed.add_field(name=emoji.name,value=emoji.id)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(CogsManagement(bot))
