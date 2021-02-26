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

    random_image =  random.choice(images) 
    await ctx.send(file = discord.File(random_image))
images = [
    "Pics\\Ertugrul\\ertugrul 1.jpg","Pics\\Ertugrul\\ertugrul 2.jpg","Pics\\Ertugrul\\ertugrul 3.jpg",
    "Pics\\Ertugrul\\ertugrul 4.jpg","Pics\\Ertugrul\\ertugrul 5.jpg","Pics\\Ertugrul\\ertugrul 6.jpg"
    ]

@client.command()
async def osman(ctx):

    random_image =  random.choice(osma) 

    await ctx.send(file = discord.File(random_image))
osma = [
    "Pics\\Osman\\osman 1.jpg","Pics\\Osman\\osman 2.jpg","Pics\\Osman\\osman 3.jpg",
    "Pics\\Osman\\osman 4.jpg","Pics\\Osman\\osman 5.jpg","Pics\\Osman\\osman 6.jpg" 
]


@client.command()
async def ibn_arabi(ctx):

    random_image =  random.choice(ibn) 

    await ctx.send(file = discord.File(random_image))
ibn = [
    "Pics\\IbnArabi\\Ibn 1.jpg","Pics\\IbnArabi\\Ibn 2.jpg","Pics\\IbnArabi\\Ibn 3.jpg",
    "Pics\\IbnArabi\\Ibn 4.jpg","Pics\\IbnArabi\\Ibn 5.jpg","Pics\\IbnArabi\\Ibn 6.jpg"
]

@client.command()
async def bala(ctx):

    random_image =  random.choice(balah) 

    await ctx.send(file = discord.File(random_image))
balah = [
    "Pics\\Bala\\Bala 1.jpg", "Pics\\Bala\\Bala 2.jpg","Pics\\Bala\\Bala 3.jpg",
    "Pics\\Bala\\Bala 4.jpg","Pics\\Bala\\Bala 5.jpg"
]

@client.command()
async def bamsi(ctx):

    random_image =  random.choice(bam) 

    await ctx.send(file = discord.File(random_image))
bam = [
    "Pics\\Bamsi\\Bamsi 1.jpg","Pics\\Bamsi\\Bamsi 2.jpg","Pics\\Bamsi\\Bamsi 3.jpg",
    "Pics\\Bamsi\\Bamsi 4.jpg","Pics\\Bamsi\\Bamsi 5.jpg","Pics\\Bamsi\\Bamsi 6.jpg"
]

@client.command(aliases = ['A']) 
async def Aslihan(ctx):

    random_image =  random.choice(asl) 

    await ctx.send(file = discord.File(random_image))
asl = ["Pics\\Aslihan\\Aslihan 1.jpg"] 

client.run("ODE0NTMwMjA4NDA1MTI3MjM4.YDfMXg.BeG50nM2jIY1Kj9rTHoiBnJ7M7o") 