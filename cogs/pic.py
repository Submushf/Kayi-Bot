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

        embed = discord.Embed(title=f"<:ottoman:819796515798253579> Osman",color= 0x0F6BE2)
        embed.set_image(url=osma)

        await ctx.send(embed=embed)


    @commands.command(description = "gives a pic of bamsi.") 
    async def bamsi(self,ctx):
        bam =  random.choice(bams)

        embed = discord.Embed(title=f"<:kayi:819796457942155285> Bamsi",color= 0x0F6BE2)
        embed.set_image(url=bam)

        await ctx.send(embed=embed)

    @commands.command(description = "gives a pic of ertugrul.") 
    async def ertugrul(self,ctx):
        ertug =  random.choice(ertugrul)

        embed = discord.Embed(title=f"<:kayi:819796457942155285> Ertugrul",color= 0x0F6BE2)
        embed.set_image(url=ertug)

        await ctx.send(embed=embed)

    @commands.command(aliases=['ia'], description = "gives pic of ibn_arabi.") 
    async def ibn_arabi(self,ctx):
        ibn =  random.choice(arabi)

        embed = discord.Embed(title=f"<:kayi:819796457942155285> Ibn Arabi",color= 0x0F6BE2)
        embed.set_image(url=ibn)

        await ctx.send(embed=embed)

    @commands.command(description = "gives a pic of bala.") 
    async def bala(self,ctx):
        bal =  random.choice(bala)

        embed = discord.Embed(title= f"<:ottoman:819796515798253579> Bala" ,color= 0x0F6BE2)
        embed.set_image(url=bal)

        await ctx.send(embed=embed)

    @commands.command(description = "gives a pic of turgut.") 
    async def turgut(self,ctx):
        tur =  random.choice(turgut)
        
        embed = discord.Embed(title=f"<:kayi:819796457942155285> Turgut",color = 0x0F6BE2)
        embed.set_image(url=tur)

        await ctx.send(embed=embed) 

    @commands.command(description = "gives a pic of selcan.") 
    async def selcan(self,ctx):
        sel =  random.choice(selcan)

        embed = discord.Embed(title=f"<:kayi:819796457942155285> Selcan",color=0x0F6BE2)
        embed.set_image(url= sel) 
 
        await ctx.send(embed = embed )

    @commands.command(description = "gives a pic of selcan.") 
    async def gokce(self,ctx):
        gok =  random.choice(gokce)

        embed = discord.Embed(title=f"<:kayi:819796457942155285> Gokce",color=0x0F6BE2)
        embed.set_image(url= gok) 
 
        await ctx.send(embed = embed )

    @commands.command(description = "gives a pic of halime.") 
    async def halime(self,ctx):
        hal =  random.choice(halime)

        embed = discord.Embed(title=f"<:kayi:819796457942155285> Halime",color=0x0F6BE2)
        embed.set_image(url= hal) 
 
        await ctx.send(embed = embed )

    @commands.command(description = "gives a pic of tugtekin.") 
    async def tugtekin(self,ctx):
        tug =  random.choice(tugtekin)

        embed = discord.Embed(title=f"<:dodurgo:819801316410785813> Tugtekin",color=0x0F6BE2)
        embed.set_image(url= tug) 
 
        await ctx.send(embed = embed )

    @commands.command(description = "gives a pic of aslihan.") 
    async def aslihan(self,ctx):
        asl =  random.choice(aslihan)

        embed = discord.Embed(title=f"<:cavdar:819801315537846272> Aslihan",color=0x0F6BE2)
        embed.set_image(url= asl) 
 
        await ctx.send(embed = embed )

    @commands.command(description = "gives a pic of aslihan.") 
    async def bayhoca(self,ctx):
        bay =  random.choice(bayhoca)

        embed = discord.Embed(title=f"<:ottoman:819796515798253579> bayhoca",color=0x0F6BE2)
        embed.set_image(url= bay) 
 
        await ctx.send(embed = embed )

    @commands.command(description = "gives a pic of dogan.") 
    async def dogan(self,ctx):
        do =  random.choice(dogan)

        embed = discord.Embed(title=f"<:kayi:819796457942155285> Dogan",color=0x0F6BE2)
        embed.set_image(url= do) 
 
        await ctx.send(embed = embed )

    @commands.command(description = "gives a pic of noyan.") 
    async def noyan(self,ctx):
        no =  random.choice(noyan)

        embed = discord.Embed(title=f"noyan",color=0x000000)
        embed.set_image(url= no) 
 
        await ctx.send(embed = embed )

    @commands.command(description = "gives a pic of gondogdu.") 
    async def gondogdu(self,ctx):
        gon =  random.choice(gondog)

        embed = discord.Embed(title=f"<:kayi:819796457942155285> gondogdu",color=0x0F6BE2)
        embed.set_image(url= gon) 
 
        await ctx.send(embed = embed )

    @commands.command(description = "gives a pic of hafsa.") 
    async def hafsa(self,ctx):
        haf =  random.choice(hafsa)

        embed = discord.Embed(title=f"<:kayi:819796457942155285> Hafsa",color=0x0F6BE2)
        embed.set_image(url= haf) 
 
        await ctx.send(embed = embed )

    @commands.command(description = "gives a pic of savci.") 
    async def savci(self,ctx):
        sav =  random.choice(savci)

        embed = discord.Embed(title=f"<:ottoman:819796515798253579> Savci",color=0x0F6BE2)
        embed.set_image(url= sav) 
 
        await ctx.send(embed = embed )

