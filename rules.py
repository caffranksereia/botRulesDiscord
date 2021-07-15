import discord
from discord.ext import commands

class adminSebas():
    def __init__(self,adminSebas):
        self.adminSebas = adminSebas




@client.command()
async def Sebas(ctx):
        await ctx.send("Yes,my lord")

@client.command()
async def ban(ctx, members: commands.Greedy[discord.member], delete_days: typing.Optional[int] = 0, *, reason: str):
        for member in members:
            await member.ban(delete_message_days=delete_days, reason=reason)

