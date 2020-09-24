import os

# region Global Variables
# DEBUG = 0, RELEASE = 1
currentMode = 0

# For Discord
fi = 'https://bit.ly/33TsUJh'

# For Yahoo Geocode API
yahoo_client_id = os.environ.get('YAHOO_CLIENT_ID')
yahoo_endpoint = 'https://map.yahooapis.jp/geocode/V1/geoCoder'

# For OpenWeatherMap API
owm_api_key = os.environ.get('OWM_API_KEY')
# endregion

# region Functions


def discordconfig():
    if currentMode == 0:
        discord_bot_token = os.environ.get('DISCORD_BOT_TOKEN_DEBUG')
        channel_id_weather = os.environ.get('WEATHER_CHANNEL_DEBUG')
        return discord_bot_token, channel_id_weather
    elif currentMode == 1:
        discord_bot_token = os.environ.get('DISCORD_BOT_TOKEN')
        channel_id_weather = os.environ.get('WEATHER_CHANNEL')
        return discord_bot_token, channel_id_weather


def owmbaseurl(coordinate):
    base_url = 'http://api.openweathermap.org/data/2.5/onecall?'
    split_coordinate = coordinate.split(',')
    url = (base_url + 'lat=' + str(split_coordinate[1]) + '&lon=' +
           str(split_coordinate[0]) +
           '&exclude=minutely,hourly&units=metric&lang=ja&appid=' +
           owm_api_key)
    return url


def owmpicurl(icon):
    return 'http://openweathermap.org/img/wn/' + icon + '@2x.png'
# endregion
