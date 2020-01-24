import discord
from discord.ext import commands

class RoleReactionCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id != 654933197586694156:
            return
        if str(payload.emoji) == "<:LoL:654146562468872214>":
            role = self.bot.get_guild(payload.guild_id).get_role(653834600602402827)
            member = self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
            await member.add_roles(role)
        elif str(payload.emoji) == "<:Hots:654150946456338463>":
            role = self.bot.get_guild(payload.guild_id).get_role(653835527497449472)
            member = self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
            await member.add_roles(role)
        elif str(payload.emoji) == "<:diablo3_2:654159805694476298>":
            role = self.bot.get_guild(payload.guild_id).get_role(653835076853039104)
            member = self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
            await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id != 654933197586694156:
            return
        if str(payload.emoji) == "<:LoL:654146562468872214>":
            role = self.bot.get_guild(payload.guild_id).get_role(653834600602402827)
            member = self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
            await member.remove_roles(role)
        elif str(payload.emoji) == "<:Hots:654150946456338463>":
            role = self.bot.get_guild(payload.guild_id).get_role(653835527497449472)
            member = self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
            await member.remove_roles(role)
        elif str(payload.emoji) == "<:diablo3_2:654159805694476298>":
            role = self.bot.get_guild(payload.guild_id).get_role(653835076853039104)
            member = self.bot.get_guild(payload.guild_id).get_member(payload.user_id)
            await member.remove_roles(role)

def setup(bot):
   bot.add_cog(RoleReactionCog(bot))