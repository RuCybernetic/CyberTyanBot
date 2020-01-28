from discord import Embed
from discord.ext import commands
import discord


class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['удалить'])
    @commands.has_role('Админ')
    async def clear(self, ctx, amount: int = None):
        await ctx.message.delete()
        if amount is None:
            await ctx.send('Укажите кол-во сообщений которые надо удалить', delete_after=10)
        else:
            await ctx.channel.purge(limit=amount)
            emb = discord.Embed(title='Удаление сообщений',
                                description=f'Админ {ctx.author.mention} почистил чат.')
            await ctx.send(embed=emb, delete_after=10)

    @commands.command(aliases=['добавить_роль'])
    @commands.has_role('Админ')
    async def add_role(self, ctx, member: discord.Member = None, role: discord.Role = None):
        logs = self.bot.get_channel(669129314251309056)
        await ctx.message.delete()
        if member == None:
            await ctx.send('Укажите кому дать роль', delete_after=10)
        elif role == None:
            await ctx.send('Укажите какую роль дать', delete_after=10)
        else:
            await member.add_roles(role)
            emb = discord.Embed(title='Выдача роли',
                                description=f'Админ {ctx.author.mention} дал роль {role} для {member.name}.')
            await logs.send(embed=emb)

    @commands.command(aliases=['бан'])
    @commands.has_role('Админ')
    async def ban(self, ctx, member: discord.Member = None, reason=None):
        logs = self.bot.get_channel(669129314251309056)
        await ctx.message.delete()
        if member is None:
            await ctx.send('Укажите кого надо забанить', delete_after=10)
        elif member is ctx.message.author:
            await ctx.send('Ты шо дурной, зачем банить самого себя?', delete_after=10)
        else:
            if reason is None:
                emb = discord.Embed(title='Бан', description=f'Админ {ctx.author.mention} забанил пользователя {member}.')
                await logs.send(embed=emb)
                await member.send(f'Вас забанили на сервере {ctx.guild.name}')
                await ctx.guild.ban(member)
            elif reason is not None:
                emb = discord.Embed(title='Бан', description=f'Админ {ctx.author.mention} забанил пользователя {member} по причине {reason}.')
                await logs.send(embed=emb)
                await member.send(f'Вас забанили на сервере {ctx.guild.name} по причине {reason}.')
                await ctx.guild.ban(member, reason=reason)

    @commands.command(aliases=['мут'])
    @commands.has_role('Админ')
    async def mute(self, ctx, member: discord.Member = None):
        logs = self.bot.get_channel(669129314251309056)
        await ctx.message.delete()
        if member == None:
            await ctx.send('Укажите кого надо замутить', delete_after=10)
        elif member == ctx.message.author:
            await ctx.send("Ты шо дурной, зачем мутить самого себя?", delete_after=10)
        else:
            emb = discord.Embed(title="Мут", description=f'Админ {ctx.author.mention} замутил пользователя {member}')
            role = discord.utils.get(ctx.message.guild.roles, name='Mute')
            await member.add_roles(role)
            await logs.send(embed=emb)

    @commands.command(aliases=['анмут'])
    @commands.has_role('Админ')
    async def unmute(self, ctx, member: discord.Member = None):
        logs = self.bot.get_channel(669129314251309056)
        await ctx.message.delete()
        if member == None:
            ctx.send("Укажите кого надо размутить", delete_after=10)
        else:
            emb = discord.Embed(title="Анмут", description=f'Админ {ctx.author.mention} размутил пользователя {member}')
            role = discord.utils.get(ctx.message.guild.roles, name="Mute")
            await member.remove_roles(role)
            await logs.send(embed=emb)

def setup(bot):
    bot.add_cog(ModerationCog(bot))
