# Importing the discord library for discord bot
import discord
from discord.ext import commands

# importing the dotenv library for Token secracy
from dotenv import load_dotenv
import os

load_dotenv()

# TOKEN variable and retreiving the value from .env file
TOKEN = os.environ['TOKEN']

# Intenst for discord Bot
intents = discord.Intents.default()
intents.members = True

# Definig bot for whole code
bot = commands.Bot(command_prefix="!t ", intents=intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    # for making a difference b/w confirmation message and logs!!
    print("--------------------------------------------------------------------------------------------------------------------")


@bot.command(name="hi")
async def hi(ctx):
    await ctx.send(f"Hello!!👋👋 {ctx.author.mention}")


@bot.event
async def on_member_join(member):
    guild = member.guild
    await member.send(f"Welcome to the server!! {member.mention}. Please go through the rules in channel {guild.system_channel.mention}")

    if guild.system_channel is not None:
        await guild.system_channel.send(f"Welcome {member.mention} to {guild.name}. And be nice to fellow server-mates.")


@bot.command(pass_context=True, name="join")
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.reply(f"{ctx.author.name}, I joined to the same voice channel as yours!! 🔉🔉🔉")
    else:
        await ctx.reply(f"{ctx.author.name}, You are not connected to any voice channel. So please join one and try the command `!t join` to make me join the same voice channel")


@bot.command(pass_context=True, name="leave")
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send(f"{bot.user.mention} left the voice channel!! 🔇🔇🔇")
    else:
        await ctx.send("I am not connected to any voice channel, so why are you try to disconnect me from one 🤣🤣🤣")

bot.run(TOKEN)
