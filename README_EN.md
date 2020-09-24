# Discord Weather Bot

![PEP8 Test](https://github.com/Hipro-Official/Discord-Weather-Bot/workflows/PEP8%20Test/badge.svg)
![license](https://img.shields.io/badge/license-GPL--3.0-green)
![version](https://img.shields.io/badge/version-1.0.0-blue)
<br>

![image](./picture/Weather.png)

日本語をご所望の場合, [README.md](./README.md)をご参照ください。

This is the inventory page of the Discord Weather Bot. This Discord Weather Bot is only available for Japanese cities. <br>
If you want to use it with other cities in the world, please visit [Discord Weather Bot Global](https://github.com/Hipro-Official/Discord-Weather-Bot-Global). <br>

## Specification

Discord Weather Bot uses Heroku. The configuration is as follows.
![image](picture/Component.png)

### Features
The Discord Weather Bot has the following features.
1. Embed the day's weather for a specific city
2. Embed the next day's weather for a specific city
3. Embed weather for a week in a specific city
4. Embed the weather for the day at 6am daily
5. Embed the next day's weather at 6 p.m. daily

### Usage (code)
Config/config.py contains the URL of the API and the names of the environment variables that you have registered with Heroku. <br>
If the URL of the API has changed, please edit this file if you want to use a different environment variable name. <br>
Please refer to [here](https://devcenter.heroku.com/articles/config-vars#using-the-heroku-dashboard) for information on how to register Heroku environment variables. <br>.
In addition, the cities for the daily 6 a.m. and 6 p.m. weather forecasts, which are distributed at 6 a.m. and 6 p.m. daily, are maintained in [citylist.json](./JSON/citylist.json). When increasing the number of cities to be distributed, please follow the array notation in JSON.
For the city name, see the city name in the Usage (command).

### Usage (commands)
1. Look up the day's weather for a specific city.
    ```sh
    $day XXXX
    ```
2. Look up the next day's weather for a specific city.
    ```sh
    $tmr XXXX
    ```
3. Look up the week's weather for a specific city.
    ```sh
    $week XXXX
    ```
Please enter the city name in XXXX. You can use the following information for the city name.
|#|Item|Example|
|:-:|:-|:-|
|1|Prefectural level|東京都|
|2|Municipal level|東京都港区|
|3|Town level|東京都港区六本木|
|4|Chome level|東京都港区六本木1丁目|
<br>
In the code, the search is set at the Chome level, but it is also possible to search at the Prefectural level, Municipal level, and Town level.

### API
|#|API name|URL|
|:-:|:-|:-|
|1|Yahoo!ジオコーダAPI|https://developer.yahoo.co.jp/webapi/map/openlocalplatform/v1/geocoder.html|
|2|OpenWeatherMap API|https://openweathermap.org/api|
|3|HeartRails Geo API|https://geoapi.heartrails.com/api.html|

When using the APIs, please comply with the restrictions of each API provider.<br>

### 注意事項
You are free to modify the code, but if you modify all or part of the code in this Bot, please insert the following information as your license.
```
Code provided by Hipro
https://github.com/Hipro-Official
```

Hipro cannot be held responsible for any changes to the code in the files except for [config.py](Config/config.py) and [citylist.json](JSON/citylist.json) in this bot.<br>
If you have any problems, please issue a voucher in Issue.

### License
GNU GENERAL PUBLIC LICENSE v3.0