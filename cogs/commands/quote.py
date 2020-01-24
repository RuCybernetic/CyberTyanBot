from discord.ext import commands
import discord
import random

class QuoteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['цитата'])
    async def quote(self, ctx, link_message):
        channel = ctx.message.channel
        message_id = link_message.split('/')[-1]
        message = await channel.fetch_message(message_id)
        content = f'{message.content} [🔥]({link_message})'
        quote_channel = self.bot.get_channel(669752999517749278)
        author = message.author
        emb = discord.Embed(colour=discord.Color(random.randint(0x000000, 0xFFFFFF)), description=content)
        emb.set_footer(text=f'©️ {author.name}', icon_url=author.avatar_url)
        for a in message.attachments:
            if a.filename.endswith((".png", ".jpg", ".gif")):
                emb.set_image(url=a.proxy_url)
        await quote_channel.send(embed=emb)
        await ctx.message.delete()
        
def setup(bot):
    bot.add_cog(QuoteCog(bot))