import os
import discord
from discord.ext import commands


TOKEN = os.environ.get('BOT_TOKEN')
bot = commands.Bot(command_prefix='!')

bot.load_extension("jishaku")


@bot.command()
async def ping(ctx):
    latency = bot.latency
    a = await ctx.send(latency)

@bot.command()
async def load(ctx, extensions):
    bot.load_extension(f'cogs.{extensions}')
    await ctx.send("loaded")

@bot.command()
async def unload(ctx, extensions):
    bot.unload_extension(f'cogs.{extensions}')
    await ctx.send("unloaded")

@bot.command()
async def reload(ctx, extensions):
    bot.unload_extension(f'cogs.{extensions}')
    bot.load_extension(f'cogs.{extensions}')
    await ctx.send("reloaded")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

for filename in os.listdir('./cogs/commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.commands.{filename[:-3]}')

for filename in os.listdir('./cogs/events'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.events.{filename[:-3]}')

bot.run(TOKEN)
