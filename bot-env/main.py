import json
import discord
from discord.ext import commands


with open ('config.json') as e:
    infos = json.load(e)
    TOKEN = infos['token']
    prefix = infos['prefix'] 

client = commands.Bot(command_prefix = prefix ,intents = discord.Intets.all())

client.run(TOKEN)

