import discord 
from aiohttp import ClientSession
from discord.ext import commands
import random

class gif(commands.Cog):

    def __init__(self, client):
        self.client = client 

    
    @commands.command(description = "gives a GIf of ertugrul.") 
    async def Gertugrul(self,ctx):
        ertug =  random.choice(ertugrul)

        embed = discord.Embed(title=f"<:kayi:819796457942155285> Ertugrul GIF",color= 0x0F6BE2)
        embed.set_image(url=ertug)

        await ctx.send(embed=embed)


ertugrul = [
    "https://giphy.com/gifs/trt-network-hTCmma89XdaVJQkhDk",
    "https://giphy.com/gifs/trt-network-fight-ertugrul-dirilis-1ziUCYGa3C4IlVJAg4",
    "https://giphy.com/gifs/trt-network-ertugrul-dirilis-3h1gQfJrUX8Q8p6R9K",
    "https://giphy.com/gifs/trt-network-resurrection-ertugrul-1hMdFstxM17s71s0yF",
    "https://giphy.com/gifs/trt-network-ertugrul-dirilis-B36VltfkyCSXzBr3em",
    "https://giphy.com/gifs/trt-network-9P1E8mbjhcOH3nCxdW",
    "https://giphy.com/gifs/trt-network-turkish-trt-resurrection-ertugrul-UrUkgydpeX8wyIMPkC",
    "https://giphy.com/gifs/trt-network-ertugrul-dirili-erturul-2jMtgySAUMChemf6aw",
    "https://giphy.com/gifs/trt-network-brave-courage-ertugrul-836DnpjHWmrDNTVBbw",
    "https://giphy.com/gifs/trt-network-turkish-trt-ertugrul-YPQLlzdqx3R7LnvflM",
    "https://giphy.com/gifs/trt-network-trt-ertugrul-resurrection-JQYcyro5pHoViMmrnc",
    "https://giphy.com/gifs/trt-network-bullseye-on-point-target-fXz4X9c9s1NNBPGLhB"
]


def setup(client):
    client.add_cog(gif(client))