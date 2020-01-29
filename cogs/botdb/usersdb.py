import discord
import sqlite3
from discord.ext import commands

class OnMessageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # conn = sqlite3.connect("database.db")
    # cursor = conn.cursor()

    @commands.Cog.listener()
    async def on_ready(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        print('DB подключено')
        for guild in self.bot.guilds:
            for member in guild.members:
                cursor.execute(f"SELECT id FROM users WHERE id={member.id}")
                if cursor.fetchone() is None:
                    cursor.execute(f"INSERT INTO users VALUES ({member.id}, '{member.name}', '<@{member.id}>', 0, 0)")
                else:
                    pass
                conn.commit()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT id FROM users WHERE id={member.id}")
        if cursor.fetchone() is None:
            cursor.execute(f"INSERT INTO users VALUES ({member.id}, '{member.name}', '<@{member.id}>', 0, 0)")
        else:
            pass
        conn.commit()

    @commands.Cog.listener()
    async def on_message(self, message):

        pass

    @commands.command()
    async def my_info(self, message):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        for i in cursor.execute(f'SELECT nickname, xp, lvl FROM users WHERE id = {message.author.id}'):
            emb = discord.Embed(title='Информация из базы данных')
            emb.add_field(name="Никнейм", value=f"{i[0]}", inline=False)
            emb.add_field(name="Опыт", value=f"{i[1]}", inline=False)
            emb.add_field(name="Уровень", value=f"{i[2]}", inline=False)
            await message.channel.send(embed=emb)

def setup(bot):
    bot.add_cog(OnMessageCog(bot))