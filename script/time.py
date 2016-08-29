#!/usr/bin/python
# -*- coding: utf-8 -*-
# 日期脚本

import sys
from datetime import datetime
from lib import baidu_voice


# 现在时间
def time_now():
    baidu_voice.Voice.tts("现在时间：%s点%s分" % (datetime.now().hour, datetime.now().minute))


# 今天日期
def time_today():
    baidu_voice.Voice.tts("今天是：%s月%s号" % (datetime.now().month, datetime.now().day))


if __name__ == '__main__':
    param = sys.argv[1]

    if "now" == param:
        time_now()
    if "today" == param:
        time_today()
