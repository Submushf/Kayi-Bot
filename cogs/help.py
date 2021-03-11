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
        embed.add_field(name="⚙ Help", value="The help command", inline= True)
        embed.add_field(name="🔨 Moderation", value="The moderation commands", inline= True)
        embed.add_field(name="🥳 Fun", value="Shows all the fun", inline= True)
        embed.add_field(name="📷 Pic", value="Shows the list of character's from the series.", inline= True)
        embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/818374423685627907/818378561189969930/kayi_bot.png") 
        embed.set_footer(text="Prefix- k!")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))