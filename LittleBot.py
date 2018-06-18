import discord
import asyncio
import random
import pickle
import os

client = discord.Client()

@client.event
async def on_ready():
	print("ONLINE! LITTLE!")

@client.event
async def on_message(message):
	if message.content.startswith('리틀아' and '누구야'):
		cc = random.choice(['저요? 저는 리틀이라고 해요.. 아직 학생이지만 무시하지 말아줘요..', '안녕 리틀이라고 해요!', '안뇽~ 리틀이에요 요즘 학교 때문에 너무 힘드네요 ㅠ..', '안녕! 반가워.. 내가 누구냐고? 그러게 나도 내가 누군지 모르겠어 ..', '안녕, 리틀이라고 해 요즘 공부 너무 힘들다', '난 리틀이라고 해..', '누군긴 누구야 리틀이지'])
		await client.send_message(message.channel, cc)
	elif message.content.startswith('리틀아' and '양비카' and '생각해'):
		cc = random.choice(['양비카 님에 대해선.. 별생각 없어요 ㅎ..', '양비카가 누구였더라.. 물건인가? 사람이름은 아닌것 같은데..', '양비카님이 누군지도 몰라..', '양비카! 양비카! 양비카.. 나도 몰라..', '양비카라는 것에 대해선 좋게 생각하고 있어.. 아마도..', '비카? 비커인가..', '.. 양비카?'])
		await client.send_message(message.channel, cc)

client.run(os.getenv('TOKEN'))










































client.run("NDU3NzIwMTAwODQyMjQyMDQ4.DgfVWQ.VP795bpF6WmbESxOgYMmi69PbIo")
