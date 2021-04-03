import re
import math
import random
from asyncio import sleep
import discord
from discord.ext import commands
import DiscordUtils

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
       
        embed1 = discord.Embed(
            title= "Help Menu",
            description = f'`Prefix :` - `k./k!`\n`Page 1 :` - `Menu`\n`Page 2 :` - `Other`\n`Page 3 :` - `Dirilis_Ertugrul/Kurulus_Osman`' , 
            color = 0x0F6BE2
            )
        embed1.add_field(name="Links", value="[Our Server](https://discord.gg/bv6UZafJzG)", inline=False)
        embed1.set_thumbnail(url= "https://cdn.discordapp.com/attachments/818374423685627907/818378561189969930/kayi_bot.png")
        embed1.set_footer(text="React to change page • 1/3") 


        embed3 = discord.Embed(color=0x0F6BE2)
        embed3.add_field(name='Others', value='`say`, `dead`, `kill`, `memes`, `gif`', inline=False) 
        embed3.set_footer(text="Page • 2/3")


        embed4= discord.Embed(color = 0x0F6BE2)
        embed4.add_field(name='Dirilis Ertugrul', value='`ertugrul`, `halime`, `hayme`, `suleyman_shah`, `ilibilge`, `sungurtekin`, `kurtoglu`, `omer`, `deli_demir`, `aykiz`, `gondogdu`, `turgut`, `tugtekin`, `hafsa`, `emir_alaziz`, `leyla`, `ibn_arabi`, `gokce`, `aslihan`, `dogan`, `titus`, `petruccio`, `ares`, `noyan`', inline=False) 
        embed4.add_field(name='Kurulus Osman', value='`osman`, `bala`, `gonca`, `bamsi`, `savci`, `selcan`, `bayhoca`, `boran`, `goktug`, `gunduz`, `malhun`', inline=False) 
        embed4.set_footer(text="Page • 3/3")

        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
        paginator.add_reaction('<:back1:823818044249341962>', "back")
        paginator.add_reaction('⛔', "lock")
        paginator.add_reaction('<:forward1:823818044052733992>', "next")
        embeds = [embed1, embed3, embed4]
        await paginator.run(embeds)

    @commands.command(aliases=['latency'])
    @commands.cooldown(1, 5, commands.BucketType.user) 
    async def ping(self, ctx):
        em2=discord.Embed(description=f"<:update:809170074006192130> My ping in **{ctx.guild.name}** is `{round(self.client.latency * 1000)}`ms", color=0x0F6BE2)
        em2.set_author(name=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
        em1=discord.Embed(description="`Pinging...`", color=0x0F6BE2)
        em1.set_author(name=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
        message = await ctx.send(embed=em1)
        await sleep(self.client.latency)
        await message.edit(embed=em2)



def setup(client):
    client.add_cog(Help(client))