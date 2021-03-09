import discord 
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
    await ctx.send("> <:error:798368255991087125> `Unknown command. Try k!help for a list of commands`")
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

#------------------------------------------------------------------------------------------------------
driver = webdriver.Chrome()
driver.get('https://www.cleverbot.com')
driver.find_element_by_id('noteb').click()

def get_response(message):
    driver.find_element_by_xpath('//*[@id="avatarform"]/input[1]').send_keys(message + Keys.RETURN)
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="snipTextIcon"]')
            break
        except:
            continue
    response = driver.find_element_by_xpath('//*[@id="line1"]/span[1]').text
    return response

class MyClient(discord.Client):

    async def on_message(self, message):
        if message.author != self.user:
            reponse = get_response(message.content)
            await message.channel.send(f"{message.author.mention} {reponse}")


client.run("ODE4MzcyNDk5NDMxNDg5NTU2.YEXGyA.hkRJRrCQpkxIYQM91sTqO8t2WCk") 