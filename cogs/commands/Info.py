from discord.ext import commands
import discord
import random

class InfoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx, member: discord.Member = None):
        if not member:
            return await ctx.send('Ты не указал пользователя...')
        else:
            emb = discord.Embed(title='**Информация о {}**'.format(member),
                            color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
            emb.add_field(name='Никнейм:', value=member.name)
            emb.add_field(name='Присоединился к серверу:', value=str(member.joined_at)[:16])
            emb.add_field(name='Присоединился к дискорду:', value=str(member.created_at)[:16])
            emb.add_field(name='ID пользователя:', value=member.id)
            if member.activity is not None:
                emb.add_field(name='Играет в:', value=member.activity.name)
            else:
                pass
            emb.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=emb)

def setup(bot):
    bot.add_cog(InfoCog(bot))