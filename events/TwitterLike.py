from discord.ext import commands
import discord

class TwitCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self,  message):
        if message.content.startswith('https://twitter.com/'):
            await message.add_reaction('<:like:656406179471294465>')
            await message.add_reaction('<:dislike:656406199490576384>')
            
def setup(bot):
    bot.add_cog(TwitCog(bot))