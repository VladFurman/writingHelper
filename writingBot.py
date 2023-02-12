# This example requires the 'message_content' intent.

import re
import discord
from discord.ext import commands

import config

description = "It's a bot it goes ping when someone says five"

intents = discord.Intents.default()
intents.message_content = True

# client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='?',
                   description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    channel = bot.get_channel(config.channelBotTestID)
    assert isinstance(channel, discord.TextChannel)
    await channel.send('`Initiate!`')


def hasFive(text):
    text = text.lower()
    for match in re.finditer('\"([^"]*?)\"', text):
        if 'five' in match[0]:
            return True

    return False


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id == config.channelToScanID or message.channel.id == config.channelBotTestID:
        if hasFive(message.content):
            if (message.author.id == config.userIdToScanForFive):
                channel = bot.get_channel(config.channelToReportID)
                assert isinstance(channel, discord.TextChannel)
                await channel.send('There\'s a five!')

bot.run(config.bot_key)
