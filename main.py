import discord
from discord.ext import commands
import music

cogs = [music]


client = commands.Bot(command_prefix='>>', intents = discord.Intents.all())

@client.event
async def on_ready():
     print("Bot is ready!!")

@client.event
async def on_member_join(member):
     print(f"{member} has joined the server.")

for i in range(len(cogs)):
     cogs[i].setup(client)
     

client.run("--------YOUR TOKEN HERE-------")