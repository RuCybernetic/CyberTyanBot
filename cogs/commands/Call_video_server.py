from discord.ext import commands
import discord

class QuoteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='Сделать звонок на сервере')
    @commands.has_permissions(administrator=True)
    async def call(self, ctx):
        guild = ctx.message.guild.id
        channel = ctx.message.author.voice.channel.id
        embed = discord.Embed(colour=0xff000, description=f'https://discordapp.com/channels/{guild}/{channel}')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(QuoteCog(bot))