# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    
    # following completion of this for..in generator, guild var will be our Bun Discord Guild.
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
        f'Channels #{len(guild.channels)}'
    )

    for channel in guild.text_channels:
        messages = await channel.history(limit=200).filter(lambda m: m.author.name == 'Avrae').flatten()
        print(
            f'Channel: {channel.name} - Avrae Message #{len(messages)}'
        )
        for m in messages:
            if len(m.embeds) > 0:
                print(
                  f'{m.embeds[0].to_dict()}\n' 
                )

client.run(TOKEN)
