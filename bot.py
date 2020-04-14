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
    bunguild = await client.fetch_guilds(limit=10).find(lambda m: m.name == 'Bun')

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{bunguild.name}(id: {bunguild.id})'
    )

    client.get_all_channels()

    print(
        f'{len(bunguild.text_channels)}'
        f'{len(bunguild.channels)}'
    )


    for channel in bunguild.text_channels:
      messages = await channel.history(limit=200).filter(lambda m: m.author.name == 'Avrae').flatten()
      for message in messages:
        print(
            f'{message.content}'
        )
      break

client.run(TOKEN)
