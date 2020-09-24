import discord
import datetime
import Config.config as config


def createembed(mode, message, city, weatherinfo, coordinateinfo):
    embed = None

    # $day
    if mode == 0:
        daily = weatherinfo['daily'][0]
        max_temp = int(daily['temp']['max'])
        min_temp = int(daily['temp']['min'])
        description = daily['weather'][0]['description']
        icon = daily['weather'][0]['icon']

        embed = discord.Embed(
            title=str(message.content[5:]) + 'の今日の天気', color=5620992)
        embed.add_field(name='天気', value=description)
        embed.add_field(name='最低気温', value=str(min_temp) + '℃')
        embed.add_field(name='最高気温', value=str(max_temp) + '℃')
        embed.set_thumbnail(url=config.owmpicurl(icon))
        embed.set_footer(
            text='取得位置: '
            + coordinateinfo['prefecture']
            + coordinateinfo['city'],
            icon_url=config.fi)

    # $tmr
    elif mode == 1:
        daily = weatherinfo['daily'][1]
        max_temp = int(daily['temp']['max'])
        min_temp = int(daily['temp']['min'])
        description = daily['weather'][0]['description']
        icon = daily['weather'][0]['icon']

        embed = discord.Embed(
            title=str(message.content[5:]) + 'の明日の天気', color=5620992)
        embed.add_field(name='天気', value=description)
        embed.add_field(name='最低気温', value=str(min_temp) + '℃')
        embed.add_field(name='最高気温', value=str(max_temp) + '℃')
        embed.set_thumbnail(url=config.owmpicurl(icon))
        embed.set_footer(
            text='取得位置: '
            + coordinateinfo['prefecture']
            + coordinateinfo['city'],
            icon_url=config.fi)

    # $week
    elif mode == 2:
        embed = discord.Embed(
            title=str(message.content[5:]) + 'の１週間の天気', color=5620992)

        for i in range(7):
            daily = weatherinfo['daily'][i + 1]
            date = datetime.datetime.fromtimestamp(daily['dt'])
            max_temp = int(daily['temp']['max'])
            min_temp = int(daily['temp']['min'])
            description = daily['weather'][0]['description']

            embed.add_field(name='日付', value=str(date.year) +
                            '/' + str(date.month) + '/' + str(date.day))
            embed.add_field(name='天気', value=description)
            embed.add_field(name='気温（最低/最高）',
                            value=str(min_temp) + '℃/' + str(max_temp) + '℃')
            embed.set_footer(
                text='取得位置: '
                + coordinateinfo['prefecture']
                + coordinateinfo['city'],
                icon_url=config.fi)

    # $help
    elif mode == 3:
        embed = discord.Embed(title='Discord Weather Bot使用方法', color=0x1e90ff)
        embed.add_field(name='```$day XXXX```',
                        value='XXXXの当日の天気を配信', inline=False)
        embed.add_field(name='```$tmr XXXX```',
                        value='XXXXの翌日の天気を配信', inline=False)
        embed.add_field(name='```$week XXXX```',
                        value='XXXXの翌日からの１週間の天気を配信', inline=False)
        embed.add_field(name='```$help```', value='ヘルプを表示', inline=False)
        embed.add_field(
            name='注意',
            value='XXXXには都道府県、市区町村、町/大字、丁目/字が入ります。',
            inline=False)
        embed.set_footer(text='Discord Weather Bot',
                         icon_url=config.fi)

    # daily forecast
    elif mode == 4:
        daily = weatherinfo['daily'][0]
        max_temp = int(daily['temp']['max'])
        min_temp = int(daily['temp']['min'])
        description = daily['weather'][0]['description']
        icon = daily['weather'][0]['icon']

        embed = discord.Embed(title=city + 'の今日の天気', color=5620992)
        embed.add_field(name='天気', value=description)
        embed.add_field(name='最低気温', value=str(min_temp) + '℃')
        embed.add_field(name='最高気温', value=str(max_temp) + '℃')
        embed.set_thumbnail(url=config.owmpicurl(icon))

    elif mode == 5:
        daily = weatherinfo['daily'][1]
        max_temp = int(daily['temp']['max'])
        min_temp = int(daily['temp']['min'])
        description = daily['weather'][0]['description']
        icon = daily['weather'][0]['icon']

        embed = discord.Embed(title=city + 'の明日の天気', color=5620992)
        embed.add_field(name='天気', value=description)
        embed.add_field(name='最低気温', value=str(min_temp) + '℃')
        embed.add_field(name='最高気温', value=str(max_temp) + '℃')
        embed.set_thumbnail(url=config.owmpicurl(icon))

    return embed
