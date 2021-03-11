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
    "https://cdn.discordapp.com/attachments/819152142933032980/819152208217112576/download.jpg",
    "https://cdn.discordapp.com/attachments/819152142933032980/819258463057346560/download.jpg"
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
    "https://cdn.discordapp.com/attachments/819129568824000523/819147597485834240/crop.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/819147598836269076/e3b8ee559f3780622332c44ea53caf9f.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/819259483196358676/16153970785403713226195795561269.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/819259646405509130/16153971169234260322434651949770.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/819259766449897502/16153971459472096856475720546899.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/819259836133801984/16153971611712824311368080648650.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/819260166099828797/1615397241128971185448621089115.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/819260345184288788/images_4_1.jpeg",
    "https://cdn.discordapp.com/attachments/819129568824000523/819260409156599848/16153972990783930123758325008565.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/819261102432059402/16153974646587450084958545313554.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/819261170405998642/16153974804158271689860223977181.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/819310853186650202/16154093259956732633600087303372.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/819311078206996531/16154093798345613992896257077841.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/819311264160940072/16154094234978699690557893743253.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/819311620958191667/16154094882986920428442376069523.jpg"
]

arabi = [
    "https://cdn.discordapp.com/attachments/819129798210617384/819129857060372480/Ibn_1.jpg",
    "https://cdn.discordapp.com/attachments/819129798210617384/819129858230583296/Ibn_3.jpg",
    "https://cdn.discordapp.com/attachments/819129798210617384/819129860911661076/Ibn_4.jpg",
    "https://cdn.discordapp.com/attachments/819129798210617384/819129866225451008/Ibn_6.jpg",
    "https://cdn.discordapp.com/attachments/819129798210617384/819362692153344031/16154216858734618015024032976350.jpg",
    "https://cdn.discordapp.com/attachments/819129798210617384/819362987642454046/16154217451457094694743395791199.jpg",
    "https://cdn.discordapp.com/attachments/819129798210617384/819363165439524864/16154217981314251649338964581075.jpg",
    "https://cdn.discordapp.com/attachments/819129798210617384/819363303133413376/1615421831469199482492886621116.jpg",
    "https://cdn.discordapp.com/attachments/819129798210617384/819363417357549588/16154218587721362838408784663982.jpg"
]

osm = [
    "https://cdn.discordapp.com/attachments/819129626601193494/819129734386155530/osman_1.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/819129734939279400/IMG_7336.JPG",
    "https://cdn.discordapp.com/attachments/819129626601193494/819313743716286514/16154100152766367997828979813107.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/819313815312138320/16154100326041384446161409783364.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/819313863295762493/1615410044267351550655207418004.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/819314025175187496/16154100816642655227935493661433.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/819314118191611934/16154101043737235403151073204347.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/819314157966327868/16154101141986423375166099679888.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/819314409418915860/16154101630925381454156296005164.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/819322837504229405/com.bongasoft.addremovewatermark_osman15.PNG",
    "https://cdn.discordapp.com/attachments/819129626601193494/819322858522017802/fafd.PNG",
    "https://cdn.discordapp.com/attachments/819129626601193494/819322886711803964/osman_pfp.PNG",
    "https://cdn.discordapp.com/attachments/819129626601193494/819322900514471966/osman6.PNG",
    "https://cdn.discordapp.com/attachments/819129626601193494/819323216032038942/osman13.PNG",
    "https://cdn.discordapp.com/attachments/819129626601193494/819323217633607681/osmannn.PNG",
    "https://cdn.discordapp.com/attachments/819129626601193494/819323064717148241/osman12.PNG",
    "https://cdn.discordapp.com/attachments/819129626601193494/819323001081167922/osman8.PNG"
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
    "https://cdn.discordapp.com/attachments/819129208927420477/819255292579676190/16153960796056172704452842558216.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819255671970070578/16153961698386160215886082935643.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819255973469749268/16153962416257233877281789087956.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819256332448170094/16153963269127801742146634494941.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819256290253602866/16153963174373194960803211838412.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819256601470435398/16153963916144988152238484112560.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819256669347250186/1615396407968261973972943916786.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819256717422231593/16153964193354842829585875581591.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/819256763777548368/16153964301134010854488612466299.jpg"
]

bams = [
    "https://cdn.discordapp.com/attachments/819129450557472770/819129525954281472/Bamsi_2.jpg",
    "https://cdn.discordapp.com/attachments/819129450557472770/819129525996224532/Bamsi_1.jpg",
    "https://cdn.discordapp.com/attachments/819129450557472770/819129528029937694/Bamsi_3.jpg",
    "https://cdn.discordapp.com/attachments/819129450557472770/819129528948752404/Bamsi_4.jpg",
    "https://cdn.discordapp.com/attachments/819129450557472770/819129530291585044/Bamsi_5.jpg",
    "https://cdn.discordapp.com/attachments/819129450557472770/819257479858094120/16153966005407013730361639870858.jpg",
    "https://cdn.discordapp.com/attachments/819129450557472770/819257598960074780/16153966291478243838237182306760.jpg",
    "https://cdn.discordapp.com/attachments/819129450557472770/819257695886114816/16153966523914038257354979805402.jpg",
    "https://cdn.discordapp.com/attachments/819129450557472770/819257858741764116/16153966907562437270273258649968.jpg",
    "https://cdn.discordapp.com/attachments/819129450557472770/819258032055123968/16153967322472246835040504632118.jpg",
    "https://cdn.discordapp.com/attachments/819129450557472770/819258071284580373/16153967418066304577480538576916.jpg",
    "https://cdn.discordapp.com/attachments/819129450557472770/819258206252433448/16153967740392150726857299428802.jpg",
    "https://cdn.discordapp.com/attachments/819129450557472770/819258262138126356/1615396787139941009599070588682.jpg",
    "https://cdn.discordapp.com/attachments/819129450557472770/819259054471249940/16153969760408821095341864860067.jpg",
    "https://cdn.discordapp.com/attachments/819129450557472770/819258887672692787/16153969367893851033852730751383.jpg"
]

def setup(client):
    client.add_cog(other(client))