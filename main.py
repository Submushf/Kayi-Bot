import discord 
from discord.ext import commands
import os
import random
import asyncio
import datetime
import wikipedia
import requests

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

    random_image =  random.choice(bal) 

    await ctx.send(file = discord.File(random_image))
bal = [
    "Pics\\bala\\Bala 1.jpg", "Pics\\bala\\Bala 2.jpg","Pics\\bala\\Bala 3.jpg",
    "Pics\\bala\\Bala 4.jpg","Pics\\bala\\Bala 5.jpg"
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

@client.command(description="Shows the covid stats")
async def covid(ctx, *, countryName = None):
    try:
        if countryName is None:
            embed=discord.Embed(title="This command is used like this: ```g!covid [country]```", colour=0x07C9F5, timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)


        else:
            url = f"https://coronavirus-19-api.herokuapp.com/countries/{countryName}"
            stats = requests.get(url)
            json_stats = stats.json()
            country = json_stats["country"]
            totalCases = json_stats["cases"]
            todayCases = json_stats["todayCases"]
            totalDeaths = json_stats["deaths"]
            todayDeaths = json_stats["todayDeaths"]
            recovered = json_stats["recovered"]
            active = json_stats["active"]
            critical = json_stats["critical"]
            casesPerOneMillion = json_stats["casesPerOneMillion"]
            deathsPerOneMillion = json_stats["deathsPerOneMillion"]
            totalTests = json_stats["totalTests"]
            testsPerOneMillion = json_stats["testsPerOneMillion"]

            embed2 = discord.Embed(title=f"**COVID-19 Status Of {country}**!", description="This Information Isn't Live Always, Hence It May Not Be Accurate!", colour=0x07C9F5, timestamp=ctx.message.created_at)
            embed2.add_field(name="**Total Cases**", value=totalCases, inline=True)
            embed2.add_field(name="**Today Cases**", value=todayCases, inline=True)
            embed2.add_field(name="**Total Deaths**", value=totalDeaths, inline=True)
            embed2.add_field(name="**Today Deaths**", value=todayDeaths, inline=True)
            embed2.add_field(name="**Recovered**", value=recovered, inline=True)
            embed2.add_field(name="**Active**", value=active, inline=True)
            embed2.add_field(name="**Critical**", value=critical, inline=True)
            embed2.add_field(name="**Cases Per One Million**", value=casesPerOneMillion, inline=True)
            embed2.add_field(name="**Deaths Per One Million**", value=deathsPerOneMillion, inline=True)
            embed2.add_field(name="**Total Tests**", value=totalTests, inline=True)
            embed2.add_field(name="**Tests Per One Million**", value=testsPerOneMillion, inline=True)

            embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/781887772390719498/795612340116389898/covidbot.PNG")
            await ctx.send(embed=embed2)

    except:
        embed3 = discord.Embed(title="Invalid Country Name Or API Error! Try Again..!", colour=0x07C9F5, timestamp=ctx.message.created_at)
        embed3.set_author(name="Error!")
        await ctx.send(embed=embed3)


client.run("ODE0NTMwMjA4NDA1MTI3MjM4.YDfMXg.BeG50nM2jIY1Kj9rTHoiBnJ7M7o") 