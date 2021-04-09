import discord
from discord.ext import commands
import random 
from random import choice 
from aiohttp import ClientSession
import asyncio
import urllib.request
import re

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['s'],description="says what you say")
    async def say(self,ctx,*,message):
        await ctx.send(f'**{message}** \n\n-**{ctx.message.author}**')

    @commands.command(aliases=['cp'],description="create a poll")
    async def poll(self,ctx,*,message):
        embed = discord.Embed(title = "Poll", description = f"{message}", color = 0x0F6BE2) 
        msg = await ctx.channel.send(embed = embed)
        await msg.add_reaction('1️⃣')
        await msg.add_reaction('2️⃣')
        await ctx.message.delete()

    @commands.command(description="dun dead comand")
    async def dead(self,ctx,  member : discord.Member = None):
        giffy = random.choice(gifs)
        await ctx.send(f"**{member}, YOU DIED**")
        await ctx.send(giffy)

    @commands.command()
    async def kill(self, ctx, member : discord.Member = None):
        kgiffy = random.choice(kgif)
        await ctx.send(f"**{member} WAS KILLED**")
        await ctx.send(kgiffy)


    @commands.command(aliases=['yts'])
    async def ytsearch(self,ctx,*, search):
        s = search.replace(' ', '_')
        search_keyword=s
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        await ctx.send("https://www.youtube.com/watch?v=" + video_ids[0])


kgif = [
    "https://c.tenor.com/Zi1l60KaBGMAAAAM/among-us-kill.gif",
    "https://c.tenor.com/zopcO8RpVpUAAAAM/kill-yourself-killing-me-smalls.gif",
    "https://cdn.discordapp.com/attachments/820565111663755274/825255936435814410/16168267362585722570335909280318.gif",
    "https://tenor.com/view/assassin-assassin-creed-arno-arno-dorian-assassins-creed-unity-gif-17819476"
]

gifs = [
    "https://tenor.com/view/casket-grave-meme-dancing-dance-gif-16902018",
    "https://c.tenor.com/B-x2kXqxJp8AAAAM/dies-over.gif"
]

def setup(bot):
    bot.add_cog(Fun(bot))