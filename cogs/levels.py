import discord 
from discord.ext import commands
import json

class Leveling(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_message(self, message, member):
        with open('users.json', 'r',encoding="utf8") as f:
            user = json.load(f)
        try:
            with open('users.json', 'w',encoding="utf8") as f:
                user[str(message.author.id)]['exp'] = user[str(message.author.id)]['exp']+1
                lvl_start = user[str(message.author.id)]['level']
                lvl_end = user[str(message.author.id)]['exp'] ** (1.5/40)
                if lvl_start < lvl_end:
                    user[str(message.author.id)]['level'] = user[str(message.author.id)]['level']+1
                    lvl = user[str(message.author.id)]['level']
                    await message.channel.send(f"🏆 Oh, {member.mention} has leveled up to {lvl}") 
                    json.dump(user,f, sort_keys=True, indent=4, ensure_ascii=False)
                    return
                json.dump(user,f, sort_keys=True, indent=4, ensure_ascii=False)

        except:
            with open('users.json', 'w',encoding="utf8") as f:
                user = {}
                user[str(message.author.id)] = {}
                user[str(message.author.id)]['level'] = 0
                user[str(message.author.id)]['xp'] = 0
                json.dump(user,f,sort_keys=True, indent=4, ensure_ascii=False)


def setup(bot):
    bot.add_cog(Leveling(bot))