#----------------------------------------------------------------------------------------------------------------------------

savci = [
    "https://cdn.discordapp.com/attachments/822161478017875989/822162140843999242/91aded80-26e4-486f-b899-a2971179c9d7.jpg",
    "https://cdn.discordapp.com/attachments/822161478017875989/822162153611067462/35bf1969-c483-4025-a3ec-1256d3063324.jpg",
    "https://cdn.discordapp.com/attachments/822161478017875989/822162159953903706/Cute_savci_._Ertugruls_son.._Very_cute_boy_._Very_cute_boy_.png",
    "https://cdn.discordapp.com/attachments/822161478017875989/822162173752901662/fd55a7e7-ffef-4313-adb9-ccbafc3d22bd.jpg",
    "https://cdn.discordapp.com/attachments/822161478017875989/822162177842348052/Savc.jpg",
    "https://cdn.discordapp.com/attachments/822161478017875989/822162179108634694/KurulusOsman38bolum.jpg",
    "https://cdn.discordapp.com/attachments/822161478017875989/822162193071603732/d775274a-eea2-4762-b942-101e2509ec2b.jpg",
    "https://cdn.discordapp.com/attachments/822161478017875989/824040790779101204/cb55511627251a405cfcfdde34a4c2c7.jpg",
    "https://cdn.discordapp.com/attachments/822161478017875989/824040790534914059/926eea221ea8e53c5a8baddd90c64948.jpg",
    "https://cdn.discordapp.com/attachments/822161478017875989/824040790916726824/f904560f286fc601e55cc9f7754bbd20.jpg",
    "https://cdn.discordapp.com/attachments/822161478017875989/824040791240343622/ba825b00bc9b4ded22dcf356a547bc3c.jpg",
    "https://cdn.discordapp.com/attachments/822161478017875989/824040791109271590/f3966344b5b361b299fea101bfd20050.jpg",
    "https://cdn.discordapp.com/attachments/822161478017875989/824040792326668298/63ddbd26b1fc775a79e435807e040351.jpg",
    "https://cdn.discordapp.com/attachments/822161478017875989/824040792136876072/29910762b1a225db44233a49412e84a5.jpg",
    "https://cdn.discordapp.com/attachments/822161478017875989/824040792326668298/63ddbd26b1fc775a79e435807e040351.jpg",
    "https://cdn.discordapp.com/attachments/822161478017875989/824040791563042876/e8741aede930b706293ad3ef6d3a2c29.jpg"
]

