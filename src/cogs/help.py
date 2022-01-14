import nextcord
from nextcord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('help')

    @commands.command(name='help')
    async def help(self, ctx, *, command: str = None):
        """Shows help about a command or the bot"""
        embed = nextcord.Embed(title='Help', description='', color=nextcord.Color.blue())
        for command in self.bot.commands:
            if command.hidden:
                continue
            if command.aliases:
                aliases = ' | '.join(command.aliases)
                embed.add_field(name=f'{command.name} | {aliases}', value=command.help, inline=true)
            else:
                embed.add_field(name=command.name, value=command.help, inline=true)

def setup(bot):
    bot.add_cog(Help(bot))