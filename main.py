import discord
import asyncio
from discord.ext import commands
import youtube_dl
import random
import pafy

a=list()
playerlist={}



game=discord.Game("")
bot=commands.Bot(command_prefix='/',status=discord.Status.online,activity=discord.Game(name="ground pounding ur mum"))

@bot.command(aliases=['hi'])
async def hello(ctx):
    if (len(a)>=6):
        a.pop(0)
    await ctx.send(f'{ctx.author.mention}, hi')

@bot.command(aliases=['?'])
async def babo(ctx):
    if (len(a)>=6):
        a.pop(0)
    await ctx.send('fuck you')

@bot.command(aliases=['list'])
async def embed(ctx):
    if (len(a)>=6):
        a.pop(0)
    embed=discord.Embed(title='명령어 목록',color=0xF090A6)
    embed.add_field(name="/?",value="바보",inline=False)
    embed.add_field(name="/hi",value="인사말",inline=False)
    embed.add_field(name="/enter",value="음성채널 입장",inline=False)
    embed.add_field(name="/play",value="노래 재생",inline=False)
    embed.add_field(name="/pause",value="노래 중지",inline=False)
    embed.add_field(name="/resume",value="노래 재개",inline=False)
    embed.add_field(name="/stop",value="노래 끄기",inline=False)
    embed.add_field(name="/bye",value="음성채널 퇴장",inline=False)
    embed.add_field(name="/playlist",value="재생목록",inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def enter(ctx):
    if (len(a)>=6):
        a.pop(0)
    channel = ctx.author.voice.channel
    if bot.voice_clients==[]:
        await channel.connect()
        await ctx.send("I'm in")

@bot.command()
async def play(ctx,url):
    if (len(a)>=6):
        a.pop(0)
    video=pafy.new(url)
    title=video.title
    a.append(video.title)
    
    ydl_opts = {'format': 'bestaudio'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
    voice = bot.voice_clients[0]
    voice.play(discord.FFmpegPCMAudio(URL,**FFMPEG_OPTIONS))
    
@bot.command()
async def pause(ctx):
    if (len(a)>=6):
        a.pop(0)
    if not bot.voice_clients[0].is_paused():
        bot.voice_clients[0].pause()
    else:
        await ctx.send("It's already paused bxxch")

@bot.command()
async def resume(ctx):
    if (len(a)>=6):
        a.pop(0)
    if bot.voice_clients[0].is_paused():
        bot.voice_clients[0].resume()
    else:
        await ctx.send("It's already playing bxxch")

@bot.command()
async def stop(ctx):
    if (len(a)>=6):
        a.pop(0)
    if bot.voice_clients[0].is_playing():
        bot.voice_clients[0].stop()
    else:
        await ctx.send("It's already stopped bxxth")

@bot.command()
async def bye(ctx):
    if (len(a)>=6):
        a.pop(0)
    await bot.voice_clients[0].disconnect()

@bot.command()
async def playlist(ctx):
    if (len(a)>=6):
        a.pop(0)
    await ctx.send(embed=discord.Embed(title="[PLAYLIST]",description=a,color=0xF090A6,inline=False))

bot.run('OTkzNDM5Mjc3NTQ5NjI1Mzg0.G_4Win.rdn8lgkoBHr-NNnjpeEQTLaeGZ3HfdN--ZQLgU')
token=os.environ.get('token')





