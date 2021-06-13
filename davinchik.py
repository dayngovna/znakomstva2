import json
import os
import discord
from discord.ext import commands
import pytz
client = commands.Bot(command_prefix=">",intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
        activity=discord.Game("ekfara bot")) 
@client.command()
async def create(ctx,years,floor,*,im):#создать анкету
#https://ru.stackoverflow.com/questions/1187074/Как-делать-аргументы-в-несколько-слов-в-discord-py
    with open('datavinchik.json') as json_file:
        data = json.load(json_file)
        datafile = {
        'name': ctx.author.mention, 
        'years': years,
        'floor': floor,
        'im': im,
        'ava': str(ctx.author.avatar_url)}
        data.append(datafile)
    with open('datavinchik.json', 'w') as f:
        json.dump(data, f, indent=1)

    for x in data:
        if x['name'] == ctx.author.mention:
            await ctx.author.send("Все твои анкеты")
            embed = discord.Embed(title=f'Анкета '+x['name'])
            embed.set_thumbnail(url=x['ava'])
            embed.add_field(name="Возраст",value=x['years'])
            embed.add_field(name="Пол",value=x['floor'])
            embed.add_field(name="О себе",value=x['im'],inline=False)
            await ctx.author.send(embed=embed)
@client.command()
async def find(ctx,years):#поиск анкеты
    with open('datavinchik.json') as findfile:
        data = json.load(findfile)
        for xx in data:
            print(xx)
            if xx['years'] == str(years):
                print("finded!")
                embed = discord.Embed(title=f'Анкета '+xx['name'])
                embed.set_thumbnail(url=xx['ava'])
                embed.add_field(name="Возраст",value=xx['years'])
                embed.add_field(name="Пол",value=xx['floor'])
                embed.add_field(name="О себе",value=xx['im'],inline=False)
                await ctx.author.send(embed=embed)
            else:
                await ctx.author.send("Мы не нашли анкету,измените запрос")
@client.command()
async def ekfar(ctx):#help
    embed = discord.Embed(title="Это бот знакомств от экфара")
    embed.add_field(name="Бот работает через лс",value="Просто напиши ему команду",inline=False)
    embed.add_field(name="Чтобы создать анкету пропиши",value=">create возраст пол текст",inline=False)
    embed.add_field(name="Чтобы найти анкету по возрасту пропиши",value=">find возраст",inline=False)
    embed.add_field(name="Чтобы вызвать это меню пропиши",value=">ekfar",inline=False)
    embed.add_field(name="Удачного пользования!",value="Создан тут https://discord.gg/3qW8tGU9",inline=False)
    await ctx.send(embed=embed)
@client.command()
async def admindata():
    with open('datavinchik.json') as adfile:
        data = json.load(adfile)
        await ctx.autor.send(data)
client.run(os.environ['token'])
