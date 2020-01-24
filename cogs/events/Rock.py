from discord.ext import commands
import discord
from random import choice


class RockCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self,  message):
        a = ('Я знаю, что ты камень', 'Камушек попафся', 'И что, думал я не замечу? Я знаю что ты камень!')
        smile = ('<:Adjusting_his_glasses:655901928970125314>', '<:CoolStory:655902001225400390>', '<:rock:666196527034662912>')
        rock = ('камень', 'камушек', 'камни', 'камушки', 'камней', 'камушков', 'камня', 'камушка', 'камню', 'камушку', 'камнем', 'камушком', 'камне', 'камушке')
        for i in rock:
            if i in message.content.lower() and message.author.name != self.bot.user.name:
                role = discord.utils.get(message.author.guild.roles, name='🥔Камень')
                await message.channel.send(f'{choice(a)} {choice(smile) }')
                await message.add_reaction('<:rock:666196527034662912>')
                await message.author.add_roles(role)
            
def setup(bot):
    bot.add_cog(RockCog(bot))