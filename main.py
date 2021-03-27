import discord 
from discord.ext import commands
#from prsaw import RandomStuff
import random
import datetime
import os
import praw
import asyncio
import json

client = commands.Bot(command_prefix=('k!', 'k.', 'K.', 'K!', 'k?', 'K?'), case_insensitive=True, intents = discord.Intents.all()) 
client.remove_command("help")

# do under prefix thing
#rs = RandomStuff(async_mode = True)

reddit = praw.Reddit(client_id = "p0m92UTJwk6ccg",
                     client_secret = "af1vaLhlP99UE5zEeHxTuPbtLyIZDw",
                     username = "Devesh1211",
                     password = "Devesh@123",
                     user_agent = "pythonpraw")

#@client.event
#async def on_message(msg):

#    if client.user == msg.author:
#        return
#    if msg.channel.id == 824618122363273286:
#        response = await rs.get_ai_response(msg.content)
#        await msg.reply(response)
        
#    await client.process_commands(msg)

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.idle, activity= discord.Activity(
        type= discord.ActivityType.listening, name= "to k.help" 
    )) 
    print(f"-----------\nOnline\n----------") 

@client.command()
async def server(ctx):
    embed = discord.Embed(title="Server Count", description= f"<:tick:823812620632981574> I am in {len(client.guilds)} servers", color=0x0F6BE2)
    await ctx.send(embed=embed) 

#-----------------------------------------------------------------------------------------------------
@client.listen()
async def on_message(message):
    if message.content in {"<@818372499431489556>", "<@!818372499431489556>"}:
        embed = discord.Embed(color = 0x0F6BE2)
        embed.add_field(name = "<a:783393435242463324:823922568326414337> Hey there" ,value="My Default Prefix is `k.` & `k!`.")
        await message.channel.send(embed = embed)

@client.event
async def on_command_error(ctx, error):  
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("> <:deny:823812620577538059> You can't do that\n ```Missing Permission```")

    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("> <:deny:823812620577538059> `Missing Required Argument`")

    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("> <:deny:823812620577538059> `Unknown command. Try k.help for a list of commands`")

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
async def meme(ctx):
    
    if not hasattr(client, 'nextMeme'):
        client.nextMeme = getMeme()

    name, url = client.nextMeme
    embed = discord.Embed(title = name, color=0x0F6BE2)
    embed.set_image(url=url)
    await ctx.send(embed=embed)

    client.nextMeme = getMeme()

def getMeme():
    all_subs = []
    subreddit = reddit.subreddit("Ertugrulmemes")   
    top = subreddit.top(limit=150)

    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    return name, url

@client.command(aliases=['cats'])
async def cat(ctx):

    if not hasattr(client, 'nextCat'):
        client.nextCat = getCat()

    name, url = client.nextCat
    embed = discord.Embed(title = 'Cat', color=0x0F6BE2)
    embed.set_image(url=url)
    await ctx.send(embed=embed)

    client.nextCat = getCat()

def getCat():
    all_subs = []
    subreddit = reddit.subreddit("Cats")   
    top = subreddit.top(limit=100)

    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    return name, url

#--------------------------------------------------------------------------------------------------------

client.run("ODE4MzcyNDk5NDMxNDg5NTU2.YEXGyA.hkRJRrCQpkxIYQM91sTqO8t2WCk") 