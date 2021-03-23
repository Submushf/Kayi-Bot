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
        embed.add_field(name="Kicked",value=f"<:tick:823812620632981574> {member.mention} was kicked from the server.",inline=True)
        await ctx.send(embed=embed)

    @commands.command(aliases=['b'], description = "Ban members")
    @commands.has_permissions(ban_members = True)
    #@commands.has_role("Sultana")
    async def ban(self, ctx, member : discord.Member):
        await member.ban()
        embed = discord.Embed(color= 0x0F6BE2)
        embed.add_field(name="Banned", value= f"<:tick:823812620632981574> {member.mention} was banned from the server.") 
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
                embed.add_field(name="Unbanned", value=f"<:tick:823812620632981574> {user.mention} was unbanned.")
                await ctx.send(embed=embed)
                return

    @commands.command(aliases=['av'])
    async def avatar(self, ctx, member : discord.Member = None):
        
        if member is None:
            member = ctx.author if not member else member
            embed = discord.Embed(title = f"{member.name}'s avatar", color = 0x0F6BE2)
            embed.set_image(url=member.avatar_url)
            await ctx.send(embed=embed)
            return

        else:
            embed2 = discord.Embed(title=f"{member}'s Avatar!", colour=0x0F6BE2)
            embed2.set_image(url=member.avatar_url)
            await ctx.send(embed=embed2)

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

    @commands.command(aliases=['l', 'close'])
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user) 
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx, role : discord.Role=None, channel : discord.TextChannel=None):
        if not channel:
            channel = ctx.channel
        role = role or ctx.guild.default_role
        overwrite = channel.overwrites_for(role)
        overwrite.send_messages = False
        await channel.set_permissions(role, overwrite=overwrite)
        await ctx.message.delete()
        embed=discord.Embed(title='🔒 Channel Lock', description=f'Locked down **{channel}** for **{role}**', color=0x0F6BE2)
        embed.set_footer(text=f'Used by {ctx.author}')
        await ctx.send(embed=embed)

    @commands.command(aliases=['u', 'ul', 'open'])
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user) 
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx, role : discord.Role=None, channel : discord.TextChannel=None):
        if not channel:
            channel = ctx.channel
        role = role or ctx.guild.default_role
        overwrite = channel.overwrites_for(role)
        if role is ctx.guild.default_role:
            overwrite.send_messages = None
        if role is not ctx.guild.default_role:
            overwrite.send_messages = True
        await channel.set_permissions(role, overwrite=overwrite)
        await ctx.message.delete()
        embed=discord.Embed(title='🔓 Channel Unlock', description=f'Unlocked **{channel}** for **{role}**', color=0x0F6BE2)
        embed.set_footer(text=f'Used by {ctx.author}')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Moderation(client))