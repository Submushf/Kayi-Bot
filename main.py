import discord 
from discord.ext import commands
import random
import datetime
import os
import asyncio

client = commands.Bot(command_prefix= "k!", case_insensitive=True, intents = discord.Intents.all()) 
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.idle, activity= discord.Activity(
        type= discord.ActivityType.listening, name= "to k!help" 
    )) 
    print(f"-----------\nOnline\n----------") 

@client.command()
async def server(ctx):
    embed = discord.Embed(title="Server Count", description= f"<:myspace:819614963260981269>  I am in {len(client.guilds)} servers", color=0x0F6BE2)
    await ctx.send(embed=embed) 

#-----------------------------------------------------------------------------------------------------

@client.event
async def on_command_error(ctx, error):  
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("😣 `You can't do that`")
        await ctx.message.delete()

    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("<:red:819856148043137045> `Missing Required Argument`")

    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("<:error:819978871037624352> `Unknown command. Try k!help for a list of commands`")

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

#--------------------------------------------------------------------------------------------------------

@client.command()
async def pages(ctx):
    contents = ["This is page 1!", "This is page 2!", "This is page 3!", "This is page 4!"]
    pages = 4
    cur_page = 1
    message = await ctx.send(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
    # getting the message object for editing and reacting

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            # example

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            await message.delete()
            break
            # ending the loop if user doesn't react after x seconds

client.run("ODE4MzcyNDk5NDMxNDg5NTU2.YEXGyA.hkRJRrCQpkxIYQM91sTqO8t2WCk") 