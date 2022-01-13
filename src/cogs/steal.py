import nextcord
from nextcord.ext import commands
import json
import time
import random
import string

class Make_Robbery_Sin(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
	
	@commands.command()
	async def rob(self,ctx,user:nextcord.Member=None,amount:str=""):
		"""Rob a user"""
		if user == None:
			return await ctx.send("Please specify a user")
		if amount == "":
			return await ctx.send("Please specify an amount")
		with open("src/data/bank.json") as fp:
			db = json.load(fp)
		if str(user.id) not in db:
			db[str(user.id)] = {"money":0,"bank":0,"daily":0,"weekly":0,"monthly":0}
		if str(ctx.author.id) not in db:
			db[str(ctx.author.id)] = {"money":0,"bank":0,"daily":0,"weekly":0,"monthly":0}
		if db[str(user.id)]["bank"] < int(amount):
			return await ctx.send("This user doesn't have enough money to rob")
		if random.choice([True,False]):
			db[str(ctx.author.id)]["money"] += int(amount)
			db[str(user.id)]["money"] -= int(amount)
			with open("src/data/bank.json","w") as fp:
				json.dump(db,fp)
			await ctx.send("You have robbed {} for {} bitties!".format(user.name,amount))
			await user.send("You have been robbed for {} bitties by {}".format(amount,ctx))
		else:
			a = amount + random.randint(500,10000)# the bot isnt online :>
			if (db[str(ctx.author.id)]["money"] - db[str(ctx.author)]) < a:
				db[str(user.id)]["money"] += int(a)
				return await ctx.send("Sadly you don't have enough money to pay the fine. You will be in jail for 2 days!")
			db[str(user.id)]["money"] += int(a)
			db[str(ctx.author.id)]["money"] -= int(a)
			with open("src/data/bank.json","w") as fp:
				json.dump(db,fp)
			await ctx.send("You failed the robbery and lost {} bitties from getting sued.".format(a))
			
def setup(bot):
	bot.add_cog(Make_Robbery_Sin(bot))