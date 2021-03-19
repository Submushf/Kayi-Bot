import discord 
from aiohttp import ClientSession
from discord.ext import commands
import random

class gif(commands.Cog):

    def __init__(self, client):
        self.client = client 

    
    @commands.command(description = "gives a random GIf from the series") 
    async def gif(self,ctx):
        gi =  random.choice(gifs)

#        embed = discord.Embed(title=f"<:kayi:819796457942155285> Gif",color= 0x0F6BE2)
#        embed.set_image(url=gi)

        await ctx.send(gi)

#------------------------------------------------------------------------------------------------------------

gifs = [
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
    "https://media.giphy.com/media/Me7TLPqe7zNu7srsBo/giphy.gif",
    "https://cdn.discordapp.com/attachments/820496784781606932/820527270434570300/gif_temp.gif",
    "https://cdn.discordapp.com/attachments/820496784781606932/820527351178854420/gif_temp.gif",
    "https://giphy.com/gifs/trt-network-ertugrul-dirilis-turkishdrama-MDsmaNZL19ws9HHxa3",
    "https://giphy.com/gifs/trt-network-trt-ertugrul-video-call-UqRevvabMWsXIbQf6h",
    "https://cdn.discordapp.com/attachments/820521610250944542/820523068949659678/QTCFfgT2dww9oOtxW3.gif",
    "https://giphy.com/gifs/trt-network-trt-ertugrul-resurrection-StdfZEtECDCI38Ipc6",
    "https://cdn.discordapp.com/attachments/820521610250944542/820523960990040114/lPjEfc21fGy2eQoJOv.gif",
    "https://cdn.discordapp.com/attachments/820521610250944542/820524429196001300/Id1NYlbgCPtwRUe0tL.gif",
    "https://giphy.com/gifs/trt-network-turkish-dirilis-resurrection-ertugrul-VgrKQZ3sQl8v0izEnC",
    "https://giphy.com/gifs/trt-network-ertugrul-dirilis-dirilisertugrul-kz0GUVisyRBp7KzW9B",
    "https://giphy.com/gifs/trt-network-fight-dead-acting-geEVZZ0UZOwxzS1nLP",
    "https://giphy.com/gifs/trt-network-cry-pain-weep-VDA5Xvkg1ZWPTCoWld",
    "https://giphy.com/gifs/trt-network-slap-revenge-old-man-jVBHUatovBURllqnJp",
    "https://giphy.com/gifs/trt-network-dirilis-eyvallah-suleymanshah-SXUXHb7oKi8tyxghxs",
    "https://giphy.com/gifs/trt-network-9P1E8mbjhcOH3nCxdW",
    "https://giphy.com/gifs/trt-network-fight-battle-sword-XbJN1Pupcii3c2LCUT",
    "https://giphy.com/gifs/trt-network-fire-flame-bonfire-l28qr0dkMxmaIrmvr4",
    "https://giphy.com/gifs/trt-network-hunger-dirilis-familydinner-ftGsJG0fXuJM9Xtq3A",
    "https://cdn.discordapp.com/attachments/820496784781606932/820534873307086848/tumblr_30cd1dc10d62a582cd93a0dcf612e864_6944638c_400.gif",
    "https://tenor.com/view/wakanda-forever-bala-osman-kurulus-osman-wakanda-gif-20747621" 
]


def setup(client):
    client.add_cog(gif(client))