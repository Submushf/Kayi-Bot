import discord 
from discord.ext import commands
import asyncio
import random

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client=client 

    @commands.command(aliases=['c'], description = "clear's messages")
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount=2):
        await ctx.channel.purge(limit = amount)

    @commands.command(aliases= ['k'], description = "Kicks members")
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member):
        await member.kick()
        embed = discord.Embed(color = 0x0F6BE2 )
        embed.add_field(name="Kicked",value=f"👍 {member.mention} was kicked from the server.",inline=True)
        await ctx.send(embed=embed)

    @commands.command(aliases=['b'], description = "Ban members")
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member):
        await member.ban()
        embed = discord.Embed(color= 0x0F6BE2)
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
                embed = discord.Embed(color = 0x0F6BE2)
                embed.add_field(name="Unbanned", value=f"📜 {user.mention} was unbanned.")
                await ctx.send(embed=embed)
                return

    @commands.command(aliases=['whois', 'ui'], description = "Shows User's Info ")
    async def info(self, ctx, member : discord.Member=None):
        if not member:
            member = ctx.author
        created_at = member.created_at.strftime("%b %d, %Y,  %H:%m UTC")
        joined_at = member.joined_at.strftime("%b %d, %Y,  %H:%m UTC")
        embed=discord.Embed(title=f"{member.name}#{member.discriminator}'s Info", color=0x0F6BE2)
        embed.add_field(name="User ID", value=f"{member.id}", inline=False)
        embed.add_field(name="Account Created At", value=f"{created_at}", inline=True)
        embed.add_field(name="Joined Server At", value=f"{joined_at}", inline=True)
        embed.set_thumbnail(url=f"{member.avatar_url}")
        await ctx.send(embed=embed)

    @commands.command()
    async def servers(self,ctx):
        await ctx.send(f"<:myspace:819614963260981269> I am in {len(client.guilds)} servers") 

def setup(client):
    client.add_cog(Moderation(client))