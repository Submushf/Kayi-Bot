import discord
from discord.ext import commands
import random 
from random import choice 
import asyncio

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['8ball'], description = "just a 8ball game")
    async def _8ball(self,ctx):

        responses = ["As I see it, yes", "It is certain", "Most likely", "Outlook good",
                     "Signs point to yes", "Without a doubt", "Yes", "Yes – definitely", "You may rely on it", "Reply hazy, try again",
                     "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                     "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
    
        #await ctx.send(f'> 🎱 {random.choice(responses)}') 
        embed = discord.Embed(title= f"🎱 {random.choice(responses)}", color= 0x0F6BE2)
        await ctx.send(embed=embed) 

    @commands.command(description= "youtube channel")
    async def youtube(self, ctx):

        embed = discord.Embed(
            title = "Youtube", 
            description= f"<:youtube:819620176181854238> **Subscribe to [Sana Edits](https://www.youtube.com/channel/UCMxWaxacyOX_3IgD6tHRazw)**",
            color= 0xE21E0F
            )
        await ctx.send(embed=embed)
        
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


def setup(bot):
    bot.add_cog(Fun(bot))