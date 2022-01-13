import nextcord
from nextcord.ext import commands


class Info(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


@commands.command()
async def help(self, ctx):
		embed=nextcord.Embed(
			title="Bot Commands:",
			description="The commands followed are the commands that is built into the Jampy bot",
		)
		embed.add_field(name="Credits", value="See all the people who helped make this bot", inline=True)



def setup(bot):
    bot.add_cog(Info(bot))