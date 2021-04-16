import discord 
from discord.ext import commands
import random
import os
#from prsaw import RandomStuff

client = commands.Bot(command_prefix=('k!', 'k.', 'K.', 'K!'), case_insensitive=True, intents = discord.Intents.all()) 
client.remove_command("help")

#rs = RandomStuff(async_mode = True)

#@client.event
#async def on_message(msg):

#    if client.user == msg.author:
#        return
#    if msg.channel.id == 827222228512538694:
#        response = await rs.get_ai_response(msg.content)
#        await msg.reply(response)
        
#    await client.process_commands(msg)

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity= discord.Activity(
        type= discord.ActivityType.listening, name= "k.help" 
    )) 
    print(f"-----------\nOnline\n----------")

@client.command()
async def server(ctx):
    embed = discord.Embed(title="Server Count", description= f"<:tick:823812620632981574> I am in {len(client.guilds)} servers", color=0x0F6BE2)
    await ctx.send(embed=embed) 

#-----------------------------------------------------------------------------------------------------

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


#--------------------------------------------------------------------------------------------------------

client.run("ODIzMDkwNDY4MDkwMTUwOTQ0.YFbwuw.iQI6KXYppayNfHszRXN5rZ72RWs") 