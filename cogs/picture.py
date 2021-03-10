import discord 
from aiohttp import ClientSession
from discord.ext import commands
import random

class other(commands.Cog):

    def __init__(self, client):
        self.client = client 

#----------------------------------------------------------------------------------------------------------------

    @commands.command(description = "gives a info of osman.") 
    async def osman(self,ctx):
        osma =  random.choice(osm)

        embed = discord.Embed(color= 0x0F6BE2)
        embed.add_field(name="Osman", value=f"Osman I was the founder of the Ottoman empire.")
        embed.set_image(url=osma)

        await ctx.send(embed=embed)


    @commands.command(description = "gives a info of bamsi.") 
    async def bamsi(self,ctx):
        bam =  random.choice(bams)

        embed = discord.Embed(color= 0x0F6BE2)
        embed.add_field(name="bamsi", value=f"`bamsi` is a close ally of ertugrul and fought in his side until he died.")
        embed.set_image(url=bam)

        await ctx.send(embed=embed)

    @commands.command(description = "gives a info of ertugrul.") 
    async def ertugrul(self,ctx):
        ertug =  random.choice(ertugrul)

        embed = discord.Embed(color= 0x0F6BE2)
        embed.add_field(name="Ertugrul", value=f"`Ertuğrul Gazi` was the father of Osman I who would ultimately found of the Ottoman empire.")
        embed.set_image(url=ertug)

        await ctx.send(embed=embed)

    @commands.command(description = "gives info of ibn_arabi.") 
    async def ibn_arabi(self,ctx):
        ibn =  random.choice(arabi)

        embed = discord.Embed(color= 0x0F6BE2)
        embed.add_field(name="Ibn Arabi", value=f"`Ibn Arabi` was Andalusian Muslim scholar, mystic, poet, and philosopher, extremely influential within Islamic thought.")
        embed.set_image(url=ibn)

        await ctx.send(embed=embed)

    @commands.command(description = "gives a info of bala.") 
    async def bala(self,ctx):
        bal =  random.choice(bala)

        embed = discord.Embed(color= 0x0F6BE2)
        embed.add_field(name="Bala", value=f"`Bala Hatun` was the first wife of Ottoman Sultan Osman I. She was the daughter of the famous Sheikh Edebali.")
        embed.set_image(url=bal)

        await ctx.send(embed=embed)

    @commands.command(description = "gives a info of turgut.") 
    async def turgut(self,ctx):
        tur =  random.choice(turgut)
        
        embed = discord.Embed(color = 0x0F6BE2)
        embed.add_field(name="Turgut", value=f"`Turgut Alp` was one of the warriors and alps who fought for Ertuğrul, a Turkic leader and bey, and Ertuğrul's son Osman I, the founder of the Ottoman Empire.")
        embed.set_image(url=tur)

        await ctx.send(embed=embed) 

    @commands.command(description = "gives a info of selcan.") 
    async def selcan(self,ctx):
        sel =  random.choice(selcan)

        embed = discord.Embed(color=0x0F6BE2)
        embed.add_field(name="Selcan", value="Selcan Hatun is the wife of Gündoğdu, elder sister of Gökçe, who she loves dearly, and the mother of Süleyman Alp.")
        embed.set_image(url= sel) 
        await ctx.send(embed = embed )

#----------------------------------------------------------------------------------------------------------------------------

selcan = [
    "https://cdn.discordapp.com/attachments/819152142933032980/819152213359329280/images.jpg",
    "https://cdn.discordapp.com/attachments/819152142933032980/819152210553339914/images_1.jpg",
    "https://cdn.discordapp.com/attachments/819152142933032980/819152209110761492/f96b139ebadbcb1b9247c7fc05d32c83.jpg",
    "https://cdn.discordapp.com/attachments/819152142933032980/819152208217112576/download.jpg"
]

turgut = [
    "https://cdn.discordapp.com/attachments/819149935097151498/819149985626193930/images_1.jpg",
    "https://cdn.discordapp.com/attachments/819149935097151498/819149986482356274/images_2.jpg",
    "https://cdn.discordapp.com/attachments/819149935097151498/819149988398891028/images_3.jpg",
    "https://cdn.discordapp.com/attachments/819149935097151498/819149989694930944/images_4.jpg",
    "https://cdn.discordapp.com/attachments/819149935097151498/819149990625542154/images.jpg",
    "https://cdn.discordapp.com/attachments/819149935097151498/819149993105424384/turgut.jpg"
]

bala = [
    "https://cdn.discordapp.com/attachments/819129568824000523/819129601754005515/9f8cacd7-e10c-40ce-ad4f-4697cc2ad5a3.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/819147594570792960/b2a1b8485d9b43e34b3ccd9a28300f2e.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/819147594554277898/0749c9865973db3014cdd0a7dfee482d.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/819147597485834240/crop.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/819147598836269076/e3b8ee559f3780622332c44ea53caf9f.jpg"
]

arabi = [
    "https://cdn.discordapp.com/attachments/819129798210617384/819129855446745117/Ibn_2.jpg",
    "https://cdn.discordapp.com/attachments/819129798210617384/819129857060372480/Ibn_1.jpg",
    "https://cdn.discordapp.com/attachments/819129798210617384/819129858230583296/Ibn_3.jpg",
    "https://cdn.discordapp.com/attachments/819129798210617384/819129860911661076/Ibn_4.jpg",
    "https://cdn.discordapp.com/attachments/819129798210617384/819129866225451008/Ibn_6.jpg",
    "https://cdn.discordapp.com/attachments/819129798210617384/819129863168065550/Ibn_5.png"
]

osm = [
    "https://cdn.discordapp.com/attachments/819129626601193494/819129734386155530/osman_1.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/819129734939279400/IMG_7336.JPG",
    "https://cdn.discordapp.com/attachments/819129626601193494/819132401341956116/9f7c72322ffe0ef31741544bc35ef6ac.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/819132503334846474/images.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/819132567227858964/images_1.jpg"    
]

ertugrul = [
    "https://cdn.discordapp.com/attachments/819129208927420477/819129323646222356/download.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819129327899770910/ertugrul_2.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819129329816567839/ertugrul_4.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819129330407964692/ertugrul_3.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819129331003424838/ertugrul_5.jpg"
]

bams = [
    "https://cdn.discordapp.com/attachments/819129450557472770/819129525954281472/Bamsi_2.jpg",
    "https://cdn.discordapp.com/attachments/819129450557472770/819129525996224532/Bamsi_1.jpg",
    "https://cdn.discordapp.com/attachments/819129450557472770/819129528029937694/Bamsi_3.jpg",
    "https://cdn.discordapp.com/attachments/819129450557472770/819129528948752404/Bamsi_4.jpg",
    "https://cdn.discordapp.com/attachments/819129450557472770/819129530291585044/Bamsi_5.jpg"
]

def setup(client):
    client.add_cog(other(client))