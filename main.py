import discord 
from discord.ext import commands
import random
import datetime
import os

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
    await ctx.send("<<:sb_red:809289039717859338>809289039717859338> `Command not found!.`")

@client.event
async def kick_error(self,ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("> <:error:798368255991087125> `Please specify someone to kick.`")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("> <:error:798368255991087125> `You are missing required permissions: Kick Members`")

@client.event
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("> <:error:798368255991087125> `Please specify someone to ban.`")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("> <:error:798368255991087125> `You are missing required permissions: Ban Members`")

#-----------------------------------------------------------------------------------------------------

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