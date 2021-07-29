import discord
import logging
import asyncio
import os

from headcount import *

ROOT_DIR = os.path.abspath(os.curdir)
client = discord.Client()
logging.basicConfig(level=logging.ERROR)
headcountStatus = False

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('$headcount'):
        global headcountStatus
        if (headcountStatus is False):
            headcountStatus = True
            await start_headcount(client,message)

@client.event
async def on_reaction_add(reaction,user):
    global headcountStatus
    if (user.id != client.user.id and not user.bot): # Death to bots
        if (headcountStatus is not False): # Have we even begun?
            if (reaction.emoji == '❌'):
                if (user.permissions_in(reaction.message.channel).send_messages):
                    headcountStatus = False
                    await cancel_headcount(client, reaction, user)
            elif (reaction.emoji == '👍'):
                await update_headcount(client, reaction, user)
            elif (reaction.emoji == '✅'):
                if (user.permissions_in(reaction.message.channel).send_messages):
                    headcountStatus = False
                    await end_headcount(client, reaction, user)

t = open(ROOT_DIR + "/token.cfg", "r").read()

client.run(t)