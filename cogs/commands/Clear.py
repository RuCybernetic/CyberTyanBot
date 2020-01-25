from discord.ext import commands
import discord

class ClearCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['удалить'])
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount: int = None):
        if amount is None:
            await ctx.send('Укажите кол-во сообщений которые надо удалить')
        else:
            await ctx.message.delete()
            await ctx.channel.purge(limit=amount)
        emb = discord.Embed(title='Удаление сообщений', description=f'Администратор {ctx.author.mention} почистил чат.')
        await ctx.send(embed=emb, delete_after=10)

def setup(bot):
    bot.add_cog(ClearCog(bot))