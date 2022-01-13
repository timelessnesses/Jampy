import nextcord
from nextcord.ext import commands
import json
import time
from datetime import datetime
class MoneyManagement(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
	
	@commands.command()
	async def daily(self,ctx):
		"""Gives you your daily money"""
		with open("src/data/bank.json") as fp:
			db = json.load(fp)
		if str(ctx.author.id) not in db:
			db[str(ctx.author.id)] = {"money":0,"bank":0,"daily":0,"weekly":0,"monthly":0}
		if db[str(ctx.author.id)]["daily"]+86400 > time.time():
			return await ctx.send("You have already claimed your daily money")
		db[str(ctx.author.id)]["money"] += 5000
		db[str(ctx.author.id)]["daily"] = time.time()
		with open("src/data/bank.json","w") as fp:
			json.dump(db,fp)
		await ctx.send("You have claimed your 5000 bitties!")
	
	@commands.command()
	async def weekly(self,ctx):
		"""Gives you your weekly money"""
		with open("src/data/bank.json") as fp:
			db = json.load(fp)
		if str(ctx.author.id) not in db:
			db[str(ctx.author.id)] = {"money":0,"bank":0,"daily":0,"weekly":0,"monthly":0}
		if db[str(ctx.author.id)]["weekly"]+604800 > time.time():
			return await ctx.send("You have already claimed your weekly money")
		db[str(ctx.author.id)]["money"] += 1000000
		db[str(ctx.author.id)]["weekly"] = time.time()
		with open("src/data/bank.json","w") as fp:
			json.dump(db,fp)
		await ctx.send("You have claimed your 1000000 bitties!")
	
	@commands.command()
	async def monthly(self,ctx):
		"""Gives you your monthly money"""
		with open("src/data/bank.json") as fp:
			db = json.load(fp)
		if str(ctx.author.id) not in db:
			db[str(ctx.author.id)] = {"money":0,"bank":0,"daily":0,"weekly":0,"monthly":0}
		if db[str(ctx.author.id)]["monthly"]+2592000 > time.time():
			return await ctx.send("You have already claimed your monthly money")
		db[str(ctx.author.id)]["money"] += 1000000000
		db[str(ctx.author.id)]["monthly"] = time.time()
		with open("src/data/bank.json","w") as fp:
			json.dump(db,fp)
		await ctx.send("You have claimed your 1000000000 bitties!")
	
	@commands.command()
	async def give(self,ctx,user:nextcord.Member=None,amount:str=""):
		"""Gives money to a user"""
		if user == None:
			return await ctx.send("Please specify a user")
		if amount == "":
			return await ctx.send("Please specify an amount")
		try:
			amount = int(amount)
		except ValueError:
			return await ctx.send("Amount must be a number")
		if amount <= 0:
			return await ctx.send("Amount must be greater than 0")
		with open("src/data/bank.json") as fp:
			db = json.load(fp)
		if str(user.id) not in db:
			db[str(user.id)] = {"money":0,"bank":0,"daily":0,"weekly":0,"monthly":0}
		if db[str(ctx.author.id)]["money"] < amount:
			return await ctx.send("You don't have enough money")
		db[str(ctx.author.id)]["money"] -= amount
		db[str(user.id)]["money"] += amount
		with open("src/data/bank.json","w") as fp:
			json.dump(db,fp)
		await ctx.send("You have given {} bitties to {}".format(amount,user.mention))

def setup(bot):
	bot.add_cog(MoneyManagement(bot))