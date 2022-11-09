import discord
from discord.ext import commands
import random

bot = commands.Bot(intents=discord.Intents.all() , command_prefix= "!" , description='The Best Bot For the Best User!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    game = discord.Game("!!명령어")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == '!!명령어':
        embed = discord.Embed(title='명령어', description=' ', color=discord.Color.random())
        embed.add_field(name="!주사위6", value="1~6의 주사위를 굴립니다.", inline=False)
        embed.add_field(name="!주사위10", value="1~10의 주사위를 굴립니다.", inline=False)
        embed.add_field(name="!주사위50", value="1~50의 주사위를 굴립니다.", inline=False)
        embed.add_field(name="!주사위100", value="1~100의 주사위를 굴립니다.", inline=False)
        embed.add_field(name="!홀짝", value="홀수 또는 짝수를 고릅니다.", inline=False)
        embed.set_thumbnail(url="https://imgur.com/FilnlKm.jpg")
        await message.channel.send(embed=embed)

    if message.content == '!주사위6':
        a = random.randint(1,6)
        await message.channel.send(f"나온 눈금 : {a}")

    if message.content == '!주사위10':
        a = random.randint(1,10)
        await message.channel.send(f"나온 눈금 : {a}")

    if message.content == '!주사위50':
        a = random.randint(1,50)
        await message.channel.send(f"나온 눈금 : {a}")

    if message.content == '!주사위100':
        a = random.randint(1,100)
        await message.channel.send(f"나온 눈금 : {a}")

    if message.content == "!홀짝":
        a = random.randint(1, 2)
        if a == 1:
            await message.channel.send("홀")
        else:
            await message.channel.send("짝")

@bot.event
async def on_typing(channel, user, when):
    print(channel) # 채널 이름
    print(user) # 유저 닉네임
    print(when) # 날짜 및 시간

bot.run('MTAzOTQ2MjQyOTI1NzY0NjE0MA.GXwswr.06sV56Y1tOGMDbPi6ngv6vf9mIX-vUfE3BCaOA')
