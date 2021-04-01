import discord
from discord.ext import commands
import random
import praw

class meme(commands.Cog):
    def __init__(self, client):
        self.client = client

    reddit = praw.Reddit(client_id = "p0m92UTJwk6ccg",
                client_secret = "af1vaLhlP99UE5zEeHxTuPbtLyIZDw",
                username = "Devesh1211",
                password = "Devesh@123",
                user_agent = "pythonpraw",
                check_for_async=False)

    @commands.command(aliases=['memes'])
    async def meme(self,ctx):
    
        if not hasattr(self.client, 'nextMeme'):
            self.client.nextMeme = self.getMeme()

        name, url = self.client.nextMeme
        embed = discord.Embed(title = name)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

        self.client.nextMeme = self.getMeme()

    def getMeme(self):
        all_subs = []
        subreddit = self.reddit.subreddit("Ertugrulmemes")   
        top = subreddit.top(limit=150)

        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url
        return name, url

def setup(client):
    client.add_cog(meme(client))