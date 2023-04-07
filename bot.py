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
    print('Bot was connected!')
    await bot.change_presence(activity=discord.Game(f'{prefix}help'))




#bot cmds
@bot.command(name='help')
async def help(ctx):
    embed1 = discord.Embed(title="Информация о командах", color=discord.Color(0xFFFFFF))
    embed1.add_field(name=f"help : ", value="Вызовет это меню", inline=False)
    embed1.add_field(name=f"ping : ", value="Показывает текущий пинг", inline=False)
    embed1.add_field(name=f"role [@участник] [@роль]: ", value="выдает указанному участнику указанную роль", inline=False)

    embed2 = discord.Embed(title='РП дествия')
    embed1.add_field(name=f"bite [@участник] : ", value="укусить участника", inline=False)
    embed1.add_field(name=f"blush : ", value="покраснеть", inline=False)
    embed1.add_field(name=f"cry : ", value="заплакать", inline=False)
    embed1.add_field(name=f"cuddle [@участник] : ", value="прижаться к участнику", inline=False)
    embed1.add_field(name=f"dance : ", value="танцевать", inline=False)
    embed1.add_field(name=f"feed [@участник] : ", value="покормить участника", inline=False)
    embed1.add_field(name=f"happy : ", value="бысть счастливым", inline=False)
    embed1.add_field(name=f"hit [@участник] : ", value="ударить участника", inline=False)
    embed1.add_field(name=f"hug [@участник] : ", value="обнять участника", inline=False)
    embed1.add_field(name=f"kill [@участник] : ", value="убить участника", inline=False)
    embed1.add_field(name=f"kiss [@участник] : ", value="поцеловать участника", inline=False)
    embed1.add_field(name=f"cuddle [@участник] : ", value="прижаться к пользователю", inline=False)
    embed1.add_field(name=f"cuddle [@участник] : ", value="прижаться к пользователю", inline=False)
    embed1.add_field(name=f"cuddle [@участник] : ", value="прижаться к пользователю", inline=False)
    embed1.add_field(name=f"cuddle [@участник] : ", value="прижаться к пользователю", inline=False)
    embed1.add_field(name=f"cuddle [@участник] : ", value="прижаться к пользователю", inline=False)
    embed1.add_field(name=f"cuddle [@участник] : ", value="прижаться к пользователю", inline=False)
    embed1.add_field(name=f"cuddle [@участник] : ", value="прижаться к пользователю", inline=False)
    embed2.set_footer(text='РП - (Role Play)ролевые игры.')

    message = await ctx.send(embed=embed1)


#проверит пинг
@bot.command(name='ping') #работает
async def ping(ctx):
    start = time.perf_counter()
    end = time.perf_counter()
    latency = (end - start) * 1000
    embed = discord.Embed(title = f"🏓Pong!", description = f"Пинг: {latency:.2f} ms", color=discord.Color(0xFFFFFF))
    message = await ctx.send(embed=embed)

#выдать роль
@bot.command(name='role')
@commands.has_permissions(manage_roles=True)
async def role(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)

