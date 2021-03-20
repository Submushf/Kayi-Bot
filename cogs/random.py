import discord 
from aiohttp import ClientSession
from discord.ext import commands
import random
from random import choice

class randoms(commands.Cog):

    def __init__(self, client):
        self.client = client 

    @commands.command(aliases = ['random'],description = "gives a random GIf from the series") 
    async def randoms(self,ctx):
        gi =  random.choice(ran)

        embed = discord.Embed(title=f"Random")
        embed.set_image(url=gi)

        await ctx.send(embed = embed)


ran = [
    "https://cdn.discordapp.com/attachments/822698105966821396/822698171242119199/26.jpg",
    "https://cdn.discordapp.com/attachments/822698105966821396/822700358899728445/12.jpg",
    "https://cdn.discordapp.com/attachments/822698105966821396/822700363240964116/21.jpg",
    "https://cdn.discordapp.com/attachments/822698105966821396/822700371826049024/31.png",
    "https://cdn.discordapp.com/attachments/822698105966821396/822700489678389268/Olivia_Black.jpg",
    "https://cdn.discordapp.com/attachments/822698105966821396/822700532471693392/moonlight.jpg"
]


def setup(client):
    client.add_cog(randoms(client))