hafsa = [
    "https://cdn.discordapp.com/attachments/821468846577549333/821470755735732244/MV5BZjE5MzczMTItODkyZi00NGY3LWIwNGEtMWIxZWNmYWZiNzIwXkEyXkFqcGdeQXVyNDg4MjkzNDk._V1_.jpg",
    "https://cdn.discordapp.com/attachments/821468846577549333/821471580659253288/2Q.png",
    "https://cdn.discordapp.com/attachments/821468846577549333/821472529536254022/92bf07e8355f5bff248c0fb2c1f15704.png",
    "https://cdn.discordapp.com/attachments/821468846577549333/821472530706595891/MV5BZGNkYzg1ZGYtMWE2My00MjI3LTgxNTMtZGUwMTA4N2FkMzIyXkEyXkFqcGdeQXVyNDg4MjkzNDk.png",
    "https://cdn.discordapp.com/attachments/821468846577549333/821472533765029958/892bf67b5999b35f8f20eb402b90df89.png",
    "https://cdn.discordapp.com/attachments/821468846577549333/821472530115199037/MV5BZmNiMDg3ZGUtMjQwOS00ZWY1LTk5MmQtNDQwOWQ5YzYwZWNiXkEyXkFqcGdeQXVyNDg4MjkzNDk.png",
    "https://cdn.discordapp.com/attachments/821468846577549333/821472816838344704/37b7b35a0405a02e77435a85e856dcd3.png",
    "https://cdn.discordapp.com/attachments/821468846577549333/824040656137093145/5fdc2f6dc2a34a28bdc4c783f2135db8.jpg"
]

gondog = [
    "https://cdn.discordapp.com/attachments/820499056483893298/820499323660926985/16156926802563060678998392793706.jpg",
    "https://cdn.discordapp.com/attachments/820499056483893298/820499368272199720/16156926905688703318664208853175.jpg",
    "https://cdn.discordapp.com/attachments/820499056483893298/820499409464459294/16156927006255710007520277169085.jpg",
    "https://cdn.discordapp.com/attachments/820499056483893298/820499667745374260/1615692762335309079421613789389.jpg",
    "https://cdn.discordapp.com/attachments/820499056483893298/820499964089204746/16156928181972590803948966724719.jpg",
    "https://cdn.discordapp.com/attachments/820499056483893298/820500094662869032/1615692863782429481811928387362.jpg",
    "https://cdn.discordapp.com/attachments/820499056483893298/820500201188884497/16156928888478787512302311042327.jpg",
    "https://cdn.discordapp.com/attachments/820499056483893298/820500271167176714/1615692905490716512420827936784.jpg",
    "https://cdn.discordapp.com/attachments/820499056483893298/820500536780128256/16156929678685183412621085081612.jpg",
    ""
]

noyan = [
    "https://cdn.discordapp.com/attachments/820562940821897236/820563191456727040/16157079070726485459356669641652.jpg",
    "https://cdn.discordapp.com/attachments/820562940821897236/820563297765425162/16157079330522819018708662079776.jpg",
    "https://cdn.discordapp.com/attachments/820562940821897236/820563351201120296/16157079451492512879194695117329.jpg",
    "https://cdn.discordapp.com/attachments/820562940821897236/820563548936863774/16157079919535274161949406551159.jpg",
    "https://cdn.discordapp.com/attachments/820562940821897236/820563966367236106/16157080923137251517100967212886.jpg",
    "https://cdn.discordapp.com/attachments/820562940821897236/820563926802235402/16157080719112085770880011016277.jpg",
    "https://cdn.discordapp.com/attachments/820562940821897236/820564060520448000/16157081145566693191445485987392.jpg",
    "https://cdn.discordapp.com/attachments/820562940821897236/820564110126481438/16157081264029091310944461113719.jpg"
]

