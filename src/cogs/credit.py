import nextcord
from nextcord.ext import commands

class Credit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='credit')
    async def credit(self, ctx):
        embed=nextcord.Embed(
            title="Information about Jampy",
            description="This bot is a black-smithing bot made for TasosIsDev's 4th BotJam\n\n**Important notice: This bot is not a moderation-based bot, as it was made for thr bot Jam with the team: Blacksmith**",
			color=0x
        )
        embed.add_field(
            name="test",
            value="test"
        )
        embed.add_field(
            name="**test**",
            value="a"
        )
        embed.add_field(
            name="&test*",
            value="a"
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Credit(bot))