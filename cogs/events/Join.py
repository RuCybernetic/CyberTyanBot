import discord
import random
from discord.ext import commands

class OnMemberJoinCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 647290681320013825:
            role = discord.utils.get(member.guild.roles, name='Гость')
            await member.add_roles(role)
            a = ('зови своих друзей', 'пиши если чо', 'заходи не стесняйся')
            channel = self.bot.get_channel(647293816730288128)
            em = discord.Embed(description=f'{member.mention}, {random.choice(a)}', color=0x00b820)
            em.set_author(name='Добро пожаловать на сервер')
            await channel.send(embed=em)
        else:
            pass

def setup(bot):
    bot.add_cog(OnMemberJoinCog(bot))