import requests
import Config.config as config

# OpenWeatherMap


def openweathermap(coordinate):
    complete_url = config.owmbaseurl(coordinate)
    response = requests.get(complete_url)
    weatherinfo = response.json()
    return weatherinfo
