import discord 
from discord.ext import commands
import random
import datetime
import os
import asyncio

client = commands.Bot(command_prefix= "k!", intents = discord.Intents.all()) 
client.remove_command("help")

@client.event
async def on_ready():
    print(f"-----------\nOnline\n----------") 

async def ch_pr():
    await client.wait_until_ready()

    statuses = [f"in {len(client.guilds)} servers", "k!help"]  

    while not client.is_closed():

        status = random.choice(statuses) 
        await client.change_presence(activity=discord.Game(name=status)) 

        await asyncio.sleep(120) 

client.loop.create_task(ch_pr())

@client.event
async def on_member_join(member):
    channel = client.get_channel(816417695423004683)
    await channel.send(f"🥳 Hey {member.mention}, Welcome To the server. Hope you Enjoy your stay.")

#-----------------------------------------------------------------------------------------------------

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send("<:error:798368255991087125> `Unknown command. Try k!help for a list of commands`")


@client.command()
async def server(ctx):
    embed = discord.Embed(title="Server Count", description= f"<:myspace:819614963260981269>  I am in {len(client.guilds)} servers", color=0x0F6BE2)
    await ctx.send(embed=embed) 

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

@client.command()
async def top(ctx):
    embed = discord.Embed(
        title = "<:kayi:819796457942155285> Top Servers", 
        description= "**Kayi Edits [click here](https://discord.gg/shqH8NH84f)**\n **Ertugrul Community [click here](https://discord.gg/V6MKJQ5zVC)**\n **IYI Community [click here](https://discord.gg/3aRqRUqp8b)**", 
        color=0x0F6BE2
        )
    await ctx.send(embed=embed)


client.run("ODE4MzcyNDk5NDMxNDg5NTU2.YEXGyA.hkRJRrCQpkxIYQM91sTqO8t2WCk") 