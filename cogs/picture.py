import discord 
from aiohttp import ClientSession
from discord.ext import commands
import random

class picture(commands.Cog):

    def __init__(self, client):
        self.client = client 

    @commands.command(description = "gives a picture of the character.") 
    async def ertugrul(self,ctx):
        ertug =  random.choice(ertugrul)

        await ctx.send({ertug})

ertugrul = [
    "https://cdn.discordapp.com/attachments/819129208927420477/819129323646222356/download.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819129327899770910/ertugrul_2.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819129329816567839/ertugrul_4.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819129330407964692/ertugrul_3.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819129331003424838/ertugrul_5.jpg"
]

    @commands.command(description = "gives a picture of the character.") 
    async def bamsi(self,ctx):
        bam =  random.choice(bams)

        await ctx.send({bam})

bams = [
    "https://cdn.discordapp.com/attachments/819129450557472770/819129525954281472/Bamsi_2.jpg",
    "https://cdn.discordapp.com/attachments/819129450557472770/819129525996224532/Bamsi_1.jpg",
    "https://cdn.discordapp.com/attachments/819129450557472770/819129528029937694/Bamsi_3.jpg",
    "https://cdn.discordapp.com/attachments/819129450557472770/819129528948752404/Bamsi_4.jpg",
    "https://cdn.discordapp.com/attachments/819129450557472770/819129530291585044/Bamsi_5.jpg"
]

    @commands.command(description = "gives a picture of the character.") 
    async def osman(self,ctx):
        osma =  random.choice(osm)

        await ctx.send({osma})

osm = [
    "https://cdn.discordapp.com/attachments/819129626601193494/819129734386155530/osman_1.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/819129734939279400/IMG_7336.JPG",
    "https://cdn.discordapp.com/attachments/819129626601193494/819132401341956116/9f7c72322ffe0ef31741544bc35ef6ac.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/819132503334846474/images.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/819132567227858964/images_1.jpg"    
]


def setup(client):
    client.add_cog(picture(client))