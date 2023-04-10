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

counter_cmds = 0

#start bot event
@bot.event
async def on_ready():
    print('Bot was connected!')
    await bot.change_presence(activity=discord.Streaming(name=f"{prefix}help", url='https://www.youtube.com/watch?v=xvFZjo5PgG0'))


#bot cmds
@bot.command(name='help')
async def help(ctx):
    embed1 = discord.Embed(title="Информация о командах", color=discord.Color(0xFFFFFF))
    embed1.add_field(name=f"help : ", value="Вызовет это меню", inline=False)
    embed1.add_field(name=f"ping : ", value="Показывает текущий пинг", inline=False)
    embed1.add_field(name=f"role [@участник] [@роль]: ", value="выдает указанному участнику указанную роль", inline=False)
    embed1.add_field(name=f"avatar [@участник]: ", value="При указании участника выводит его аватар, иначе выводит аватар написашего", inline=False)

    embed2 = discord.Embed(title='РП дествия', color=discord.Color(0xFFFFFF))
    embed2.add_field(name=f"bite [@участник] : ", value="укусить участника", inline=False)
    embed2.add_field(name=f"blush : ", value="покраснеть", inline=False)
    embed2.add_field(name=f"cry : ", value="заплакать", inline=False)
    embed2.add_field(name=f"cuddle [@участник] : ", value="прижаться к участнику", inline=False)
    embed2.add_field(name=f"dance : ", value="танцевать", inline=False)
    embed2.add_field(name=f"feed [@участник] : ", value="покормить участника", inline=False)
    embed2.add_field(name=f"happy : ", value="бысть счастливым", inline=False)
    embed2.add_field(name=f"hit [@участник] : ", value="ударить участника", inline=False)
    embed2.add_field(name=f"hug [@участник] : ", value="обнять участника", inline=False)
    embed2.add_field(name=f"kill [@участник] : ", value="убить участника", inline=False)
    embed2.add_field(name=f"kiss [@участник] : ", value="поцеловать участника", inline=False)
    embed2.add_field(name=f"lick [@участник] : ", value="лизнуть пользователя", inline=False)
    embed2.add_field(name=f"pat [@участник] : ", value="погладить участника", inline=False)
    embed2.add_field(name=f"slap [@участник] : ", value="дать пощечину участнику", inline=False)
    embed2.add_field(name=f"smile : ", value="улыбнуться", inline=False)
    embed2.add_field(name=f"smug : ", value="выглядеть самодовольно", inline=False)
    embed2.add_field(name=f"wave [@участник] : ", value="приветствовать участника", inline=False)
    embed2.add_field(name=f"wink [@участник] : ", value="подмингнуть участнику", inline=False)
    embed2.set_footer(text='РП - (Role Play)ролевые игры.')

    message = await ctx.send(embed=embed1)
    message = await ctx.send(embed=embed2)
    counter_cmds =+ 1


#проверит пинг
@bot.command(name='ping') #работает
async def ping(ctx):
    start = time.perf_counter()
    end = time.perf_counter()
    latency = (end - start) * 1000
    embed = discord.Embed(title = f"🏓Pong!", description = f"Пинг: {latency:.2f} ms", color=discord.Color(0xFFFFFF))
    message = await ctx.send(embed=embed)
    counter_cmds =+ 1