dogan = [
    "https://cdn.discordapp.com/attachments/820557480881946624/820557608934834196/16157065759475243564387637528921.jpg",
    "https://cdn.discordapp.com/attachments/820557480881946624/820557662684315648/16157065888142387566695256265660.jpg",
    "https://cdn.discordapp.com/attachments/820557480881946624/820557729382531082/16157066048242185352320455733387.jpg",
    "https://cdn.discordapp.com/attachments/820557480881946624/820557864330199080/1615706637273314443126933481733.jpg",
    "https://cdn.discordapp.com/attachments/820557480881946624/820557922291023902/16157066511423539668697537595749.jpg",
    "https://cdn.discordapp.com/attachments/820557480881946624/820558252232015922/images_9_1.jpeg",
    "https://cdn.discordapp.com/attachments/820557480881946624/820558953120399360/1615706885902236371904667642398.jpg",
    "https://cdn.discordapp.com/attachments/820557480881946624/820559428448681994/16157069984773789923460368265743.jpg",
    "https://cdn.discordapp.com/attachments/820557480881946624/822156737020428295/45be87637aac2925a8ca4d18026b3ef6.jpg",
    "https://cdn.discordapp.com/attachments/820557480881946624/822156737221230612/623bfcee8c1a72fc2eeb7096e1ad60a9.jpg",
    "https://cdn.discordapp.com/attachments/820557480881946624/822156737460174939/d020ec441fa7c5543d0c2a1ea917cae3.jpg"
]

aslihan = [
    "https://cdn.discordapp.com/attachments/819576549623857183/820484931196157962/1615689246038174480679128649677.jpg",
    "https://cdn.discordapp.com/attachments/819576549623857183/820484998141706260/16156892644726201472122929848246.jpg",
    "https://cdn.discordapp.com/attachments/819576549623857183/820485035920457788/16156892733291259739840158784325.jpg",
    "https://cdn.discordapp.com/attachments/819576549623857183/820485183508971530/16156893089057113195217893009525.jpg",
    "https://cdn.discordapp.com/attachments/819576549623857183/820485276509929492/16156893310468840813811438975426.jpg",
    "https://cdn.discordapp.com/attachments/819576549623857183/820485340610428958/16156893464526472452421174794888.jpg",
    "https://cdn.discordapp.com/attachments/819576549623857183/820485426313822238/16156893657861065997739541637535.jpg",
    "https://cdn.discordapp.com/attachments/819576549623857183/820485483242455081/16156893792048999274897464650442.jpg",
    "https://cdn.discordapp.com/attachments/819576549623857183/820485532487647238/16156893919373869307518958680380.jpg",
    "https://cdn.discordapp.com/attachments/819576549623857183/820485671495008276/16156894249223039705692729381731.jpg",
    "https://cdn.discordapp.com/attachments/819576549623857183/820485739392401428/16156894403295031135772650786174.jpg",
    "https://cdn.discordapp.com/attachments/819576549623857183/820485827883827210/16156894624862309053423817077533.jpg",
    "https://cdn.discordapp.com/attachments/819576549623857183/820485962060660776/16156894946705165125572301450343.jpg",
    "https://cdn.discordapp.com/attachments/819576549623857183/824040521847537704/d1e4081d7ce0fc5b6c284f95a00463cb.jpg"
]

halime = [
    "https://cdn.discordapp.com/attachments/819317076664647690/819317373122904085/16154108805956631388302549369933.jpg",
    "https://cdn.discordapp.com/attachments/819317076664647690/819317570141552640/16154109277503067580164355590835.jpg",
    "https://cdn.discordapp.com/attachments/819317076664647690/819317614974337034/16154109383941549875372167466132.jpg",
    "https://cdn.discordapp.com/attachments/819317076664647690/819317669177327616/16154109515467180385882622499172.jpg",
    "https://cdn.discordapp.com/attachments/819317076664647690/819317749129805824/16154109705278729844922723264733.jpg",
    "https://cdn.discordapp.com/attachments/819317076664647690/819317820831432734/16154109876055200101142801813022.jpg",
    "https://cdn.discordapp.com/attachments/819317076664647690/819317960119812136/16154110197881612134819845014289.jpg",
    "https://cdn.discordapp.com/attachments/819317076664647690/819318727757529088/1615411203780128106032590144899.jpg",
    "https://cdn.discordapp.com/attachments/819317076664647690/819319762165301258/16154114504804837270365256936488.jpg",
    "https://cdn.discordapp.com/attachments/819317076664647690/819319963482325002/16154114983093038421073182876084.jpg",
    "https://cdn.discordapp.com/attachments/819317076664647690/819320262201704538/1615411569742340672366162863799.jpg",
    "https://cdn.discordapp.com/attachments/819317076664647690/819320428917030943/16154116093121596264671653419483.jpg",
    "https://cdn.discordapp.com/attachments/819317076664647690/819320742704316436/16154116728265587322147732366159.jpg",
    "https://cdn.discordapp.com/attachments/819317076664647690/819320428917030943/16154116093121596264671653419483.jpg",
    "https://cdn.discordapp.com/attachments/819317076664647690/823834340282204191/20ff8750f25ff95ba0688490ec2792f1.jpg",
    "https://cdn.discordapp.com/attachments/819317076664647690/823834340776869948/58142cc8c902e10e9fb5774f901846e3.jpg",
    "https://cdn.discordapp.com/attachments/819317076664647690/823834340916068423/f4fc856031d1407165f7be85528a44c4.jpg",
    "https://cdn.discordapp.com/attachments/819317076664647690/823834341083447326/c38731a2621ceaa6bfa62f20c74b3f59.jpg"
    
]

