import discord
from discord.ext import commands
from pytube import YouTube
import asyncio
import ffmpeg

# Создание клиента Discord и указание префикса команд
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Обработчик события "Готовность бота"
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


# Команда для выхода бота из голосового канала
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

# Команда для проигрывания музыки с YouTube
@bot.command()
async def play(ctx, url):
    # Получение голосового клиента
    voice_client = ctx.voice_client

    # Загрузка видео с YouTube
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()

    channel = ctx.author.voice.channel
    await channel.connect()

    # Проигрывание аудио в голосовом канале
    voice_client.play(discord.FFmpegPCMAudio(executable="C:/path/to/ffmpeg.exe", source=stream.url), after=lambda e: print('done', e))

    # Ожидание окончания проигрывания
    while voice_client.is_playing():
        await asyncio.sleep(1)

    # Отключение голосового клиента после окончания проигрывания
    await voice_client.disconnect()

# Запуск бота с указанием токена
bot.run('MTA5Nzg3MTUwNjQxNzEzNTY3Ng.GtlljK.Bn5a8qsm0nHM2ylnhgmSrXpWUP37J5Fiq5tPYg')
