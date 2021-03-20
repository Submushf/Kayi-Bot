import re
import math
import random

import discord
from discord.ext import commands
import DiscordUtils

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
       
        embed1 = discord.Embed(title= "Help Menu", description="Wondering where you can watch all episode [click here](https://ardirilisertugrul.net/EnErtugrul/allepisode.php) ", color = 0x0F6BE2)
        embed1.add_field(name=f"`Help`", value=f"`Shows This message`", inline=False)
        embed1.add_field(name=f"`Page-2 :`", value=f"`Shows the moderation commands`", inline= False)
        embed1.add_field(name=f"`Page-3 :`", value=f"`Shows all the other commands`", inline= False)
        embed1.add_field(name=f"`Page-4 :`", value=f"`Shows the list of character's.`", inline= False) 
        embed1.add_field(name=f"`Gif :`", value=f"`gives a random GIf from the series.`", inline= False) 
        embed1.set_thumbnail(url= "https://cdn.discordapp.com/attachments/818374423685627907/818378561189969930/kayi_bot.png")
        embed1.set_footer(text="Page-1/4")

        embed2 = discord.Embed(title= "Moderation",color=0x0F6BE2)
        embed2.add_field(name="clear", value=f"`clear's messages`", inline= False)
        embed2.add_field(name="kick", value=f"`kick members`", inline= False)
        embed2.add_field(name="ban", value=f"`ban members`", inline= False)
        embed2.add_field(name="unban", value=f"`unban members`", inline= False)
        embed2.add_field(name="info", value=f"`shows user info`", inline= False)
        embed2.add_field(name="avatar", value=f"`gives user avatar`", inline= False)
        embed2.add_field(name="server", value=f"`shows the amount of servers the bot is in`", inline= False)        
        embed2.set_thumbnail(url= "https://cdn.discordapp.com/attachments/818374423685627907/818378561189969930/kayi_bot.png") 
        embed2.set_footer(text="Page-2/4")
        
        embed3 = discord.Embed(title= "others" ,color=0x0F6BE2)
        embed3.add_field(name="8ball", value=f"`just a 8ball game`", inline= False)
        embed3.add_field(name="youtube", value=f"`Youtube channel`", inline= False) 
        embed3.add_field(name="top", value=f"`shows the top ertugrul server`", inline= False)
        embed3.add_field(name="say", value=f"`says what you say`", inline= False)
        embed3.add_field(name="poll", value=f"`make a poll`", inline= False)
        embed3.add_field(name="dead", value=f"`just gives a dead gif`", inline= False)
        embed3.add_field(name="random", value=f"`gives a random image`", inline= False)        
        embed3.set_thumbnail(url= "https://cdn.discordapp.com/attachments/818374423685627907/818378561189969930/kayi_bot.png") 
        embed3.set_footer(text="Page-3/4")

        embed4= discord.Embed(title= "Picture" , color = 0x0F6BE2)
        embed4.add_field(name="ertugrul", value= "`gives a pic of ertugrul.`", inline= False)
        embed4.add_field(name="Efamily", value= "`Showes a pic of ertugrul's family.`", inline= False)
        embed4.add_field(name="halime", value= "`gives a pic of halime.`", inline= False)
        embed4.add_field(name="osman", value= "`gives a pic of osman.`", inline= False)
        embed4.add_field(name="gondogdu", value= "`gives a pic of gondogdu.`", inline= False)
        embed4.add_field(name="Savci", value= "`gives a pic of Savci.`", inline= False)
        embed4.add_field(name="bamsi", value= "`gives a pic of bamsi.`", inline= False)
        embed4.add_field(name="turgut", value= "`gives a pic of turgut.`", inline= False)
        embed4.add_field(name="tugtekin", value= "`gives a pic of tugtekin.`", inline= False)
        embed4.add_field(name="bala", value= "`gives a pic of bala.`", inline= False)
        embed4.add_field(name="hafsa", value= "`gives a pic of hafsa.`", inline= False)
        embed4.add_field(name="selcan", value= "`gives a pic of selcan.`", inline= False)
        embed4.add_field(name="ibn_arabi", value= "`gives a pic of Ibn arabi.`", inline= False)
        embed4.add_field(name="gokce", value= "`gives a pic of gokce.`", inline= False)
        embed4.add_field(name="aslihan", value= "`gives a pic of aslihan.`", inline= False)
        embed4.add_field(name="bayhoca", value= "`gives a pic of bayhoca.`", inline= False)
        embed4.add_field(name="dogan", value= "`gives a pic of dogan.`", inline= False)
        embed4.add_field(name="noyan", value= "`gives a pic of noyan.`", inline= False)
        embed4.set_thumbnail(url= "https://cdn.discordapp.com/attachments/818374423685627907/818378561189969930/kayi_bot.png") 
        embed4.set_footer(text="Page-4/4")

        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
        paginator.add_reaction('◀', "back")
        paginator.add_reaction('⛔', "lock")
        paginator.add_reaction('▶', "next")
        embeds = [embed1, embed2, embed3, embed4]
        await paginator.run(embeds)

def setup(client):
    client.add_cog(Help(client))