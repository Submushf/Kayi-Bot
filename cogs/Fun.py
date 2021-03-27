import discord
from discord.ext import commands
import random 
from random import choice 
from aiohttp import ClientSession
import asyncio

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

kgif = [
    "https://c.tenor.com/Zi1l60KaBGMAAAAM/among-us-kill.gif",
    "https://c.tenor.com/zopcO8RpVpUAAAAM/kill-yourself-killing-me-smalls.gif"
]

gifs = [
    "https://tenor.com/view/casket-grave-meme-dancing-dance-gif-16902018",
    "https://c.tenor.com/B-x2kXqxJp8AAAAM/dies-over.gif"
]

def setup(bot):
    bot.add_cog(Fun(bot))