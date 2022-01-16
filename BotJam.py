from dotenv import load_dotenv

load_dotenv()
import os

import nextcord
from nextcord.ext import commands

import keep_alive
from keep_alive import keep_alive

bot = commands.Bot("j!", intents=nextcord.Intents().all())

bot.__emojis = {
    "stone": "931381079489806356",
    "rickroll": "931382810751664158",
    "sword": "931382894239293540",
    "iron": "931383376210964480",
    "diamond": "931384417702772736",
    "gold": "931385164758655007",
    "wood": "931385961605111838",
    "leather": "931386657322700850",
    "bone": "931387021073719316",
}


@bot.event
async def on_ready():
    await bot.change_presence(
        activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="My Tools")
    )
    print("Bot started")


for file in os.listdir("src/cogs"):
    if file.endswith(".py"):
        bot.load_extension("src.cogs." + file[:-3])

keep_alive()  # wait i can reload cogs? yes?
bot.run(os.environ["TOKEN"])