#выдать роль
@bot.command(name='role')
@commands.has_permissions(manage_roles=True)
async def role(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    counter_cmds =+ 1

#укусить
@bot.command(name='bite')
async def bite(ctx,member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} укусил(а) {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://media.tenor.com/greMiXEBwRMAAAAC/love-kiss.gif')
    embed.set_footer(text='Больно!')
    await ctx.channel.send(embed=embed)
    counter_cmds =+ 1

#покраснеть
@bot.command(name='blush')
async def blush(ctx):
    embed = discord.Embed(title=f'{ctx.author.name} покаснел!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://media.tenor.com/Ed5IC_yxZkoAAAAd/miku-nakano-gotoubun-no-hanayome.gif')
    embed.set_footer(text='Видемо ему стыдно...')
    await ctx.channel.send(embed=embed)
    counter_cmds =+ 1

#заплакать
@bot.command(name='cry')
async def cry(ctx):
    embed = discord.Embed(title=f'{ctx.author.name} плачет!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://media.tenor.com/5G8NY4J2I40AAAAd/lena-vladilena-milize.gif')
    embed.set_footer(text='Море слез!')
    await ctx.channel.send(embed=embed)
    counter_cmds =+ 1

#прижаться к кому то
@bot.command(name='cuddle')
async def cuddle(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} прижался к {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://media.tenor.com/RHJyZDF9eC4AAAAC/anime.gif')
    embed.set_footer(text='Милашки!')
    await ctx.channel.send(embed=embed)
    counter_cmds =+ 1

#танцевать
@bot.command(name='dance')
async def dance(ctx):
    embed = discord.Embed(title=f'{ctx.author.name} танцует!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://media.tenor.com/OqOWJ0nsAlIAAAAd/dance-anime-dance.gif')
    embed.set_footer(text='Дискотека!')
    await ctx.channel.send(embed=embed)
    counter_cmds =+ 1

#покорми кого то
@bot.command(name='feed')
async def feed(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} накормил {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://media.tenor.com/2GdPghU41p8AAAAd/anime-dororo.gif')
    embed.set_footer(text='Вкусняшка!')
    await ctx.channel.send(embed=embed)
    counter_cmds =+ 1

#ударить когото
@bot.command(name='hit')
async def hit(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} ударил {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://media.tenor.com/Y8_ITfFMQmMAAAAC/yue-arifureta.gif')
    embed.set_footer(text='Какой дерзкий!')
    await ctx.channel.send(embed=embed)
    counter_cmds =+ 1

#обнять когото
@bot.command(name='hug')
async def hug(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} обнял {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://media.tenor.com/kCZjTqCKiggAAAAC/hug.gif')
    embed.set_footer(text='Никуда не убежишь!')
    await ctx.channel.send(embed=embed)
    counter_cmds =+ 1

#убить когото 
@bot.command(name='kill')
async def kill(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} убил {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://media.tenor.com/NbBCakbfZnkAAAAC/die-kill.gif')
    embed.set_footer(text='Сколько крови!')
    await ctx.channel.send(embed=embed)
    counter_cmds =+ 1

#поцеловать
@bot.command(name='kiss')
async def kiss(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} поцеловал {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://media.tenor.com/9--9GyBOu2gAAAAC/love-cute.gif')
    embed.set_footer(text='Не мешайте парочке!')
    await ctx.channel.send(embed=embed)
    counter_cmds =+ 1

#облизать
@bot.command(name='lick')
async def lick(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} лизнул {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://media.tenor.com/Pb1JPfqXpAIAAAAC/lick-licky.gif')
    embed.set_footer(text='Вся щека в слюнях!')
    await ctx.channel.send(embed=embed)
    counter_cmds =+ 1

#погладить
@bot.command(name='pat')
async def pat(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} погладил {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://media.tenor.com/pvF8xcytu1YAAAAC/pat.gif')
    embed.set_footer(text='Милота!')
    await ctx.channel.send(embed=embed)
    counter_cmds =+ 1

#пощечина
@bot.command(name='slap')
async def slap(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} сделал пощечину {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://media.tenor.com/XiYuU9h44-AAAAAC/anime-slap-mad.gif')
    embed.set_footer(text='Аж за звезды из глаз!')
    await ctx.channel.send(embed=embed)
    counter_cmds =+ 1

#улыбка
@bot.command(name='smile')
async def smile(ctx):
    embed = discord.Embed(title=f'{ctx.author.name} улыбнулся!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://media.tenor.com/W-b2SyPl7iEAAAAC/anime-smile.gif')
    embed.set_footer(text='Улыбка до ушей!')
    await ctx.channel.send(embed=embed)
    counter_cmds =+ 1

#самодовольный
@bot.command(name='smug')
async def smug(ctx):
    embed = discord.Embed(title=f'{ctx.author.name} выглядит самодовольным!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://media.tenor.com/YMZ7DvHPW00AAAAC/albedo-albedo-overlord.gif')
    embed.set_footer(text='Уверен в себе!')
    await ctx.channel.send(embed=embed)
    counter_cmds =+ 1

#поприветствовать
@bot.command(name='wave')
async def slap(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} поприветствовал {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://media.tenor.com/1MfQk9vFF7MAAAAC/anime-bye-bye-maki.gif')
    embed.set_footer(text='И тебе здравтсвуй!')
    await ctx.channel.send(embed=embed)
    counter_cmds =+ 1

#подмигнуть
@bot.command(name='wink')
async def wink(ctx, member: discord.Member):
    embed = discord.Embed(title=f'{ctx.author.name} подмигнул {member}!', color=discord.Color(0xFFFFFF))
    embed.set_image(url='https://media.tenor.com/3a3XcQUCFPkAAAAC/lycoris-recoil-chisato-nishikigi.gif')
    embed.set_footer(text='о_-!')
    await ctx.channel.send(embed=embed)
    counter_cmds =+ 1


@bot.command(name='avatar')
async def on_slash_command(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author
    avatar_url = user.avatar.url  # Получаем URL аватара пользователя
    # Создаем и отправляем эмбед с аватаром пользователя
    embed = discord.Embed(title=f'Аватар {user.name}', color=discord.Color(0xFFFFFF))
    embed.set_image(url=str(avatar_url))
    await ctx.send(embed=embed)
    counter_cmds =+ 1

@bot.event
async def on_raw_reaction_add(payload):
    guild_id = payload.guild_id
    guild = bot.get_guild(guild_id)
    user_id = payload.user_id
    channel_id = payload.channel_id
    channel = guild.get_channel(channel_id)
    message_id = payload.message_id
    message = await channel.fetch_message(message_id)
    emoji = payload.emoji.name

    reaction_role_map = {
        "silver": 1093610127409565836,
        "gold_nova": 1093610184850546698, 
        "master_guardian": 1093610240928383148,
        "distinguished_master_guardian": 1093610416548098198,
        "legendary_eagle": 1093610559263490121,
        "supreme_master_first_class": 1093610659826106400,
        "the_global_elite": 1093610680369811537,
    }

    if emoji in reaction_role_map:
        role_id = reaction_role_map[emoji]
        role = guild.get_role(role_id)
        member = guild.get_member(user_id)
        if role is not None and member is not None:
            await member.add_roles(role)




bot.run('MTA5MzUzMTY2NjM3MjM3ODcxNQ.GVpXKY.IICOQZoiocquyqDgRSTbguLbzi8K0j2huKNZ3Y')