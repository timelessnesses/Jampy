import nextcord
from nextcord.ext import commands

class Credit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='credit')
    async def credit(self, ctx):
        """
        Credits to everyone who contributed to this bot
        """
        embed=nextcord.Embed(
            title="Information about Jampy",
            description="This bot is a Blacksmithing bot made for TasosIsDev's 4th BotJam\n\n**Important notice: This bot is not a moderation-based bot, as it was made for the bot Jam with the theme: Blacksmith**",
			color=0xffaa00
        )
        embed.add_field(
            name="Credits\n\nWho was the bot made by?",
            value="Jampy was made by <@737103938192408637>,(737103938192408637) and <@890913140278181909>, (890913140278181909).",
			inline=False
        )
        embed.add_field(
            name="Icon and PFP",
            value="The PFP orange backround represents heat while the font saying ''JAMPY'' represents IRON Being burnt. the idea was thought by Mooping and was made by Snaky.",
			inline=False
        )
        embed.add_field(
            name="Name",
            value="The bot was going to be named ''Jam.py'' but then Snaky had a better idea to put all letters together.",
			inline=False
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Credit(bot))