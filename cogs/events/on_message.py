import discord
from discord.ext import commands

class OnMessageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        for attachment in message.attachments:
            if attachment.filename.endswith(('.bmp', '.jpeg', '.jpg', '.png', '.gif')):
                await message.add_reaction('<:like:656406179471294465>')
                await message.add_reaction('<:dislike:656406199490576384>')
            break

        if f'{chr(96) * 3}py' in message.content:
            await message.add_reaction('<:python:655901972418789402>')

def setup(bot):
    bot.add_cog(OnMessageCog(bot))