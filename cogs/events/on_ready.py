from discord.ext import commands
import discord

class ConnectCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user} в сети!')
        print('ID:', self.bot.user.id)
        print('Bot работает.')

        game = discord.Game("Python 3")
        await self.bot.change_presence(status=discord.Status.online, activity=game)


def setup(bot):
    bot.add_cog(ConnectCog(bot))