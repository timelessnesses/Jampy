import discord
from discord.ext import commands
from utility import slash_util as slash

bot = slash.Bot("j!",intents=discord.Intents().all()) 

@bot.event
async def on_ready():
    print("Bot started")