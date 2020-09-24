import datetime
import json

import discord
import pytz
from discord.ext import tasks

import Config.config as config
from embed import createembed
from ThirdpartyAPI.heartrails import heartrails

# Import files
from ThirdpartyAPI.openweathermap import openweathermap
from ThirdpartyAPI.yahoogeocode import yahoogeocode

# Discord related
discord_bot_token, channel_id_weather = config.discordconfig()

# Open citylist.json
citylistjson = open('./JSON/citylist.json', 'r')
citylist = json.load(citylistjson)

client = discord.Client()

# region Discord Connect


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if '$' in message.content is False:
        return

    messagecontent = None
    weatherinfo = None
    coordinateinfo = None
    embed = None

    # Incorrect Command Error
    if not ('$day' in message.content
            or '$tmr' in message.content
            or '$week' in message.content
            or '$help' in message.content):
        await message.channel.send('コマンドに誤りがあります')
        return

    messagecontent = message.content.split(' ')
    try:
        geoinfo = yahoogeocode(messagecontent[1])
        if geoinfo[0] != 0:
            await message.channel.send('エラーが発生しました')
        return
    except Exception:
        await message.channel.send('コマンドに誤りがあります')
    weatherinfo = openweathermap(geoinfo[1])
    coordinateinfo = heartrails(geoinfo[1])

    # $day command
    if message.content.startswith('$day'):
        embed = createembed(0, message, '', weatherinfo, coordinateinfo)
    # $tmr command
    elif message.content.startswith('$tmr'):
        embed = createembed(1, message, '', weatherinfo, coordinateinfo)
    # $week command
    elif message.content.startswith('$week'):
        embed = createembed(2, message, '', weatherinfo, coordinateinfo)
    # $help command
    elif message.content == '$help':
        embed = createembed(3, message, '', '', '')
    else:
        await message.channel.send('コマンドに誤りがあります')
        return

    await message.channel.send(embed=embed)


# endregion

# region Daily weather forecast


@tasks.loop(seconds=60)
async def loop():
    now = datetime.datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%H:%M')
    channel = client.get_channel(int(channel_id_weather))

    if now == '6:00':
        for i in range(len(citylist['city'])):
            geoinfo = yahoogeocode.yahoogeocoding(citylist['city'][i])
        weatherinfo = openweathermap.openweathermap(geoinfo[1])
        embed = createembed(4, '', citylist['city'][i], weatherinfo, '')
        await channel.send(embed=embed)
    elif now == '19:00':
        for i in range(len(citylist['city'])):
            geoinfo = yahoogeocode.yahoogeocoding(citylist['city'][i])
        weatherinfo = openweathermap.openweathermap(geoinfo[1])
        embed = createembed(5, '', citylist['city'][i], weatherinfo, '')
        await channel.send(embed=embed)


# endregion

# Loop
loop.start()

client.run(discord_bot_token)
