import discord
from discord.ext import commands
from random import randint
from random import choice as randchoice
import asyncio

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ball = ["As I see it, yes", "It is certain", "It is decidedly so", "Most likely", "Outlook good",
                     "Signs point to yes", "Without a doubt", "Yes", "Yes – definitely", "You may rely on it", "Reply hazy, try again",
                     "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                     "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

    @commands.command(name="8ball", aliases=["8b"], description="Just A 8ball game")
    async def _8ball(self, *question):
        """Ask 8 ball a question

        Question must end with a question mark.
        """
        question = " ".join(question)
        if question.endswith("?") and question != "?":
            return await self.bot.say("`" + randchoice(self.ball) + "`")
        else:
            return await self.bot.say("That doesn't look like a question.")

def setup(bot):
    bot.add_cog(Fun(bot))