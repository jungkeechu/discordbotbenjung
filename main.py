# bot.py
import discord
import os

TOKEN = os.getenv("DISCORD_TOKEN")

# error  !!!! 
# client = discord.Client()
# TypeError: __init__() missing 1 required keyword-only argument: 'intents'
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == "Chat-Bot-Test":
            break

    print(f'{client.user} has connected to the following guild:\n',
        f'{guild.name}(id:{guild.id})'
    )


client.run(TOKEN)
