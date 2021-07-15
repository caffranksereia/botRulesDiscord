import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
import rules


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


client = commands.Bot(command_prefix = '!', intents = discord.Intents.all())

@client.event
async def on_ready():
# print no cmd id_guild e id client_user
 for guild in client.guilds:
        if guild.name == GUILD:
            break
        print(f'Entrei {client.user} Yes!,my lord \n {guild.name} (id:{guild.id})')



'''class Members(commands.MemberConverter):
    async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument)
        return [role.name for role in member.roles[1:]]
@client.command()
async def roles(ctx,*, member:Members):
    """Tells you member's roles"""
    await ctx.send('I see the following roles:'+','.join(member))
'''





client.run(TOKEN) #cliente roda recebendo o paramentro do TOKEN que foi recebido la em cima.