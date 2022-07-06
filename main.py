import discord
import asyncio
from discord.ext import commands
import youtube_dl
import random

game=discord.Game("")
bot=commands.Bot(command_prefix='/',status=discord.Status.online,activity=discord.Game(name="ground pounding ur mum"))

@bot.command(aliases=['hi'])
async def hello(ctx):
    await ctx.send(f'{ctx.author.mention}')

@bot.command(aliases=['?'])
async def babo(ctx):
    await ctx.send('fuck you')

@bot.command(aliases=['list'])
async def embed(ctx):
    embed=discord.Embed(title='명령어 목록',color=0xF090A6)
    embed.add_field(name="/?",value="바보",inline=False)
    embed.add_field(name="/hi",value="인사말",inline=False)
    embed.add_field(name="/play",value="노래 재생",inline=False)
    embed.add_field(name="/pause",value="노래 중지",inline=False)
    embed.add_field(name="/resume",value="노래 재개",inline=False)
    embed.add_field(name="/stop",value="노래 끄기",inline=False)
    embed.add_field(name="/bye",value="음성채널 퇴장",inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def play(ctx,url):
    channel = ctx.author.voice.channel
    if bot.voice_clients==[]:
        await channel.connect()
        await ctx.send("I'm in")

    ydl_opts = {'format': 'bestaudio'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
    voice = bot.voice_clients[0]
    voice.play(discord.FFmpegPCMAudio(URL,**FFMPEG_OPTIONS))

@bot.command()
async def pause(ctx):
    if not bot.voice_clients[0].is_paused():
        bot.voice_clients[0].pause()
    else:
        await ctx.send("It's already paused bxxch")

@bot.command()
async def resume(ctx):
    if bot.voice_clients[0].is_paused():
        bot.voice_clients[0].resume()
    else:
        await ctx.send("It's already playing bxxch")

@bot.command()
async def stop(ctx):
    if bot.voice_clients[0].is_playing():
        bot.voice_clients[0].stop()
    else:
        await ctx.send("It's already stopped bxxth")

@bot.command()
async def bye(ctx):
    await bot.voice_clients[0].disconnect()

@bot.command()
async def playlist(ctx):
    if playlist==[]:
        await ctx.send(embed=discord.Embed(title=":no_entry_sign: There's no playlist",color=F090A6))
        return

    playstr="```css\n[playlist]\n\n"
    for i in list(range(10)):
        playstr+=str(i+1)+":"+playlist[i]+"\n"
    await ctx.send(playstr+"```")

bot.run('token')
token=os.environ.get('token')





