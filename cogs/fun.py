import discord 
from discord.ext import commands
import random

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client 

    @commands.command(aliases=['p'],description = "Pat a user with a Gif")
    async def pat(self, ctx):
        embed = discord.Embed(color = 0x07C9F5 )
        embed.set_image(url= 'https://media.giphy.com/media/5tmRHwTlHAA9WkVxTU/giphy.gif')
        await ctx.send(embed=embed)

    @commands.command(aliases=['co'],description = "congratulate a user with a Gif")
    async def congrats(self, ctx,*,message):
        embed = discord.Embed(color = 0x07C9F5)
        embed.add_field(name="Congrats", value=f"{message}")
        embed.set_image(url= 'https://media.giphy.com/media/g9582DNuQppxC/giphy.gif')
        await ctx.send(embed=embed)

    @commands.command(aliases=['ki'], description = "Kick a user with a Gif")
    async def Kick(self, ctx):
        embed = discord.Embed(color = 0x07C9F5)
        embed.set_image(url= 'https://media.giphy.com/media/u2LJ0n4lx6jF6/giphy.gif')
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Fun(client))