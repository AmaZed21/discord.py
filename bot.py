import discord 
from discord.ext import commands, tasks
from random import choice

from music import music_cog

client = commands.Bot(command_prefix='') # insert your bot's command prefix
status = [''] # insert your bot's status
client.add_cog(music_cog(client))

@client.event
async def on_ready(): #start-up
    change_status.start()
    print("Bot is ready")

@tasks.loop(seconds=10) #discord status
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

TOKEN = # insert your token id from discord developer portal
client.run(TOKEN)