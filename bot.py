import os

import discord
from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.ext.commands import has_permissions,MissingPermissions
import asyncio
from dotenv import load_dotenv
import rules


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHAT_TXT = os.getenv('DISCORD_WELCOME')
REGRAS_CHANNEL = os.getenv('RULES')
GET_HELP = os.getenv('help')


client = commands.Bot(command_prefix = '!', intents = discord.Intents.all())

@client.event
async def on_ready():
# print no cmd id_guild e id client_user
 for guild in client.guilds:
        if guild.name == GUILD:
            break
        print(f'Entrei {client.user} Yes!,my lord \n {guild.name} (id:{guild.id})')

@client.command()
async def Sebas(ctx):
        await ctx.send("Yes,my lord")
'''
@client.command(name= 'help')
async def new_on_members(ajuda):
    ajuda = client.get_channel(GET_HELP)
    await client.send(f'comando de ajudas aqui my lord.{ajuda}')'''

@client.command()
async def on_rules(ctx):
    await ctx.send(f"Essas são as regras{REGRAS_CHANNEL}")

@client.command(name='membros')
async def on_all_members(ctx):
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    await ctx.send(f'todos os membros {guild.name}: \n -{members}')


@client.command(name='h')
async def list_help(ctx):
    await ctx.send('lista de comandos:\n membros = !membros,\n ban = !ban,\n permaban = !perma')

@client.command(name='ban')
@has_permissions(kick_members = True)
async def punisher(ctx, member:discord.Member, *,reason=None):
    await member.kick(reason = reason)
    await ctx.send(f'Voce {member}  foi punido!')




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