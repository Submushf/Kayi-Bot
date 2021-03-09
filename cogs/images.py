import discord 
from discord.ext import commands
import asyncio
import random

class images(commands.Cog):

    def __init__(self, client):
        self.client=client 
    
    @commands.command(aliases= ['A'], description = "sends image of aslihan")
    async def aslihan(self,ctx):

        asli = ["pics\Aslihan 1.jpg"]

        asli_image = random.choice(asli)

        await ctx.send(file = discord.File(asli_image)) 

    @commands.command(aliases= ['ba'], description = "sends image of bala")
    async def bala(self,ctx):

        bal = ["pics\Bala 1.jpg", "pics\Bala 2.jpg", "pics\Bala 3.jpg", "pics\Bala 4.jpg", "pics\Bala 5.jpg", "pics\\Bala 6.jpg"]

        bal_image = random.choice(bal)

        await ctx.send(file = discord.File(bal_image)) 

    @commands.command(aliases= ['B'], description = "sends image of bamsi")
    async def bamsi(self,ctx):

        bam = ["pics\Bamsi 1.jpg", "pics\Bamsi 2.jpg", "pics\Bamsi 3.jpg", "pics\Bamsi 4.jpg", "pics\Bamsi 5.jpg", "pics\Bamsi 6.jpg"]

        bam_image = random.choice(bam)

        await ctx.send(file = discord.File(bam_image)) 


def setup(client):
    client.add_cog(images(client))