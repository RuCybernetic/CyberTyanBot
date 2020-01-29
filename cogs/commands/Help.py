from discord.ext import commands
import discord
import random

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['хелп'])
    async def help(self, ctx):
        prefix = '!'
        emb = discord.Embed(title='Команды сервера: ', color=discord.Color(random.randint(0x000000, 0xFFFFFF)), inline=False)
        emb.set_thumbnail(url=self.bot.user.avatar_url)
        emb.add_field(name=f'`{prefix}help`', value='Вызывает это сообщение.',
                      inline=False)
        emb.add_field(name='Модерация: только для роли [Админ] ',
                      value=f'`{prefix}clear` `{prefix}add_role` `{prefix}ban` `{prefix}mute` `{prefix}unmute` `{prefix}call`',
                      inline=False)
        emb.add_field(name='Развлечения: ',
                      value=f'`{prefix}cat` `{prefix}quote`',
                      inline=False)
        emb.add_field(name='Прочее: ',
                      value=f'`{prefix}info` `{prefix}my_info`',
                      inline=False)
        await ctx.send(embed=emb)

def setup(bot):
    bot.add_cog(HelpCog(bot))