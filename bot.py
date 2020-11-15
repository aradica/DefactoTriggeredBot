# bot.py from https://realpython.com/how-to-make-a-discord-bot-python/

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_message(message):
    lower = message.content.lower()
    if "defacto" in lower or "de facto" in lower:
        # TODO add multiple randomly chosen responses
        response = "🤬!?tRiGGerEd?!🤬"
        await message.channel.send(response)

client.run(TOKEN)
