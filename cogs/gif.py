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

        embed = discord.Embed(color= 0x0F6BE2)
        embed.set_image(url=ertug)

        await ctx.send(embed=embed)


ertugrul = [
    "https://giphy.com/gifs/trt-network-hTCmma89XdaVJQkhDk",
    "https://giphy.com/gifs/trt-network-fight-ertugrul-dirilis-1ziUCYGa3C4IlVJAg4",
    "https://giphy.com/gifs/trt-network-ertugrul-dirilis-3h1gQfJrUX8Q8p6R9K",
    "https://giphy.com/gifs/trt-network-resurrection-ertugrul-1hMdFstxM17s71s0yF",
    "https://giphy.com/gifs/trt-network-ertugrul-dirilis-B36VltfkyCSXzBr3em",
    "https://giphy.com/gifs/trt-network-turkish-trt-resurrection-ertugrul-UrUkgydpeX8wyIMPkC",
    "https://giphy.com/gifs/trt-network-ertugrul-dirilis-5UH3EgiI4zXhmfuoyI",
    "https://giphy.com/gifs/trt-network-brave-courage-ertugrul-836DnpjHWmrDNTVBbw",
    "https://giphy.com/gifs/trt-network-trt-ertugrul-resurrection-JQYcyro5pHoViMmrnc"
]


def setup(client):
    client.add_cog(gif(client))