import discord
import os
from discord import client
from discord.ext import commands
from config import ACCESS_TOKEN

textchannel_id = 368802920306573314

bot = commands.Bot(command_prefix='§', description="Sim0nSB test Bot")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.event
async def on_ready():
    channel = bot.get_channel(textchannel_id)
    await channel.send("Wir sind Online als " + bot.user.name)
    await bot.change_presence(activity=discord.Game('Am Botten'), status=discord.Status.do_not_disturb)


@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


@bot.command()
async def india(ctx):
    channel = ctx.author.voice.channel
    voice = await channel.connect()
    voice.play(discord.FFmpegPCMAudio("/Users/simon/Documents/vsCode/Privat/PyBot/audio/indian-sound.mp3"))
    
@bot.command()
async def orgasm(ctx):
    channel = ctx.author.voice.channel
    voice = await channel.connect()
    voice.play(discord.FFmpegPCMAudio("/Users/simon/Documents/vsCode/Privat/PyBot/audio/orgasm.mp3"))
        
@bot.command()
async def windows(ctx):
    channel = ctx.author.voice.channel
    voice = await channel.connect()
    voice.play(discord.FFmpegPCMAudio("/Users/simon/Documents/vsCode/Privat/PyBot/audio/windows-xp.mp3"))



        


bot.run(ACCESS_TOKEN)