import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

#client on ready
@client.event
async def on_ready():
    print("bot ready")

#command
@client.command()
async def test(ctx):
    await ctx.send("test1")

client.run('YOUR TOKEN')
