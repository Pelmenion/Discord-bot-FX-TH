import discord
from discord.ext import commands
import youtube_dl
import os
import asyncio

prefix = '!'
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix = prefix,intents = intents)

@bot.event
async def on_ready():
    print('Bot was connected!')

# Настройки для youtube_dl
ydl_opts = {
    "format": "bestaudio/best",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
    }]
}

# Обработчик события получения сообщения
@bot.event
async def on_message(message):
    if message.content.startswith("!play"):
        # Разбиваем сообщение на список по пробелу
        args = message.content.split(" ")
        # Проверяем, что пользователь указал ссылку
        if len(args) < 2:
            await message.channel.send("Неверный формат команды. Используйте `!play ссылка`")
            return
        # Получаем ссылку на видео
        url = args[1]
        # Проверяем, что пользователь находится в голосовом канале
        if message.author.voice is None:
            await message.channel.send("Вы должны находиться в голосовом канале, чтобы проигрывать музыку")
            return
        # Загружаем аудио файл с помощью youtube_dl
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            # Получаем информацию о видео
            info = ydl.extract_info(url, download=False)
            # Создаем экземпляр класса FFmpegPCMAudio с помощью полученного аудио файла
            audio = discord.FFmpegPCMAudio(info["filename"])
            # Получаем текущий голосовой канал, в котором находится пользователь
            voice_channel = message.author.voice.channel
            # Подключаемся к голосовому каналу
            voice = await voice_channel.connect()
            # Проигрываем аудио
            voice.play(audio)
            # Ожидаем окончания проигрывания
            await voice.disconnect()

@bot.command(name='play')
async def play(ctx, url):
    if ctx.author.voice is None:
            await ctx.channel.send("Вы должны находиться в голосовом канале, чтобы проигрывать музыку")
            return
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            # Получаем информацию о видео
            info = ydl.extract_info(url, download=False)
            # Создаем экземпляр класса FFmpegPCMAudio с помощью полученного аудио файла
            audio = discord.FFmpegPCMAudio(info["filename"])
            # Получаем текущий голосовой канал, в котором находится пользователь
            voice_channel = ctx.author.voice.channel
            # Подключаемся к голосовому каналу
            voice = await voice_channel.connect()
            # Проигрываем аудио
            voice.play(audio)
            while voice.is_playing():
                await asyncio.sleep(1)
            # Удаляем файл после воспроизведения
            os.remove(info["filename"])
            # Удаляем файл после воспроизведения
            os.remove(info["filename"])
            # Отключаемся от голосового канала
            await voice.disconnect()
            # Ожидаем окончания проигрывания
            await voice.disconnect()

bot.run('OTYxMjk3MzYwNTAyMjgwMTky.GmajW0.Ez2ZxDpp7cXFp4PuK5UWluOlB5uttPpt7mrICs')