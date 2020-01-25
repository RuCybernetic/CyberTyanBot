import discord
from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Список команд", description="`help`: показывает данное сообщение\n<...>")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(HelpCog(bot))