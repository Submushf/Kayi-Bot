import discord 
from discord.ext import commands
import asyncio
import random

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client=client 

    @commands.error
    async def kick_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("> <:error:798368255991087125> `Please specify someone to kick.`")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("> <:error:798368255991087125> `You are missing required permissions: Kick Members`")

    @commands.error
    async def ban_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("> <:error:798368255991087125> `Please specify someone to ban.`")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("> <:error:798368255991087125> `You are missing required permissions: Ban Members`")

    @commands.command(aliases=['c'], description = "clear's messages")
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount=2):
        await ctx.channel.purge(limit = amount)

    @commands.command(aliases= ['k'], description = "Kicks members")
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member):
        await member.kick()
        embed = discord.Embed(color = 0x07C9F5 )
        embed.add_field(name="Kicked",value=f"👍 {member.mention} was kicked from the server.",inline=True)
        await ctx.send(embed=embed)

    @commands.command(aliases=['b'], description = "Ban members")
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member):
        await member.ban()
        embed = discord.Embed(color= 0x07C9F5)
        embed.add_field(name="Banned", value= f"🔨 {member.mention} was banned from the server.") 
        await ctx.send(embed=embed)

    @commands.command(aliases=['ub'], description = "UnBan members")
    async def unban(self, ctx,*, member):
        banned_user= await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_user:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(color = 0x07C9F5)
                embed.add_field(name="Unbanned", value=f"📜 {user.mention} was unbanned.")
                await ctx.send(embed=embed)
                return

    @commands.command(aliases=['whois', 'ui'], description = "Shows User's Info ")
    async def info(self, ctx, member : discord.Member=None):
        if not member:
            member = ctx.author
        created_at = member.created_at.strftime("%b %d, %Y,  %H:%m UTC")
        joined_at = member.joined_at.strftime("%b %d, %Y,  %H:%m UTC")
        embed=discord.Embed(title=f"{member.name}#{member.discriminator}'s Info", color=member.color)
        embed.add_field(name="User ID", value=f"{member.id}", inline=False)
        embed.add_field(name="Account Created At", value=f"{created_at}", inline=True)
        embed.add_field(name="Joined Server At", value=f"{joined_at}", inline=True)
        embed.set_thumbnail(url=f"{member.avatar_url}")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Moderation(client))