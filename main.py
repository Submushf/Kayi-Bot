import discord 
from discord.ext import commands
import random
import datetime
import os
from discord.voice_client import VoiceClient
import youtube_dl
import asyncio

client = commands.Bot(command_prefix= "k!", intents = discord.Intents.all()) 
client.remove_command("help")

@client.event
async def on_ready():
    print(f"-----------\nOnline\n----------") 

@client.event
async def on_member_join(member):
    channel = client.get_channel(816417695423004683)
    await channel.send(f"🥳 Hey {member.mention}, Welcome To the server. Hope you Enjoy your stay.")

#-----------------------------------------------------------------------------------------------------

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send("> <:error:798368255991087125> `Unknown command. Try k!help for a list of commands`")

#------------------------------------------------------------------------------------------------------
@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}") 

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}") 

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}') 


client.run("ODE4MzcyNDk5NDMxNDg5NTU2.YEXGyA.hkRJRrCQpkxIYQM91sTqO8t2WCk") 