#укусить
@bot.command(name='bite')
async def bite(ctx,member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} укусил(а) {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://tenor.com/ru/view/love-kiss-anime-couple-romance-gif-17606985')
    embed.set_footer(text='Больно!')
    await ctx.channel.send(embed=embed)

#покраснеть
@bot.command(name='blush')
async def bite(ctx):
    embed = discord.Embed(title=f'{ctx.author.name} покаснел!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://tenor.com/ru/view/miku-nakano-gotoubun-no-hanayome-anime-miku-blushing-surprised-gif-17778942')
    embed.set_footer(text='Видемо ему стыдно...')
    await ctx.channel.send(embed=embed)

#заплакать
@bot.command(name='cry')
async def cry(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} плачет!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://tenor.com/ru/view/lena-vladilena-milize-eighty-six-86-sad-gif-22114746')
    embed.set_footer(text='Море слез!')
    await ctx.channel.send(embed=embed)

#прижаться к кому то
@bot.command(name='cuddle')
async def cuddle(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} прижался к {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://tenor.com/ru/view/anime-gif-26077455')
    embed.set_footer(text='Милашки!')
    await ctx.channel.send(embed=embed)

#танцевать
@bot.command(name='dance')
async def dance(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} танцует!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://tenor.com/ru/view/dance-anime-dance-gif-23191581')
    embed.set_footer(text='Дискотека!')
    await ctx.channel.send(embed=embed)

#покорми кого то
@bot.command(name='feed')
async def feed(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} накормил {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://tenor.com/ru/view/anime-dororo-feed-gif-23624256')
    embed.set_footer(text='Вкусняшка!')
    await ctx.channel.send(embed=embed)

#ударить когото
@bot.command(name='hit')
async def hit(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} ударил {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://tenor.com/ru/view/yue-arifureta-hitting-shokugyou-de-sekai-saikyou-anime-gif-15501898')
    embed.set_footer(text='Какой дерзкий!')
    await ctx.channel.send(embed=embed)

#обнять когото
@bot.command(name='hug')
async def hug(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} обнял {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://tenor.com/ru/view/hug-gif-25588769')
    embed.set_footer(text='Никуда не убежишь!')
    await ctx.channel.send(embed=embed)

#убить когото 
@bot.command(name='kill')
async def kill(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} убил {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://tenor.com/ru/view/die-kill-kills-you-anime-gif-23910501')
    embed.set_footer(text='Сколько крови!')
    await ctx.channel.send(embed=embed)

#поцеловать
@bot.command(name='kiss')
async def kiss(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} поцеловал {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://tenor.com/ru/view/love-cute-no-gif-18051138')
    embed.set_footer(text='Не мешайте парочке!')
    await ctx.channel.send(embed=embed)

#облизать
@bot.command(name='lick')
async def lick(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} лизнул {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://tenor.com/ru/view/lick-licky-anime-gif-17549074')
    embed.set_footer(text='Вся щека в слюнях!')
    await ctx.channel.send(embed=embed)

#погладить
@bot.command(name='pat')
async def pat(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} погладил {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://tenor.com/ru/view/pat-gif-19836593')
    embed.set_footer(text='Милота!')
    await ctx.channel.send(embed=embed)

#пощечина
@bot.command(name='slap')
async def slap(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} сделал пощечину {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://tenor.com/ru/view/anime-slap-mad-gif-16057834')
    embed.set_footer(text='Аж за звезды из глаз!')
    await ctx.channel.send(embed=embed)

#улыбка
@bot.command(name='smile')
async def smile(ctx):
    embed = discord.Embed(title=f'{ctx.author.name} улыбнулся!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://tenor.com/ru/view/anime-smile-gif-18275467')
    embed.set_footer(text='Улыбка до ушей!')
    await ctx.channel.send(embed=embed)

#самодовольный
@bot.command(name='smug')
async def smug(ctx):
    embed = discord.Embed(title=f'{ctx.author.name} выглядит самодовольным!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://tenor.com/ru/view/albedo-albedo-overlord-albedo-smug-smug-smug-anime-gif-23800405')
    embed.set_footer(text='Уверен в себе!')
    await ctx.channel.send(embed=embed)

#поприветствовать
@bot.command(name='wave')
async def slap(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} поприветствовал {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://tenor.com/ru/view/anime-bye-bye-maki-wave-soredemo-ayumu-wa-yosetekuru-when-will-ayumu-make-his-move-gif-26195508')
    embed.set_footer(text='И тебе здравтсвуй!')
    await ctx.channel.send(embed=embed)

#подмигнуть
@bot.command(name='wink')
async def wink(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} подмигнул {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://tenor.com/ru/view/lycoris-recoil-chisato-nishikigi-cute-wink-anime-gif-26112454')
    embed.set_footer(text='о_-!')
    await ctx.channel.send(embed=embed)


@bot.command(name='avatar')
async def avatar(ctx, member: discord.Member):
    memb = discord.utils.get(ctx.guild.members, mention=member)
    if member:
        embed = discord.Embed(title=f'Аватарка пользователя {member.name}', color=discord.Color(0xFFFFFF))
        embed.set_image(url=member.avatar_url)
        await ctx.channel.send(embed=embed)
    else:
        embed = discord.Embed(title='Ошибка', description='Пользователь не найден.', color=discord.Color(0xFFFFFF))
        await ctx.channel.send(embed=embed)

bot.run('MTA5MzUzMTY2NjM3MjM3ODcxNQ.GVpXKY.IICOQZoiocquyqDgRSTbguLbzi8K0j2huKNZ3Y')