DISCORD_TOKEN = "USE YOUR DISCORD TOKEN"

# This example requires the 'message_content' intent.

import discord
import FetchCiv

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    #unfinished feature to add AI Images
    if message.content.startswith('!imagine'):
        await message.channel.send('Image:', file=discord.File('ImagineImage\download.jpeg'))

    elif message.content.startswith('!'):
        cleanmessage = (message.content).lstrip("!").lower().capitalize()
        content = FetchCiv.civilization(cleanmessage)
        await message.channel.send(content)
    
    

client.run(DISCORD_TOKEN)
