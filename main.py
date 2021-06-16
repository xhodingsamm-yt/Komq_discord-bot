import discord
import urllib.request
import asyncio
import os
import random
import re
from discord.ext import tasks
import datetime
import youtube_dl
from youtube_dl import *
import time
from discord.ext import commands
client1 = discord.Client()
dirctory = os.path.dirname(__file__)  # 이곳부턴 기존 if문 내에 추가해 주시면 됩니다.

def ydl(url):
    ydl_opts = {  # 다운로드 옵션
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'song.mp3',  # 파일 이름
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])  # 다운로드

class chatbot(discord.Client):
    async def on_ready(self):
        # 상태 메시지 설정
        # 종류는 3가지: Game, Streaming, CustomActivity
        game = discord.Game("배드워즈")

        # 계정 상태를 변경한다.
        # 온라인 상태, game 중으로 설정
        await client.change_presence(status=discord.Status.online, activity=game)

        # 준비가 완료되면 콘솔 창에 "READY!"라고 표시
        print("READY")

    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message):
        # SENDER가 BOT일 경우 반응을 하지 않도록 한다.
        if message.author.bot:
            return None

        # message.content = message의 내용
        if message.content == "?바보":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "너도 바보"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        if message.content == "너도 바보":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "칫"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        if message.content == "코마야":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "응애 나는 아기 코마\n왜"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        if message.content == "코마 바보":
                channel = message.channel

                msg = "ㅠ"
                await channel.send(msg)
                return None
        if message.content == "코마 멍청이":
                channel = message.channel

                msg = "그러지마! ㅠ"
                await channel.send(msg)
                return None
        if message.content == "코마 쓸대없음":
                channel = message.channel

                msg = "[코마 삐짐]"
                await channel.send(msg)
                return None
        if message.content == "코마 쓸때없음":
                channel = message.channel

                msg = "[코마 삐짐]"
                await channel.send(msg)
                return None

        if message.content == "오늘 5월 5일임":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "응얘 나 어린이 꼼큐\n선물 내놔"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        #🎁
        if message.content == "🎁":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "먹튀할께 수고"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        if message.content == "!정보":
            channel = message.channel
            # 이미지를 지정한 URL에서 다운로드하여, "explain.png"로 저장
            urllib.request.urlretrieve(
                "https://yt3.ggpht.com/ytc/AAUvwnht6xOqz-q1WE1lvCiw25dzq7rq9GChctMSGfwcIA=s176-c-k-c0x00ffffff-no-rj-mo", "explain.png")

            # 디스코드에 올릴 파일을 지정하고, attachment에서 사용할 이름을 "image.png"로 지정
            image = discord.File("explain.png", filename="image.png")

            # Embed 메시지 구성
            embed = discord.Embed(title="정보", description="코마봇 BETA - Maded by 초딩쌤", color=0x00ff56)
            # 아까 지정한 파일 이름으로 해야함.
            embed.set_thumbnail(url="attachment://image.png")
            embed.add_field(name="명령어", value="?바보\n!정보", inline=True)
            embed.add_field(name="기능", value="욕설 필터링\n와이파이 핑 감지", inline=True)
            embed.add_field(name="놀이", value="가위바위보 (!가위바위보)", inline=True)

            # 메시지 보내기
            await channel.send(embed=embed, file=image)
        if message.content== "ㅅㅂ":
            channel = message.channel
            msg1 = "욕설 ㄴㄴ"
            await channel.send(msg1)
            await message.delete()
        if message.content == "!핑":
            channel = message.channel
            random1 = random.randint(1,10)
            msg2 = "연결 상태가 좋아요! 😊 '7ms'"
            await channel.send(msg2)
        if message.content == ('!가위바위보'):
            rsp = ["가위", "바위", "보"]
            embed = discord.Embed(title="가위바위보😎", description="가위바위보를 합니다. 3초내로 (가위/바위/보)를 써주세요!", color=0x00aaaa)
            channel = message.channel
            msg1 = await message.channel.send(embed=embed)

            def check(m):
                return m.author == message.author and m.channel == channel

            try:
                msg2 = await client.wait_for('message', timeout=3.0, check=check)
            except asyncio.TimeoutError:
                await msg1.delete()
                embed = discord.Embed(title="가위바위보", description="앗 3초가 지났네요...!", color=0x00aaaa)
                await message.channel.send(embed=embed)
                return
            else:
                await msg1.delete()
                bot_rsp = str(random.choice(rsp))
                user_rsp = str(msg2.content)
                answer = ""
                if bot_rsp == user_rsp:
                    answer = "난 " + bot_rsp + "을 냈고, 넌 " + user_rsp + "을 내으니까.\n" + "비겼네😁"
                elif (bot_rsp == "가위" and user_rsp == "바위") or (bot_rsp == "보" and user_rsp == "가위") or (
                        bot_rsp == "바위" and user_rsp == "보"):
                    answer = "난 " + bot_rsp + "을 냈고, 넌 " + user_rsp + "을 내으니까.\n" + "아쉽지만 내가 졌네....😂"
                elif (bot_rsp == "바위" and user_rsp == "가위") or (bot_rsp == "가위" and user_rsp == "보") or (
                        bot_rsp == "보" and user_rsp == "바위"):
                    answer = "난 " + bot_rsp + "을 냈고, 넌 " + user_rsp + "을 냈으니까.\n" + "내가 이겼다! ㅋㅋㄹㅃㅃ"
                else:
                    embed = discord.Embed(title="가위바위보", description="가위, 바위 , 보 중에만 내", color=0x00aaaa)
                    await message.channel.send(embed=embed)
                    return
                embed = discord.Embed(title="가위바위보", description=answer, color=0x00aaaa)
                await message.channel.send(embed=embed)
                return
        if message.content == "?debug":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "You are in debug mode. Please use  ?cancel  to exit the debug mode."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        if message.content == "?cancel":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "디버그 모드가 꺼졌습니다."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        if message.content == "코마야 10억 줄께":

            file = discord.File("C:\\Users\\koko7\\PycharmProjects\\komq\\a.mp3")
            await message.channel.send(file=file)
@client1.event
async def on_message(message):
    if message.content.startswith("/입장"):
        await message.author.voice.channel.connect()
        await message.send("보이스채널에 입장합니다.")
    if message.content.startswith("/퇴장"):
        for vc in bot.voice.clients:
            if vc.guild == message.guild:
                voice = vc
        await voice.disconnect()
        await message.channel.send("보이스채널에 퇴장합니다.")
    if message.content.startswith("/재생"):
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc
        url = message.content.split(" ")[1]
        option = {
            'outtmpl' : "file/" + url.split('=')[1] + ".mp3"
        }
        with youtube_dl.YoutubeDL(option) as ydl:
            ydl.download(url)
            info = ydl.extract_info(url, download=False)
            title = info["title"]
        voice.play(discord.FFmpegPCMAudio("file/" + url.split('=')[1] + ".mp3"))
        await message.channel.send(title + "을 재생합니다.")


if __name__ == "__main__":
    # 객체를 생성()
    client = chatbot()
    access_token= os.environ["BOT_TOKEN"]
    # TOKEN 값을 통해 로그인하고 봇을 실행
    client.run(access_token)
