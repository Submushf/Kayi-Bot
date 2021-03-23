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
            color = 0x0F6BE2
            )
        embed1.add_field(name="Page-1", value=f"`This message`", inline=False)
        embed1.add_field(name="Page-2", value=f"`the moderation commands`", inline= False)
        embed1.add_field(name="Page-3", value=f"`the other commands`", inline= False)
        embed1.add_field(name="Page-4", value=f"`Shows characters from Ertugrul`", inline= False)
        embed1.add_field(name="Page-5", value=f"`Shows characters From osman`", inline= False)
        embed1.set_thumbnail(url= "https://cdn.discordapp.com/attachments/818374423685627907/818378561189969930/kayi_bot.png")
        embed1.set_footer(text="React to change page • 1/5") 

        embed2 = discord.Embed(title= "Moderation",color=0x0F6BE2)
        embed2.add_field(name="clear", value=f"`clear's messages`", inline= False)
        embed2.add_field(name="kick", value=f"`kick members`", inline= False)
        embed2.add_field(name="ban", value=f"`ban members`", inline= False)
        embed2.add_field(name="unban", value=f"`unban members`", inline= False)
        embed2.add_field(name="info", value=f"`shows user info`", inline= False)
        embed2.add_field(name="poll", value=f"`make a poll`", inline= False)
        embed2.add_field(name="avatar", value=f"`gives user avatar`", inline= False)
        embed2.add_field(name="server", value=f"`num of servers the bot is in`", inline= False)        
        embed2.set_thumbnail(url= "https://cdn.discordapp.com/attachments/818374423685627907/818378561189969930/kayi_bot.png") 
        embed2.set_footer(text="Page-2/5")
        
        embed3 = discord.Embed(title= "others" ,color=0x0F6BE2)
        embed3.add_field(name="8ball", value=f"`just a 8ball game`", inline= False)
        embed3.add_field(name="say", value=f"`says what you say`", inline= False)
        embed3.add_field(name="dead", value=f"`just gives a dead gif`", inline= False)
        embed3.add_field(name="who", value=f"`a guess who game`", inline= False)
        embed3.add_field(name="Gif", value=f"`gives a random GIf from the series.`", inline= False)        
        embed3.set_thumbnail(url= "https://cdn.discordapp.com/attachments/818374423685627907/818378561189969930/kayi_bot.png") 
        embed3.set_footer(text="Page-3/5")

        embed4= discord.Embed(title= "Ertugrul Character's" , color = 0x0F6BE2)
        embed4.add_field(name="ertugrul", value= "`gives a pic of ertugrul.`", inline= False)
        embed4.add_field(name="halime", value= "`gives a pic of halime.`", inline= False)
        embed4.add_field(name="gondogdu", value= "`gives a pic of gondogdu.`", inline= False)
        embed4.add_field(name="turgut", value= "`gives a pic of turgut.`", inline= False)
        embed4.add_field(name="tugtekin", value= "`gives a pic of tugtekin.`", inline= False)
        embed4.add_field(name="hafsa", value= "`gives a pic of hafsa.`", inline= False)
        embed4.add_field(name="ibn_arabi", value= "`gives a pic of Ibn arabi.`", inline= False)
        embed4.add_field(name="gokce", value= "`gives a pic of gokce.`", inline= False)
        embed4.add_field(name="aslihan", value= "`gives a pic of aslihan.`", inline= False)
        embed4.add_field(name="dogan", value= "`gives a pic of dogan.`", inline= False)
        embed4.add_field(name="noyan", value= "`gives a pic of noyan.`", inline= False)
        embed4.set_thumbnail(url= "https://cdn.discordapp.com/attachments/818374423685627907/818378561189969930/kayi_bot.png") 
        embed4.set_footer(text="Page-4/5")

        embed5= discord.Embed(title= "Osman Character's" , color = 0x0F6BE2)
        embed5.add_field(name="osman", value= "`gives a pic of osman.`", inline= False)
        embed5.add_field(name="Savci", value= "`gives a pic of Savci.`", inline= False)
        embed5.add_field(name="bamsi", value= "`gives a pic of bamsi.`", inline= False)
        embed5.add_field(name="bala", value= "`gives a pic of bala.`", inline= False)
        embed5.add_field(name="selcan", value= "`gives a pic of selcan.`", inline= False)
        embed5.add_field(name="bayhoca", value= "`gives a pic of bayhoca.`", inline= False)
        embed5.set_thumbnail(url= "https://cdn.discordapp.com/attachments/818374423685627907/818378561189969930/kayi_bot.png") 
        embed5.set_footer(text="Page-5/5")

        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
        paginator.add_reaction('<:back1:823818044249341962>', "back")
        paginator.add_reaction('⛔', "lock")
        paginator.add_reaction('<:forward1:823818044052733992>', "next")
        embeds = [embed1, embed2, embed3, embed4, embed5]
        await paginator.run(embeds)

    @commands.command(aliases=['latency'])
    @commands.cooldown(1, 5, commands.BucketType.user) 
    async def ping(self, ctx):
        em2=discord.Embed(description=f"<:update:809170074006192130> My ping in **{ctx.guild.name}** is `{round(self.client.latency * 1000)}`ms", color=color)
        em2.set_author(name=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
        em1=discord.Embed(description="`Pinging...`", color=0x0F6BE2)
        em1.set_author(name=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
        message = await ctx.send(embed=em1)
        await sleep(self.client.latency)
        await message.edit(embed=em2)



def setup(client):
    client.add_cog(Help(client))