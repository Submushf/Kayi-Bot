import discord 
from discord.ext import commands
import random
import datetime

client = commands.Bot(command_prefix= "k!") 
client.remove_command("help")

@client.event
async def on_ready():
    print(f"-----------\nOnline\n----------") 


@client.command()
async def help(ctx):
    embed = discord.Embed(title="Help", color = 0x0F93E2)
    embed.add_field(name= "k!help", value="Gives you the help message.", inline=False)
    embed.add_field(name= "k!character", value="gives a picture of the character you gave.", inline=False)
    await ctx.send(embed=embed)


@client.command()
async def ertugrul(ctx):

    images = [
        "pics\\Ertugrul\\ertugrul 1.jpg","Pics\\Ertugrul\\ertugrul 2.jpg","Pics\\Ertugrul\\ertugrul 3.jpg",
        "pics\\Ertugrul\\ertugrul 4.jpg","Pics\\Ertugrul\\ertugrul 5.jpg","Pics\\Ertugrul\\ertugrul 6.jpg"
        ]

    random_image =  random.choice(images) 
    await ctx.send(file = discord.File(random_image))
    

@client.command()
async def osman(ctx):

    osma = [
        "pics\\Osman\\osman 1.jpg","pics\\Osman\\osman 2.jpg","pics\\Osman\\osman 3.jpg",
        "pics\\Osman\\osman 4.jpg","pics\\Osman\\osman 5.jpg","pics\\Osman\\osman 6.jpg" 
    ]

    random_image =  random.choice(osma) 

    await ctx.send(file = discord.File(random_image))
    

@client.command()
async def ibn_arabi(ctx):

    ibn = [
        "pics\\IbnArabi\\Ibn 1.jpg","pics\\IbnArabi\\Ibn 2.jpg","pics\\IbnArabi\\Ibn 3.jpg",
        "pics\\IbnArabi\\Ibn 4.jpg","Pics\\IbnArabi\\Ibn 5.jpg","pics\\IbnArabi\\Ibn 6.jpg"
    ]

    random_image =  random.choice(ibn) 

    await ctx.send(file = discord.File(random_image))
    

@client.command()
async def bala(ctx):

    balah = [
        "pics\\Bala\\Bala 1.jpg", "pics\\Bala\\Bala 2.jpg","pics\\Bala\\Bala 3.jpg",
        "pics\\Bala\\Bala 4.jpg","pics\\Bala\\Bala 5.jpg"
    ]

    random_image =  random.choice(balah) 

    await ctx.send(file = discord.File(random_image))

@client.command()
async def bamsi(ctx):

    ba = [
        "pics\\Bamsi\\Bamsi 1.jpg","pics\\Bamsi\\Bamsi 2.jpg","pics\\Bamsi\\Bamsi 3.jpg",
        "pics\\Bamsi\\Bamsi 4.jpg","pics\\Bamsi\\Bamsi 5.jpg","pics\\Bamsi\\Bamsi 6.jpg"
    ]

    random_image =  random.choice(ba) 

    await ctx.send(file = discord.File(random_image))

client.run("ODE0NTMwMjA4NDA1MTI3MjM4.YDfMXg.UoOZu9ON4edDYT_rp-fHyWjXqi4") 