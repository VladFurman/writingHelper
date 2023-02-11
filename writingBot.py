# This example requires the 'message_content' intent.

import re
import discord
from discord.ext import commands

import config

description = "It's a bot it goes ping when someone says five"

spiderInBatICID = 1073751352074829874
spiderInBatOOCID = 1073751824642887811
botTestID = 1073821842575462500

intents = discord.Intents.default()
intents.message_content = True

# client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='?',
                   description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    channel = bot.get_channel(1073821842575462500)
    await channel.send('`Initiate!`')


def hasFive(text):
    text = text.lower()
    m = re.search('\"([^"]*?)\"', text)
    for match in re.finditer('\"([^"]*?)\"', text):
        if 'five' in match[0]:
            return True

    return False


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id == spiderInBatICID or message.channel.id == botTestID:
        if hasFive(message.content):
            await bot.get_channel(spiderInBatOOCID).send('There\'s a five!')

bot.run(config.bot_key)