gokce = [
    "https://cdn.discordapp.com/attachments/819252353533476874/819252882150260756/16153955040622449359161425221861.jpg",
    "https://cdn.discordapp.com/attachments/819252353533476874/819252979924074506/16153955277391838715757751485008.jpg",
    "https://cdn.discordapp.com/attachments/819252353533476874/819253255090602014/16153955938108981379842808234937.jpg",
    "https://cdn.discordapp.com/attachments/819252353533476874/819253342274060338/16153956144973990924685431261087.jpg",
    "https://cdn.discordapp.com/attachments/819252353533476874/819253445626298398/1615395639094121034665654456255.jpg",
    "https://cdn.discordapp.com/attachments/819252353533476874/819254272113508373/16153958249763873705884494429958.jpg"    
]

selcan = [
    "https://cdn.discordapp.com/attachments/819152142933032980/819258463057346560/download.jpg",
    "https://cdn.discordapp.com/attachments/819152142933032980/819359473607901214/16154209183515887777200445349104.jpg",
    "https://cdn.discordapp.com/attachments/819152142933032980/819359538540052510/16154209339576097276691000367247.jpg",
    "https://cdn.discordapp.com/attachments/819152142933032980/819359576301240350/16154209428632109988682639984601.jpg",
    "https://cdn.discordapp.com/attachments/819152142933032980/819359777141555210/16154209907896304752978552210803.jpg",
    "https://cdn.discordapp.com/attachments/819152142933032980/819359904041009212/16154210207988629212905498614740.jpg",
    "https://cdn.discordapp.com/attachments/819152142933032980/819359979630362634/161542103889533622198050727134.jpg",
    "https://cdn.discordapp.com/attachments/819152142933032980/819360269003522108/161542110745894322770898673348.jpg",
    "https://cdn.discordapp.com/attachments/819152142933032980/819360352085082150/16154211278267847086250529926162.jpg",
    "https://cdn.discordapp.com/attachments/819152142933032980/819360652954828830/16154211995452113788625978495958.jpg",
    "https://cdn.discordapp.com/attachments/819152142933032980/819360704263880724/16154212111767046919541790522605.jpg",
    "https://cdn.discordapp.com/attachments/819152142933032980/819360865429094420/16154212499948794456397260649089.jpg"
]

bayhoca = [
    "https://cdn.discordapp.com/attachments/819588314456915978/819588620428116019/download_1.jpg",
    "https://cdn.discordapp.com/attachments/819588314456915978/819588621333823488/download.jpg",
    "https://cdn.discordapp.com/attachments/819588314456915978/819588622763556904/images_1.jpg",
    "https://cdn.discordapp.com/attachments/819588314456915978/819588623980560384/images.jpg",
    "https://cdn.discordapp.com/attachments/819588314456915978/820486197469904936/1615689550231347422146336043807.jpg",
    "https://cdn.discordapp.com/attachments/819588314456915978/820486271511822376/16156895683106705845972740810310.jpg",
    "https://cdn.discordapp.com/attachments/819588314456915978/820486345855074334/16156895862252735883577973931951.jpg",
    "https://cdn.discordapp.com/attachments/819588314456915978/820486405951586344/16156895995422859348948475527182.jpg",
    "https://cdn.discordapp.com/attachments/819588314456915978/820486498351710248/16156896223175501216099054631071.jpg",
    "https://cdn.discordapp.com/attachments/819588314456915978/820486651888402462/16156896587294213631511766874952.jpg",
    "https://cdn.discordapp.com/attachments/819588314456915978/820486907241955328/1615689718704537627682321175438.jpg",
    "https://cdn.discordapp.com/attachments/819588314456915978/820487665874239508/16156898870272337109651541081489.jpg",
    "https://cdn.discordapp.com/attachments/819588314456915978/824040579645833256/b78406a665a88a1eb63034184130403a.jpg"
]

