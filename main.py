# bot.py
import os
import random
import discord


# you need these 2 stsatemtn only for PC app
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# error  !!!! 
# you need to fix it !!!
# client = discord.Client()
# TypeError: __init__() missing 1 required keyword-only argument: 'intents'
# and Dicord API is changing always... ^^
intents=discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'{client.user} has connected to the following guild:\n',
        f'{guild.name}(id:{guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


# !!!!!`
# you have to change 'MESSAGE CONNTEN INTENT" to True
# @ dicord deceloper page
# !!!!!
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'hi':
        await message.channel.send('hello')
    elif message.content == 'i miss you':
        await message.channel.send("me too, I miss you too")

client.run(TOKEN)
