import discord
from discord.ext import commands 

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', intents=intents)

@bot.command(name='sp')
async def sp(ctx, * , message):
    channel = bot.get_channel(1204063819110944798)
    await channel.send(message)
    await ctx.message.delete()
bot.run('MTIwNDA4ODY3NjIxNzM5MzE3Mg.GyA0k4.Pz0F9zCz7MyZESAqfApUnSFt2sjjDClATRVhoM')