tugtekin = [
    "https://cdn.discordapp.com/attachments/819376297124954132/819376546782904320/16154249883005725278502705500234.jpg",
    "https://cdn.discordapp.com/attachments/819376297124954132/819376597806088212/1615425001300781439539825013455.jpg",
    "https://cdn.discordapp.com/attachments/819376297124954132/819376644463788052/1615425012379453529703151924900.jpg",
    "https://cdn.discordapp.com/attachments/819376297124954132/819376727457267732/16154250319792382752861690317134.jpg",
    "https://cdn.discordapp.com/attachments/819376297124954132/819376811287773214/16154250514623715644690425987849.jpg",
    "https://cdn.discordapp.com/attachments/819376297124954132/823893326863269919/02959d8ba11a033cb2d55c3ffd20c4c8.jpg"
]

turgut = [
    "https://cdn.discordapp.com/attachments/819149935097151498/819149993105424384/turgut.jpg",
    "https://cdn.discordapp.com/attachments/819149935097151498/819373555699023912/16154242754494080247920052696772.jpg",
    "https://cdn.discordapp.com/attachments/819149935097151498/819373612758204416/16154242893201946998225326909660.jpg",
    "https://cdn.discordapp.com/attachments/819149935097151498/819373924390797332/16154243509623625115296117652233.jpg",
    "https://cdn.discordapp.com/attachments/819149935097151498/819374391384735774/16154244491843298447186875165472.jpg",
    "https://cdn.discordapp.com/attachments/819149935097151498/819374399827476480/16154244758874478035011826330902.jpg",
    "https://cdn.discordapp.com/attachments/819149935097151498/819374788379279400/16154245453498254149828348048140.jpg",
    "https://cdn.discordapp.com/attachments/819149935097151498/819375257621758002/16154246814358077674727432377284.jpg"
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
    "https://cdn.discordapp.com/attachments/819129568824000523/819311620958191667/16154094882986920428442376069523.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/822155709386719252/a654f0b16f7d5c6276767807e44cfac8.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/822155709603905606/70dc4fde14e424e9c00a377d3a3d106a.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/822155710120722472/979553d25f159cd193c6f85d3fe877f0.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/822155710434508810/af003c209985713f4fc1d91d82b17f48.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/822155710682366023/8ebf3b9d22ef9fba308f698337d79df3.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/822155710837293096/2a332d29b606a6dc5fb847e472fac909.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/822165124008771675/c30ada40fcb29d3033ee4e9055519abf.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/822165124223467610/3a370eaabaf8220b85498c5d54726e23.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/822165124482596924/3ec03ecf2c16c5c478f520078b01b28a.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/822165124705943552/a4408e75dcf959eb2a27ca4fd6200c08.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/823017464664555520/Screenshot_20210321-071642_1.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/823732138230022174/Screenshot_20210323-063042_1.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/823732138390192158/Screenshot_20210323-062826_1.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/823732138528473138/Screenshot_20210323-062507_1.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/823732138762567680/Screenshot_20210323-062220_1.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/823732138935189544/Screenshot_20210323-062103_1.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/823834379591090219/c41f1c08c543c4177d6a4b0a64642201.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/824041052121858098/51ca35aedc8a596760541c27e3fa002a.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/824041052531851304/6a3b843dc7bc225d14253951a212bece.jpg",
    "https://cdn.discordapp.com/attachments/819129568824000523/824041052729638952/f0a32e79f358fb47d46d50d1b1e4d07d.jpg"
    
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
    "https://cdn.discordapp.com/attachments/819129798210617384/819363417357549588/16154218587721362838408784663982.jpg",
    "https://cdn.discordapp.com/attachments/819129798210617384/822869763138650152/DUe3VJkVMAA801H.jpg",
    "https://cdn.discordapp.com/attachments/819129798210617384/822869766606815272/Ibn-Arabi.jpg",
    "https://cdn.discordapp.com/attachments/819129798210617384/822869766758465557/DwIsLSjX0AEHuTJ.jpg",
    "https://cdn.discordapp.com/attachments/819129798210617384/822869767936409620/images_1.jpg",
    "https://cdn.discordapp.com/attachments/819129798210617384/822869769764995102/images.jpg"
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
    "https://cdn.discordapp.com/attachments/819129626601193494/819323001081167922/osman8.PNG",
    "https://cdn.discordapp.com/attachments/819129626601193494/822156681198174278/a2096c412e305f72cac7661fef864653.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/822156682297212955/7f6e6e9da2aa883ccfddfb6d829c0c58.png",
    "https://cdn.discordapp.com/attachments/819129626601193494/822156682658316328/bc3088b3670d92a90f6f5220707973ee.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/823732237563592704/Screenshot_20210323-060922_1.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/823732236871270420/Screenshot_20210323-062247_1.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/823732237052543001/Screenshot_20210323-062050_1.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/823732237227917322/Screenshot_20210323-061805_1.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/824040993463861288/f0a32e79f358fb47d46d50d1b1e4d07d.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/823833890967257088/490d5cf54c43a50a509ef433f761da9e.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/823833890695151616/842b9069d1efaea55c67f173c2d5776a.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/823833890509553724/06ec3a1a5271c719c5de8008d9666901.jpg",
    "https://cdn.discordapp.com/attachments/819129626601193494/823893506099249172/a0f27145d5cd2caa21a5f0d036ae7550.jpg"
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
    "https://cdn.discordapp.com/attachments/819129208927420477/819256763777548368/16153964301134010854488612466299.jpg",
    "https://cdn.discordapp.com/attachments/820936329277472828/820936412463104020/472e490aa9cfd3802f739a34642a8f49.jpg",
    "https://cdn.discordapp.com/attachments/820936329277472828/820936562057543680/IMG__.jpg",
    "https://cdn.discordapp.com/attachments/820936329277472828/820936688121544754/IMG__.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/823833207203037204/f99ffd10ccf649f086916bdcc052dffd.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/823833207376052235/8151eb799cf78649c154bc7ed0f785e9.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/823833207526653952/c15f3a5b76af8b0b981ec72d12dff7c4.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/823833207722999828/9c85c3abe24c1a886561a9a7bcca292e.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/823833207849746432/10bc131ad8562a221d9fd0aa4d2673a9.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/823833280435585064/58142cc8c902e10e9fb5774f901846e3.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/823833280621182987/eb3bb3cd395892faeb7c7c034750872b.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/823833280796557312/a762c1c4f8fe82b16d173f79ebc13293.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/823833280951353394/7113d72c8fe71d2811e6bba2a97fb60f.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/823833352321892362/0ac049ed27a3f96d6091a34e4c5d6562.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/823833352553496586/d61f359b08e528929c6c1af19baf9770.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/823833352729395240/8d7f5e08667acf55ca4f243aa1b5fc9d.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/823893377451294770/dca9fd0a22a46c06bf356c0831b33785.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/823893377941504020/70d9eb955da570ff251ccb496fcb9ef3.jpg",
    "https://cdn.discordapp.com/attachments/819129208927420477/823893378156462140/8a95e1eaba3059b44b3e56520f516d5d.png",
    "https://cdn.discordapp.com/attachments/822161478017875989/824040791403397120/202f1ca0caa4baf8a0eb37f84e39cdf5.jpg"
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
    "https://cdn.discordapp.com/attachments/819129450557472770/819258887672692787/16153969367893851033852730751383.jpg",
    "https://cdn.discordapp.com/attachments/819129450557472770/823834668914835466/0b9b9743075438d710edd1bc5362bf37.jpg"
]

def setup(client):
    client.add_cog(other(client))