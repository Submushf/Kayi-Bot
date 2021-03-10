import discord
from discord.ext import commands
import random 
from random import choice 
import asyncio

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['8ball'])
    async def _8ball(self,ctx, *,member):

        responses = ["As I see it, yes", "It is certain", "Most likely", "Outlook good",
                     "Signs point to yes", "Without a doubt", "Yes", "Yes – definitely", "You may rely on it", "Reply hazy, try again",
                     "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                     "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
    
        await ctx.send(f'{member.mention} {random.choice(responses)}') 

def setup(bot):
    bot.add_cog(Fun(bot))