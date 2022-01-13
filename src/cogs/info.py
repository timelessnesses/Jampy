import nextcord
from nextcord.ext import commands


class Info(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


@commands.command()
async def help(self, ctx):
		embed=nextcord.Embed(
			title="Bot Commands:",
			description="",
		)



def setup(bot):
    bot.add_cog(Info(bot))