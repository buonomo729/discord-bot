# bot.py
import os

import discord
import csv
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

    with open('avrae_messages.csv','w',newline='',encoding='utf-8') as csvfile:
        fieldnames = ['author','fields','color','type','description','title','thumbnail','footer','image']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for channel in guild.text_channels:
            messages = await channel.history(limit=200).filter(lambda m: m.author.name == 'Avrae').flatten()
            print(
                f'Channel: {channel.name} - Avrae Message #{len(messages)}'
            )
            for m in messages:
                if len(m.embeds) > 0:
                    writer.writerow(m.embeds[0].to_dict())
                    print(
                      f'{m.embeds[0].to_dict()}\n' 
                    )

client.run(TOKEN)
