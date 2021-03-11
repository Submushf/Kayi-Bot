import re
import math
import random

import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(name = 'help', description = "The help command!")
    async def help(self, ctx):
        embed= discord.Embed(title= "Help" , color = 0x0F6BE2)
        embed.add_field(name="⚙ help", value="The help command", inline= False)
        embed.add_field(name="🔨 mod", value="The moderation commands", inline= False)
        embed.add_field(name="🥳 Fun", value="Shows all the fun", inline= False)
        embed.add_field(name="📷 Pic", value="Shows the list of character's from the series.", inline= False) 
        embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/818374423685627907/818378561189969930/kayi_bot.png") 
        embed.set_footer(text="Prefix- k!")
        await ctx.send(embed=embed)

    @commands.command(name = 'mod', description = "The moderation command!")
    async def mod(self, ctx):
        embed= discord.Embed(title= "Moderation" , color = 0x0F6BE2)
        embed.add_field(name="clear", value="clear's messages", inline= False)
        embed.add_field(name="kick", value="kick members", inline= False)
        embed.add_field(name="ban", value="cban members", inline= False)
        embed.add_field(name="unban", value="unban members", inline= False)
        embed.add_field(name="info", value="shows user info", inline= False)
        embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/818374423685627907/818378561189969930/kayi_bot.png") 
        embed.set_footer(text="Prefix- k!")
        await ctx.send(embed=embed)

    @commands.command(name = 'fun', description = "The Fun command!")
    async def fun(self, ctx):
        embed= discord.Embed(title= "Fun" , color = 0x0F6BE2)
        embed.add_field(name="8ball", value="just a 8ball game", inline= False)       
        embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/818374423685627907/818378561189969930/kayi_bot.png") 
        embed.set_footer(text="Prefix- k!")
        await ctx.send(embed=embed)

    @commands.command(name = 'pic', description = "The pic command!")
    async def pic(self, ctx):
        embed= discord.Embed(title= "Picture" , color = 0x0F6BE2)
        embed.add_field(name="ertugrul", value= "gives a pic of ertugrul.", inline= False)
        embed.add_field(name="halime", value= "gives a pic of halime.", inline= False)
        embed.add_field(name="osman", value= "gives a pic of osman.", inline= False)
        embed.add_field(name="bamsi", value= "gives a pic of bamsi.", inline= False)
        embed.add_field(name="turgut", value= "gives a pic of turgut.", inline= False)
        embed.add_field(name="tugtekin", value= "gives a pic of tugtekin.", inline= False)
        embed.add_field(name="bala", value= "gives a pic of bala.", inline= False)
        embed.add_field(name="selcan", value= "gives a pic of selcan.", inline= False)
        embed.add_field(name="ibn_arabi", value= "gives a pic of Ibn arabi.", inline= False)
        embed.add_field(name="gokce", value= "gives a pic of gokce.", inline= False)
        embed.add_field(name="aslihan", value= "gives a pic of aslihan.", inline= False)
        embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/818374423685627907/818378561189969930/kayi_bot.png") 
        embed.set_footer(text="Prefix- k!")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))