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
	if message.content.startswith('리틀'):
		await client.send_message(message.channel, '안녕!')

client.run(os.getenv('TOKEN'))












































client.run("NDU3NzIwMTAwODQyMjQyMDQ4.DgfVWQ.VP795bpF6WmbESxOgYMmi69PbIo")
