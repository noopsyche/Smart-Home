#!/usr/bin/python
# -*- coding: utf-8 -*-
# 天气预报脚本

import sys
from datetime import datetime
from lib import baidu_voice
from lib import log
import sys
from urllib import request, parse
import json


def get_weather():
    url = 'https://api.thinkpage.cn/v3/weather/daily.json?'
    data = {
        "key": "enygxphjelwni53z",
        "location": "anyang",
        "language": "zh-Hans",
        "unit": "c",
        "start": "0",
        "days": "2",
    }
    url = url + parse.urlencode(data)
    req = request.Request(url)
    try:
        with request.urlopen(req, timeout=5) as req:
            content = req.read().decode("utf-8")
            data = json.loads(content)

            if data and isinstance(data, dict):
                return data["results"][0]["daily"]
            else:
                baidu_voice.Voice.tts("天气获取失败")

    except Exception as e:
        log.exp("获取天气 %s" % url, e)
        baidu_voice.Voice.tts("天气获取失败")
    return url


# 明天天气
def weather_tomorrow():
    data = get_weather()[1]
    if "" == data["precip"]:
        data["precip"] = "未知"

    # 计算风力等级
    if "" != data["wind_speed"]:
        if 1 > int(data["wind_speed"]):
            data["wind_level"] = 0
        if 1 <= int(data["wind_speed"]) <= 5:
            data["wind_level"] = 1
        if 6 <= int(data["wind_speed"]) <= 11:
            data["wind_level"] = 2
        if 12 <= int(data["wind_speed"]) <= 19:
            data["wind_level"] = 3
        if 20 <= int(data["wind_speed"]) <= 28:
            data["wind_level"] = 4
        if 29 <= int(data["wind_speed"]) <= 38:
            data["wind_level"] = 5
        if 39 <= int(data["wind_speed"]) <= 49:
            data["wind_level"] = 6
        if 50 <= int(data["wind_speed"]) <= 61:
            data["wind_level"] = 7
        if 62 <= int(data["wind_speed"]) <= 74:
            data["wind_level"] = 8
        if 75 <= int(data["wind_speed"]) <= 88:
            data["wind_level"] = 9
        if 89 <= int(data["wind_speed"]) <= 102:
            data["wind_level"] = 10

    baidu_voice.Voice.tts("明天天气：白天%s 晚间%s 最高温度 %s度 最低温度 %s度 降水概率 %s %s风 %s级" %
                          (data["text_day"], data["text_night"], data["high"], data["low"],
                           data["precip"], data["wind_direction"], data["wind_level"]))


# 今天天气
def weather_today():
    data = get_weather()[0]
    if "" == data["precip"]:
        data["precip"] = "未知"

    # 计算风力等级
    if "" != data["wind_speed"]:
        if 1 > int(data["wind_speed"]):
            data["wind_level"] = 0
        if 1 <= int(data["wind_speed"]) <= 5:
            data["wind_level"] = 1
        if 6 <= int(data["wind_speed"]) <= 11:
            data["wind_level"] = 2
        if 12 <= int(data["wind_speed"]) <= 19:
            data["wind_level"] = 3
        if 20 <= int(data["wind_speed"]) <= 28:
            data["wind_level"] = 4
        if 29 <= int(data["wind_speed"]) <= 38:
            data["wind_level"] = 5
        if 39 <= int(data["wind_speed"]) <= 49:
            data["wind_level"] = 6
        if 50 <= int(data["wind_speed"]) <= 61:
            data["wind_level"] = 7
        if 62 <= int(data["wind_speed"]) <= 74:
            data["wind_level"] = 8
        if 75 <= int(data["wind_speed"]) <= 88:
            data["wind_level"] = 9
        if 89 <= int(data["wind_speed"]) <= 102:
            data["wind_level"] = 10

    baidu_voice.Voice.tts("今天天气：白天%s 晚间%s 最高温度 %s度 最低温度 %s度 降水概率 %s %s风 %s级" %
                          (data["text_day"], data["text_night"], data["high"], data["low"],
                           data["precip"], data["wind_direction"], data["wind_level"]))

if __name__ == '__main__':
    param = sys.argv[1]

    if "today" == param:
        weather_today()

    if "tomorrow" == param:
        weather_tomorrow()
