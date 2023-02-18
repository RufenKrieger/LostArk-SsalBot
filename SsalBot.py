import discord
import random
import math
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('!사용법'))
    print("SsalBot Online")

@bot.command()
async def 사용법(ctx):
    await ctx.message.delete()
    await ctx.author.send(f'>>> ```!쌀산기 !쌀 !분배 !분```\n ***명령어를 이용하여 골드 분배를 편하게 할 수 있습니다.***\n\n 예시) 시장가 **5000 골드**인 아이템을 **8인 파티**에서 분배```!쌀산기 5000 8``````!쌀 5000 8``````!분배 5000 8``````!분 5000 8```\n예시) 시장가 **3000 골드**인 아이템을 **4인 파티**에서 분배```!쌀산기 3000 4``````!쌀 3000 4``````!분배 3000 4``````!분 3000 4```\n')
    


@bot.command(aliases=['쌀','Tkf','Tkftksrl','분배','분'])
async def 쌀산기(ctx,gold = None, mancount = None):
    
    await ctx.message.delete()
    try:
        if gold == None and mancount != None:
            await ctx.send(f'>>> <@{ctx.author.id}> 님, 골드 값을 포함하여 명령어를 사용해주세요! \n!사용법\n입력된 명령어: **{ctx.message.content}**')

        elif gold != None and mancount == None:
            await ctx.send(f'>>> <@{ctx.author.id}> 님, 인원 수를 포함하여 명령어를 사용해주세요! \n!사용법\n입력된 명령어: **{ctx.message.content}**')

        elif int(mancount) < 2:
            await ctx.send(f'>>> <@{ctx.author.id}> 님, 인원 수 입력이 잘못 되었습니다. 명령어를 다시 한번 확인해주세요! \n!사용법\n입력된 명령어: **{ctx.message.content}**')

        elif int(mancount) >= 2:
            ssalresult = int(gold) * 0.95 * ((int(mancount)-1) / int(mancount)) / 1.1
            equalresult = int(gold) * 0.95 * ((int(mancount)-1) / int(mancount))
            equalgold = int(gold)* 0.95 / int(mancount)
            await ctx.send(f'>>> <@{ctx.author.id}> 님이 요청해주신 **{int(gold)} 골드**에 대한 **{int(mancount)}인** 파티 계산 금액\n\n경매 최적가 : **{int(ssalresult)} 골드**\n균등 분배가 : **{int(equalresult)} 골드** | 1인당 분배 골드 : **{int(equalgold)} 골드**')
    except:
        await ctx.send(f'>>> <@{ctx.author.id}> 님, 명령어 사용법을 숙지후 사용해주세요! \n!사용법\n입력된 명령어: **{ctx.message.content}**')

bot.run("Token")