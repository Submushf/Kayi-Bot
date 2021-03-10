import discord
from discord.ext import commands
from random import randint
from random import choice as randchoice
import datetime
import time
import asyncio

class Fun:
    def __init__(self, bot):
        self.bot = bot
        self.stopwatches = {}
        self.ball = ["As I see it, yes", "It is certain", "It is decidedly so", "Most likely", "Outlook good",
                     "Signs point to yes", "Without a doubt", "Yes", "Yes – definitely", "You may rely on it", "Reply hazy, try again",
                     "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                     "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]


    @commands.command(pass_context=True)
    async def rps(self, ctx, choice : str):
        """Play rock paper scissors"""
        author = ctx.message.author
        rpsbot = {"rock" : ":moyai:",
           "paper": ":page_facing_up:",
           "scissors":":scissors:"}
        choice = choice.lower()
        if choice in rpsbot.keys():
            botchoice = randchoice(list(rpsbot.keys()))
            msgs = {
                "win": " You win {}!".format(author.mention),
                "square": " We're square {}!".format(author.mention),
                "lose": " You lose {}!".format(author.mention)
            }
            if choice == botchoice:
                await self.bot.say(rpsbot[botchoice] + msgs["square"])
            elif choice == "rock" and botchoice == "paper":
                await self.bot.say(rpsbot[botchoice] + msgs["lose"])
            elif choice == "rock" and botchoice == "scissors":
                await self.bot.say(rpsbot[botchoice] + msgs["win"])
            elif choice == "paper" and botchoice == "rock":
                await self.bot.say(rpsbot[botchoice] + msgs["win"])
            elif choice == "paper" and botchoice == "scissors":
                await self.bot.say(rpsbot[botchoice] + msgs["lose"])
            elif choice == "scissors" and botchoice == "rock":
                await self.bot.say(rpsbot[botchoice] + msgs["lose"])
            elif choice == "scissors" and botchoice == "paper":
                await self.bot.say(rpsbot[botchoice] + msgs["win"])
        else:
            await self.bot.say("Choose rock, paper or scissors.")

    @commands.command(name="8", aliases=["8ball"])
    async def _8ball(self, *question):
        """Ask 8 ball a question

        Question must end with a question mark.
        """
        question = " ".join(question)
        if question.endswith("?") and question != "?":
            return await self.bot.say("`" + randchoice(self.ball) + "`")
        else:
            return await self.bot.say("That doesn't look like a question.")

    @commands.command(aliases=["sw"], pass_context=True)
    async def stopwatch(self, ctx):
        """Starts/stops stopwatch"""
        author = ctx.message.author
        if not author.id in self.stopwatches:
            self.stopwatches[author.id] = int(time.perf_counter())
            await self.bot.say(author.mention + " Stopwatch started!")
        else:
            tmp = abs(self.stopwatches[author.id] - int(time.perf_counter()))
            tmp = str(datetime.timedelta(seconds=tmp))
            await self.bot.say(author.mention + " Stopwatch stopped! Time: **" + str(tmp) + "**")
            self.stopwatches.pop(author.id, None)

def setup(bot):
    bot.add_cog(Fun(bot))