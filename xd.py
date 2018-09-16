import discord
import time
from discord.ext import commands
from discord import Game
import asyncio
import random
import json
import aiohttp
import os
import datetime
from random import randint

Client = discord.Client()
client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Glitched 0.8"))
    print("Running.")

@client.command(pass_context=True)
async def Ping(ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await client.send_typing(channel)
    t2 = time.perf_counter()
    embed=discord.Embed(title=None, description='Ping= {}'.format(round((t2-t1)*1000)), color=0x36393E)
    await client.say(embed=embed)

@client.command(pass_context = True)
async def Say(ctx, *args):
    mesg = ' '.join(args)
    await client.delete_message(ctx.message)
    return await client.say(mesg)

@client.command(pass_context=True)
async def Info(ctx):
    embed = discord.Embed(
        title = 'info',
        description = '',
        colour = discord.Colour.red()
)
    embed.add_field(name='say', value='Example:{ .say hi', inline=False)
    embed.add_field(name='ping', value='Ping pong!', inline=False)
    embed.add_field(name='info', value='Shows info of the bot.', inline=False)
    embed.add_field(name='Mute', value='Mute [User]', inline=False)
    embed.add_field(name='Clear', value='Clear messages..', inline=False)
    embed.add_field(name='Kick', value='Kick [User]', inline=False)
    embed.add_field(name='Ban', value='Ban [User]', inline=False)
    embed.add_field(name='exam', value='Do the command and you will see.', inline=False)
    embed.add_field(name='school', value='School is hell.', inline=False)
    embed.add_field(name='funny', value='Lmao.', inline=False)
    embed.add_field(name='gay', value='Huh? Gay?', inline=False)
    embed.add_field(name='fight', value='Fite me.', inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/489117619304005658/489730513838538752/Untitled.png')
    embed.set_footer(text='Version 0.7')
    
    await client.say(embed=embed)

@client.command(pass_context=True)
async def Ban(ctx, user: discord.Member):
    if ctx.message.author.server_permissions.ban_members:
        embed = discord.Embed(banned="Banned user", description="{}".format(user.name),color=0x36393E)
        embed.add_field(name="User", value=user.name)
        embed.add_field(name="User ID",value=user.id)
        embed.add_field(name="Banned By", value=ctx.message.author.name, inline=True)
        await client.say(embed=embed)
        await client.ban(user)
    else:
        embed=discord.Embed(title="Error!", description="You do not have permissions.")
        await client.say(embed=embed)

@client.command(pass_context=True)
async def Kick(ctx, user: discord.Member):
    if ctx.message.author.server_permissions.kick_members:
        embed = discord.Embed(banned="Kicked user", description="{}".format(user.name),color=0x36393E)
        embed.add_field(name="User", value=user.name)
        embed.add_field(name="User ID",value=user.id)
        embed.add_field(name="Kicked By", value=ctx.message.author.name, inline=True)
        await client.say(embed=embed)
        await client.kick(user)
    else:
        embed=discord.Embed(title="Error!", description="You do not have permissions.")
        await client.say(embed=embed)
        

@client.command(pass_context=True)
async def Clear(ctx, limit: int=None):
     if ctx.message.author.server_permissions.manage_messages:
        async for msg in client.logs_from(ctx.message.channel, limit=limit):
         await client.delete_message (msg)
         embed = discord.Embed(description="GLITCHEDD",color=0x36393E)

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Members')
    await client.add_roles(member,role)

@client.command(pass_context=True)
async def mute(ctx, member: discord.Member):
    if ctx.message.author.server_permissions.administrator:
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member,role)
        embed = discord.Embed(banned="Muted user", description="{}".format(member.name),color=0x36393E)
        embed.add_field(name="User", value=member.name)
        embed.add_field(name="User ID",value=member.id)
        embed.add_field(name="Muted By", value=ctx.message.author.name, inline=True)
        await client.say(embed=embed)
    else:
        embed=discord.Embed(title="Error!", description="You do not have permissions.")
        await client.say(embed=embed)

@client.command(pass_context=True)
async def exam(ctx):
    await client.say("This is you during an exam:https://giphy.com/gifs/mr-bean-KKomJ7FjSgKBi")

@client.command(pass_context=True)
async def school(ctx):
    await client.say("This is you when you're late for school: https://giphy.com/gifs/mr-bean-Nde7zlveRCWPu")

@client.command(pass_context=True)
async def funny(ctx):
    await client.say("wtf: https://giphy.com/gifs/mr-bean-XiX5KGottJobK")

@client.command(pass_context=True)
async def ultragay(ctx):
    await client.say("so gay: https://giphy.com/gifs/lgbt-pride-nycpride-xTiTnGrd1CPhIs29wI")

    
@client.command(pass_context=True)
async def dance(ctx):
    await client.say("dance dance dance: https://giphy.com/gifs/mr-bean-4UwIfPbhq1GaQ")

@client.command(pass_context=True)
async def fight(ctx):
    await client.say("jew jitsu:https://giphy.com/gifs/dancing-mr-bean-rowan-atkinson-Qom9cN6sXkZmE")

@client.command(pass_context=True)
async def Botinfo(ctx):
    embed = discord.Embed(description="Info of The Bot",color=0x36393E)
    embed.add_field(name="Name Is", value=client.user.name)
    embed.add_field(name="BOT ID Is", value=client.user.id)
    embed.add_field(name="Owner Of The Bot", value="∆land.#8761")
    embed.add_field(name="Helper", value="Zero Helped me,so much so I have to add him")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def gay(ctx, member: discord.Member = None):
    if member is None:
        await client.say("Please specify a user.")
    else:
        rnd = random.randint(1, 100)
        embed = discord.Embed(title="{} is {}% gay! :gay_pride_flag: ".format(member.name, rnd), color=0x36393E)
        await client.say(embed=embed)
        
@client.command(pass_context=True, no_pm=True)
async def avatar(ctx, member: discord.Member = None):
    if member is None:
        await client.say("Please specify a user.")
    else:
        await client.reply("{} Here is the picture!".format(member.avatar_url))

@client.command(pass_context=True)
async def Userinfo(ctx, user: discord.Member = None):
    if user is None:
        await client.say("Please specify a user.")
    else:
        embed = discord.Embed
        embed.add_field(name="User Name Is:", value="{}".format(user.name), inline=False)
        embed.add_field(name="User ID Is:", value="{}".format(user.id), inline=False)
        embed.add_field(name="Created At:", value="{}".format(user.created_at), inline=False)
        embed.add_field(name="Top Role:", value="{}".format(user.top_role), inline=False)
        embed.add_field(name="Joined At", value="{}".format(user.joined_at), inline=False)
        embed.add_field(name="Status:", value="{}".format(user.status), inline=False)
        embed.add_field(name="Default Avatar:", value="{}".format(user.default_avatar), inline=False)
        await client.say(embed=embed)



client.run('NDg5NzA2ODgyNzU2MjQ3NTUz.Dnu0aQ.WP4gzmrdTl0wiMCK_stIXig2L0s')
