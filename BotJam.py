from dotenv import load_dotenv

load_dotenv()
import os

import nextcord
from nextcord.ext import commands

import keep_alive
from keep_alive import keep_alive

bot = commands.Bot("j!", intents=nextcord.Intents().all())


@bot.event
async def on_ready():
    await bot.change_presence(
        activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="My Tools")
    )
    print("Bot started")


for file in os.listdir("src/cogs"):
    if file.endswith(".py"):
        bot.load_extension("src.cogs." + file[:-3])

keep_alive()
bot.run(os.environ["TOKEN"])
