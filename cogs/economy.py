import discord 
from discord.ext import commands
import asyncio
import random
import json

class Economy(commands.Cog):

    def __init__(self, client):
        self.client=client 


@commands.command()
async def balance(self,ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title = f"{ctx.author.name}'s  balance", color = 0x0F6BE2)
    em.set_thumbnail(url= "https://cdn.discordapp.com/attachments/818374423685627907/818378561189969930/kayi_bot.png")
    em.add_field(name = "Wallet balance", value = wallet_amt)
    em.add_field(name = "Bank balance", value = bank_amt)
    await ctx.send(embed= em)


@commands.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def work(self, ctx):	
    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.author

    earnings = random.randrange(20)

    await ctx.send(f"You earned 💰{earnings} coins!!")


    users[str(user.id)]["wallet"] += earnings
    
    with open("mainbank.json","w") as f:
        json.dump(users,f) 


@commands.command()
async def withdraw(self,ctx,amount = None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount>bal[1]:
        await ctx.send("you dont have that much Drapes coin!")
        return
    if amount<0:
        await ctx.send("amount must be positive!")
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount, "bank")

    await ctx.send(f"You withdrew {amount} Drapes coins!")


@commands.command()
async def deposit(self,ctx,amount = None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount>bal[0]:
        await ctx.send("you dont have that much Drapes coin!")
        return
    if amount<0:
        await ctx.send("amount must be positive!")
        return

    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount, "bank")

    await ctx.send(f"You deposited {amount} drapes coins!") 

@commands.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def send(self,ctx,member:discord.Member,amount = None):
    await open_account(ctx.author)
    await open_account(member)

    if amount == None:
        await ctx.send("please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount>bal[1]:
        await ctx.send("you dont have that much Drapes coin!")
        return
    if amount<0:
        await ctx.send("amount must be positive!")
        return

    await update_bank(ctx.author,-1*amount, "bank")
    await update_bank(member,amount, "bank")

    await ctx.send(f"You gave {amount} Drapes coins!")

@commands.command()
async def rob(self,ctx,member:discord.Member):
    await open_account(ctx.author)
    await open_account(member)

    bal = await update_bank(member)

    if bal[0]<100:
        await ctx.send("Its useless to rob this guy")
        return

    earnings = random.randrange(0, bal[0])

    await update_bank(ctx.author,earnings)
    await update_bank(member,-1*earnings)

    await ctx.send(f"You robbed and got {earnings} Drapes coins!") 


async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0 
        users[str(user.id)]["bank"] = 0

    with open("mainbank.json","w") as f:
        json.dump(users,f) 
    return True

async def get_bank_data():
    with open("mainbank.json","r") as f:
        users = json.load(f)

    return users

async def update_bank(user,change = 0,mode = "wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("mainbank.json","w") as f:
        json.dump(users,f) 
    
    bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]	
    return bal

@commands.command(aliases = ["lb"]) 
async def leaderboard(self,ctx,x = 1):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)    

    em = discord.Embed(title = f"Top {x} Richest People" , description = "This is decided on the basis of raw money in the bank and wallet",color = discord.Color(0x7E07F5))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = self.get_user(id_)
        name = member.name
        em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)


def setup(client):
    client.add_cog(Economy(client))