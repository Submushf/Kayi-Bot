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

        embed = discord.Embed(title="Osman",color= 0x0F6BE2)
        embed.set_image(url=osma)

        await ctx.send(embed=embed)


    @commands.command(description = "gives a pic of bamsi.") 
    async def bamsi(self,ctx):
        bam =  random.choice(bams)

        embed = discord.Embed(title="Bamsi",color= 0x0F6BE2)
        embed.set_image(url=bam)

        await ctx.send(embed=embed)

    @commands.command(description = "gives a pic of ertugrul.") 
    async def ertugrul(self,ctx):
        ertug =  random.choice(ertugrul)

        embed = discord.Embed(title="Ertugrul",color= 0x0F6BE2)
        embed.set_image(url=ertug)

        await ctx.send(embed=embed)

    @commands.command(description = "gives pic of ibn_arabi.") 
    async def ibn_arabi(self,ctx):
        ibn =  random.choice(arabi)

        embed = discord.Embed(title="Ibn Arabi",color= 0x0F6BE2)
        embed.set_image(url=ibn)

        await ctx.send(embed=embed)

    @commands.command(description = "gives a pic of bala.") 
    async def bala(self,ctx):
        bal =  random.choice(bala)

        embed = discord.Embed(title= "Bala" ,color= 0x0F6BE2)
        embed.set_image(url=bal)

        await ctx.send(embed=embed)

    @commands.command(description = "gives a pic of turgut.") 
    async def turgut(self,ctx):
        tur =  random.choice(turgut)
        
        embed = discord.Embed(title="Turgut",color = 0x0F6BE2)
        embed.set_image(url=tur)

        await ctx.send(embed=embed) 

    @commands.command(description = "gives a pic of selcan.") 
    async def selcan(self,ctx):
        sel =  random.choice(selcan)

        embed = discord.Embed(title="Selcan",color=0x0F6BE2)
        embed.set_image(url= sel) 
 
        await ctx.send(embed = embed )

    @commands.command(description = "gives a pic of selcan.") 
    async def gokce(self,ctx):
        gok =  random.choice(gokce)

        embed = discord.Embed(title="Gokce",color=0x0F6BE2)
        embed.set_image(url= gok) 
 
        await ctx.send(embed = embed )

#----------------------------------------------------------------------------------------------------------------------------

gokce = [
    "https://cdn.discordapp.com/attachments/819252353533476874/819252882150260756/16153955040622449359161425221861.jpg",
    "https://cdn.discordapp.com/attachments/819252353533476874/819252979924074506/16153955277391838715757751485008.jpg",
    "https://cdn.discordapp.com/attachments/819252353533476874/819253255090602014/16153955938108981379842808234937.jpg",
    "https://cdn.discordapp.com/attachments/819252353533476874/819253342274060338/16153956144973990924685431261087.jpg",
    "https://cdn.discordapp.com/attachments/819252353533476874/819253445626298398/1615395639094121034665654456255.jpg",
    "https://cdn.discordapp.com/attachments/819252353533476874/819254272113508373/16153958249763873705884494429958.jpg"    
]

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
    "https://cdn.discordapp.com/attachments/819129208927420477/819129329816567839/ertugrul_4.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819129330407964692/ertugrul_3.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819129331003424838/ertugrul_5.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819254966408577094/16153960017696995941126443763922.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819255069484384286/1615396026249388074095680904670.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819255127407460402/16153960401184365970502870309663.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819255069484384286/1615396026249388074095680904670.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819255234344779786/16153960655846886504479589455133.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819255359646203924/16153960953953446652837487059915.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819255292579676190/16153960796056172704452842558216.jpg"
    "https://cdn.discordapp.com/attachments/819129208927420477/819255671970070578/16153961698386160215886082935643.jpg"
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