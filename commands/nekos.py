import discord
import nekos
import io

from urllib.request import Request, urlopen
from discord.ext import commands

class NekosCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cat(self, ctx):
        cats = nekos.cat()
        r = Request(cats, headers={'User-Agent': 'Mozilla/5.0'})
        g = urlopen(r).read()
        f = io.BytesIO(g)
        await ctx.send(file=discord.File(f, filename=f'cats.{cats[-3:]}'))

def setup(bot):
    bot.add_cog(NekosCog(bot))