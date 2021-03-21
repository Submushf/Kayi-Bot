import discord 
from aiohttp import ClientSession
from discord.ext import commands
import random
from random import choice

class randoms(commands.Cog):

    def __init__(self, client):
        self.client = client 

    @commands.command(aliases = ['person','Who'],description = "guess who game") 
    async def Who(self,ctx):
        gi =  random.choice(ran)

        embed = discord.Embed(title=f"Guess Who?")
        embed.set_image(url=gi)

        await ctx.send(embed = embed)


ran = [
    "https://cdn.discordapp.com/attachments/822698105966821396/822700371826049024/31.png"
    "https://cdn.discordapp.com/attachments/818374423685627907/823042586255294494/images_14.jpeg"
]


def setup(client):
    client.add_cog(randoms(client))