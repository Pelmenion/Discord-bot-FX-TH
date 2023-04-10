import discord
from discord.ext import commands
import asyncio
from colorama import init, Fore, Back, Style
import time

prefix = 'h.'
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix = prefix,intents = intents)

bot.remove_command('help')


#start bot event
@bot.event
async def on_ready():
    print('Бот запущен в спец режиме!')
    await bot.change_presence(activity=discord.Game(f'Спец режим активен!'))

@bot.command(name='rules')
async def rules(ctx):
        image_urls = [
        'https://cdn.discordapp.com/attachments/1094537362069004319/1094539356200517682/image.png',
        'https://cdn.discordapp.com/attachments/1094537362069004319/1094539402287513651/image.png',
        'https://cdn.discordapp.com/attachments/1094537362069004319/1094539621473472574/image.png',
        'https://cdn.discordapp.com/attachments/1094537362069004319/1094539654725906462/image.png',
        'https://cdn.discordapp.com/attachments/1094537362069004319/1094539698174705695/image.png',
        'https://cdn.discordapp.com/attachments/1094537362069004319/1094539762574037043/image.png',
        'https://cdn.discordapp.com/attachments/1094537362069004319/1094539929423446096/image.png',
        'https://cdn.discordapp.com/attachments/1094537362069004319/1094540388209016893/image.png',
        'https://cdn.discordapp.com/attachments/1094537362069004319/1094540455095574588/image.png',
        'https://cdn.discordapp.com/attachments/1094537362069004319/1094541909675999242/image.png',
        'https://cdn.discordapp.com/attachments/1094537362069004319/1094541986813460530/image.png',
        'https://cdn.discordapp.com/attachments/1094537362069004319/1094542052064243742/image.png',
        'https://cdn.discordapp.com/attachments/1094537362069004319/1094542127859519548/image.png',
        'https://cdn.discordapp.com/attachments/1094537362069004319/1094542336580665454/image.png',
        'https://cdn.discordapp.com/attachments/1094537362069004319/1094542386320900216/image.png',
        'https://cdn.discordapp.com/attachments/1094537362069004319/1094542397712633866/image.png',
        'https://cdn.discordapp.com/attachments/1094537362069004319/1094542506655486053/image.png',
        'https://cdn.discordapp.com/attachments/1094537362069004319/1094542538238595163/image.png',
        'https://cdn.discordapp.com/attachments/1094537362069004319/1094542565132484638/image.png',
        
    ]

        for image_url in image_urls:
            embed = discord.Embed()
            embed.set_image(url=image_url)
            await ctx.send(embed=embed)

bot.run('MTA5MzUzMTY2NjM3MjM3ODcxNQ.GVpXKY.IICOQZoiocquyqDgRSTbguLbzi8K0j2huKNZ3Y')