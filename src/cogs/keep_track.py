import nextcord
from nextcord.ext import commands
import json
class DBUpdater(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self,message):
        with open("src/cogs/db/db.json") as fp:
            db = json.load(fp)
        if str(message.author.id) not in list(db):
            db[str(message.author.id)] = {"cash":0,"bank":0,"time":{"day":0,"week":0,"month":0,"year":0}}
            with open("src/cogs/db/db.json",'w') as fp:
                json.dump(db,fp,indent=4)

def setup(bot):
    bot.add_cog(DBUpdater(bot))