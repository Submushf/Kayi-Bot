import discord 
from aiohttp import ClientSession
from discord.ext import commands
import random

class gif(commands.Cog):

    def __init__(self, client):
        self.client = client 

    
    @commands.command(description = "gives a GIf of ertugrul.") 
    async def ertugrulg(self,ctx):
        ertug =  random.choice(ertugrul)

        embed = discord.Embed(title=f"<:kayi:819796457942155285> Ertugrul Gif",color= 0x0F6BE2)
        embed.set_image(url=ertug)

        await ctx.send(embed=embed)

#------------------------------------------------------------------------------------------------------------

ertugrul = [
    "https://media.giphy.com/media/1hMdFstxM17s71s0yF/giphy.gif",
    "https://media.giphy.com/media/9P1E8mbjhcOH3nCxdW/giphy.gif",
    "https://media.giphy.com/media/hTCmma89XdaVJQkhDk/giphy.gif",
    "https://media.giphy.com/media/1oDuNVG4bFSL8ich6l/giphy.gif",
    "https://media.giphy.com/media/5YucO3kzRw7tReb5tL/giphy.gif",
    "https://media.giphy.com/media/1ziUCYGa3C4IlVJAg4/giphy.gif",
    "https://media.giphy.com/media/fXz4X9c9s1NNBPGLhB/giphy.gif",
    "https://media.giphy.com/media/YPQLlzdqx3R7LnvflM/giphy.gif",
    "https://media.giphy.com/media/UrUkgydpeX8wyIMPkC/giphy.gif",
    "https://media.giphy.com/media/2yrprYMD0Tao0KCn69/giphy.gif",
    "https://media.giphy.com/media/Me7TLPqe7zNu7srsBo/giphy.gif"
]


def setup(client):
    client.add_cog(gif(client))