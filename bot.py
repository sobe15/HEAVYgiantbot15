import discord
import asyncio
import openpyxl
import datetime
import random
import os
import sys
import json
import urllib
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote
import warnings
import re




client = discord.Client()



tierScore = {
    'default' : 0,
    'iron' : 1,
    'bronze' : 2,
    'silver' : 3,
    'gold' : 4,
    'platinum' : 5,
    'diamond' : 6,
    'master' : 7,
    'grandmaster' : 8,
    'challenger' : 9
}
def tierCompare(solorank,flexrank):
    if tierScore[solorank] > tierScore[flexrank]:
        return 0
    elif tierScore[solorank] < tierScore[flexrank]:
        return 1
    else:
        return 2
warnings.filterwarnings(action='ignore')



opggsummonersearch = 'https://www.op.gg/summoner/userName='


def deleteTags(htmls):
    for a in range(len(htmls)):
        htmls[a] = re.sub('<.+?>','',str(htmls[a]),0).strip()
    return htmls





@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game('헵자야 도움말')
    await client.change_presence(status=discord.Status.online, activity=game)








@client.event
async def on_message(message):



    if message.content.startswith('헵자야 도움말') or message.content.startswith('헵자야 도움'):
      embed = discord.Embed(title="명령어", description="", color=0xffc0cb)
      embed.add_field(name="헵자야 안녕", value="헵자가 인사를 해줘요", inline=False)
      embed.add_field(name="헵자야 내정보", value="헵자가 내정보를 알려줘요", inline=False)
      embed.add_field(name="h!번역", value="한글을 영어로 번역해줘요", inline=False)
      embed.add_field(name="헵자야 유튜브", value="헵자가 유튜브 링크를 알려줘요", inline=False)
      embed.add_field(name="헵자야 트위치", value="헵자가 트위치 링크를 알려줘요", inline=False)
      embed.add_field(name="헵자야 트위터", value="헵자가 트위터 링크를 알려줘요", inline=False)
      embed.add_field(name="헵자야 인스타", value="헵자가 인스타 링크를 알려줘요", inline=False)
      embed.add_field(name="헵자야 미니게임", value="추가 예정", inline=False)
      embed.set_footer(text='!SOBI#1919 , Hode_#0193',
                      icon_url='https://images-ext-1.discordapp.net/external/6CqUJxds58RfdVG_gjKOgIzJphb8I98lb7sBU5AUMJQ/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/657568177802444821/a150cd6578f6bb972f0ae65ed01dabdc.webp?width=645&height=645')
      embed.set_thumbnail(url="https://media.discordapp.net/attachments/787611001390497832/787612375767187456/heavygiant.png?width=676&height=676")
      await message.channel.send(embed=embed)


    if message.content.startswith('헵자야 생년월일'):
      embed = discord.Embed(title="HEAVYgiant", description="HEAVYgiant#0217", color=0xffc0cb)
      embed.add_field(name="2005년", value="2월 17일", inline=False)
      embed.set_footer(text='!SOBI#1919 , Hode_#0193',
                    icon_url='https://images-ext-1.discordapp.net/external/6CqUJxds58RfdVG_gjKOgIzJphb8I98lb7sBU5AUMJQ/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/657568177802444821/a150cd6578f6bb972f0ae65ed01dabdc.webp?width=645&height=645')
      embed.set_thumbnail(url="https://media.discordapp.net/attachments/787611001390497832/787612375767187456/heavygiant.png?width=676&height=676")
      await message.channel.send(embed=embed)


    if message.content == "헵자야 내정보":
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"""
{message.author.mention}님의 정보  
```cs
이름: {user}  
디스코드 가입일: {date.year}/{date.month}/{date.day}
```
        """)


    if message.content.startswith('헵자야 시계'):
      await message.channel.send(embed=discord.Embed(title="헵자 시계", timestamp=datetime.datetime.utcnow()))

    if message.content == "헵자야 내프사":
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{user.avatar_url}")




















    if message.content.startswith('h!번역'):
        learn = message.content.split(" ")
        Text = ""

        client_id = "XdFODz54KbGOhS0tlVGI"
        client_secret = "xFRQU4zpUA"

        url = "https://openapi.naver.com/v1/papago/n2mt"
        print(len(learn))
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(1, vrsize): #띄어쓰기 한 텍스트들 인식함
            Text = Text+" "+learn[i]
        encText = urllib.parse.quote(Text)
        data = "source=ko&target=en&text=" + encText

        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)

        response = urllib.request.urlopen(request, data=data.encode("utf-8"))

        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            data = response_body.decode('utf-8')
            data = json.loads(data)
            tranText = data['message']['result']['translatedText']
        else:
            print("Error Code:" + rescode)

        print('번역된 내용 :', tranText)

        embed = discord.Embed(
            title='한글->영어 번역결과',
            description=tranText,
            colour=discord.Colour.green()
        )
        await message.channel.send(embed=embed)





















    #잡




    #실검


    #
    if message.content.startswith('헵자야 파이썬'):
      await message.channel.send("""
    ```py
    print("헵자봇 제작자 멍청이임")
    ```
    """)

    if message.content.startswith('헵자야 미니게임'):
      await message.channel.send('마! 추가 예정이다! 기다리라! 마! (?)')

    



    #롤 전적













    #대화
    if message.content.startswith('헵자야 유튜브'):
      await message.channel.send('https://www.youtube.com/channel/UCFcFcyR8VmVg43RdGTiN3kQ')

    if message.content.startswith('헵자야 트위치'):
      await message.channel.send('https://www.twitch.tv/heavygiant217')

    if message.content.startswith('헵자야 트위터'):
      await message.channel.send('https://twitter.com/heavygiant217')

    if message.content.startswith('헵자야 디코') or message.content.startswith('헵자야 디스코드'):
      await message.channel.send('https://discord.gg/gUTAY9Cqbc')

    if message.content.startswith('헵자야 인스타'):
      await message.channel.send('https://instagram.com/heavygiant?igshid=1ewywjzmyfdwy')


    if message.content.startswith('헵자야 안녕'):
      await message.channel.send('ㅎㅇㅎㅇ')

    if message.content.startswith('헵자야 바보'):
      await message.channel.send('힝')

    if message.content.startswith('헵자야 송강욱 고인물'):
      await message.channel.send('?')

    if message.content.startswith('헵자야 마인크래프트'):
      await message.channel.send('갓똥겜')

    if message.content.startswith('헵자야 멍청이'):
      await message.channel.send('힝 나빠써 ㅠㅜ')

    if message.content.startswith('헵자야 힝'):
      await message.channel.send('히ㅇ이이이이이이이이이이이이잉ㅜㅠㅜㅠㅜㅠㅜㅠㅜㅠㅜㅜㅠㅜㅠㅜㅠㅜㅠㅜㅠㅜㅠㅜㅠㅜㅠ')

    if message.content.startswith('헵자야 귀여워'):
      await message.channel.send('뀨?')

    if message.content.startswith('헵자야 애교'):
      await message.channel.send('아잉아잉아잉아잉 이이이잉 잉 이 잉!!!!!!!!!')

    if message.content.startswith('헵자야 뀨'):
      await message.channel.send('뀨!! 뀨!!')

    if message.content.startswith('헵자야 헵자'):
      await message.channel.send('머요')

    if message.content.startswith('헵자야 멍뭉'):
      await message.channel.send('멍뭉!💕 멍뭉!💕')

    if message.content.startswith('헵자야 사랑해'):
      await message.channel.send('나듀 사량해 💕💕')

    if message.content.startswith('헵자야 나이'):
      await message.channel.send('17')

    if message.content.startswith('헵자야 생일'):
      await message.channel.send('2월 17일')

    if message.content.startswith('헵자야 냥'):
      await message.channel.send('냥!')

    if message.content.startswith('헵자야 멍멍'):
      await message.channel.send('멍❤')

    if message.content.startswith('헵자야 솝이'):
      await message.channel.send('멍청한 개발자')

    if message.content.startswith('헵자야 소비'):
      await message.channel.send('멍청한 개발자')

    if message.content.startswith('헵자야 소비를 어떻게 생각해'):
      await message.channel.send('소비바부')

    if message.content.startswith('헵자야 ㅡㅡ'):
      await message.channel.send('ㅡㅡ')

    if message.content.startswith('헵자야 ㄷㄷ'):
      await message.channel.send('ㅎㄷㄷ')

    if message.content.startswith('헵자야 ㄱㄱ'):
      await message.channel.send('ㄱㄱ~')

    if message.content.startswith('헵자야 샌즈'):
      await message.channel.send('https://ww.namu.la/s/c80fdba0c6ddeb12406e44c16cb11af88a33a04e67b9a7a171a5112db448c41d505c52a9c7e01ddad827d0dabde3d1d1fd8608ff85e5a7bd771725283678b05f8f04f1d7580f7e9829b618863a010f0f920bd6ee5b84d7cb9dfba0bd14365f76')

    if message.content.startswith('헵자 쌉굇'):
      await message.channel.send('내가 좀 고인물이긴 하지')

    















client.run()
