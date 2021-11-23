import discord
import os

client = discord.Client()

@client.command()
async def invite_link():
  os.getenv("TOKEN")
  
client.run(os.getenv("TOKEN2"))
