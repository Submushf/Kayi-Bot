import discord
from discord.ext import commands
import asyncio
import random

class Fun(commands.Cog):

    def __init__(self, client):
        self.client=client 

	@commands.command()
	async def 8ball(context):
	    possible_responses = [
	        'no way',
	        'Prolly not',
	        'Idk',
	        'Prolly',
	        'Hell yeah my',
	    ]
	    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


def setup(client):
    client.add_cog(Moderation(client))