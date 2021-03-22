import discord 
from aiohttp import ClientSession
from discord.ext import commands
import random
from random import choice

class randoms(commands.Cog):

    def __init__(self, client):
        self.client = client 

    @commands.command(aliases = ['person'],description = "guess who game") 
    async def Who(self,ctx):
        gi =  random.choice(ran)

        embed = discord.Embed(title=f"Guess Who?")
        embed.set_image(url=gi)

        await ctx.send(embed = embed)


ran = [
    "https://cdn.discordapp.com/attachments/822698105966821396/822700371826049024/31.png",
    "https://cdn.discordapp.com/attachments/818374423685627907/823042586255294494/images_14.jpeg",
    "https://cdn.discordapp.com/attachments/822698105966821396/823127693448183818/burcu_ozberk_askimmm.jpg",
    #---------------------------------boys-------------------------------------------------------
    "https://cdn.discordapp.com/attachments/822698105966821396/823127728193798164/chrishemsworth___Tumblr.jpg",
    "https://cdn.discordapp.com/attachments/822698105966821396/823127730174164992/Robert_Downey_Jr__Photostream.jpg",
    "https://cdn.discordapp.com/attachments/822698105966821396/823357757406445588/16163741715949171309586120113554.jpg",
    "https://cdn.discordapp.com/attachments/822698105966821396/823358118725419058/16163742580345388427248952105711.jpg",
    "https://cdn.discordapp.com/attachments/822698105966821396/823357494872506368/16163741208138319921527181123948.jpg"
]


def setup(client):
    client.add_cog(randoms(client))